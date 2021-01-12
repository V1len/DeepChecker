from sklearn.ensemble import RandomForestClassifier
import utils
import os
import numpy as np
np.seterr(divide='ignore',invalid='ignore')

from sklearn.model_selection import GridSearchCV
from sklearn import metrics


def GetLabelList(name_list, label_dic):
    label_list = []
    method_list = utils.method_list
    for name in name_list:
        aig_label = label_dic[name]
        assert(aig_label in method_list)
        label = method_list.index(aig_label)
        label_list.append(label)
    return label_list

def GetVecList(dir, name_list):
    vec_list = []
    for name in name_list:
        aig_name = name + ".vector"
        aig_path = os.path.join(dir, aig_name)
        if os.path.isfile(aig_path):
            vector = []
            with open(aig_path, encoding='utf-8') as fp:
                line = fp.readlines()[0].split("[")[1].split("]")[0]
                items = line.split(", ")
                for item in items:
                    vector.append(int(item))
                fp.close()
            vec_list.append(vector)
        else:
            print(aig_name)
    return vec_list 

def GeneratePredictResult(test_name_list, predict_label_list, test_set_predict_path):
    test_set_predict = {}
    method_list = utils.method_list
    for i in range(len(test_name_list)):
        test_name = test_name_list[i]
        temp_predict = []
        for predict in predict_label_list[i]:
            temp_predict.append(method_list[predict])
        test_set_predict[test_name] = temp_predict
    utils.WriteJson(test_set_predict, test_set_predict_path)

    method_list = utils.method_list
    choose_top_method_number = utils.choose_top_method_number
    for i in range(choose_top_method_number):
        top_i_method_dic = {}
        for j in range(len(test_name_list)):
            test_name = test_name_list[j]
            top_i_method_dic[test_name] = test_set_predict[test_name][i]
        statistic_dic = utils.Statistic([top_i_method_dic])
        print(statistic_dic)

    return test_set_predict

def GetAcc(predict_label_list, test_label_list):
    choose_top_method_number = utils.choose_top_method_number
    sum_acc = 0
    for i in range(choose_top_method_number):
        acc = (predict_label_list[:, i] == test_label_list).sum() / len(test_label_list)
        sum_acc += acc
    return sum_acc

def RandomForestTest(embedded_dir, train_name_list, test_name_list, train_label_list, test_label_list, test_set_predict_path):
    X = GetVecList(embedded_dir, train_name_list)
    test_X = GetVecList(embedded_dir, test_name_list)
    y = train_label_list
    test_y = test_label_list

    # model = RandomForestClassifier(n_estimators=70, criterion="entropy", max_depth=5, min_samples_split=12)
    # classifier = model.fit(X, y)
    # predictions = classifier.predict_proba(test_X)
    # # print(predictions)
    # predict_label_list = np.argsort(-predictions, axis=1)
    # # print(predict_label_list)
    
    # sum_acc = GetAcc(predict_label_list, test_y)
    # print(sum_acc)

    # test_set_predict = GeneratePredictResult(test_name_list, predict_label_list, test_set_predict_path)
    # Statistic(test_name_list, test_set_predict)

    # estimator = RandomForestClassifier()
    # param_test1= {'n_estimators':range(10,201,10)}
    # gsearch1= GridSearchCV(estimator = estimator, param_grid =param_test1, cv=5)
    # gsearch1.fit(X,y)
    # print(gsearch1.cv_results_,gsearch1.best_params_, gsearch1.best_score_)

    # estimator = RandomForestClassifier(n_estimators=100, criterion="entropy")
    # param_test2= {'max_depth':range(1,50,1)}
    # gsearch2= GridSearchCV(estimator, param_grid = param_test2, iid=False, cv=5)
    # gsearch2.fit(X,y)
    # print(gsearch2.cv_results_,gsearch2.best_params_, gsearch2.best_score_)

    # estimator = RandomForestClassifier(n_estimators=100, criterion="entropy", max_depth=10)
    # param_test2= {'min_samples_split':range(2,50,1)}
    # gsearch2= GridSearchCV(estimator, param_grid = param_test2, iid=False, cv=5)
    # gsearch2.fit(X,y)
    # print(gsearch2.cv_results_,gsearch2.best_params_, gsearch2.best_score_)

    estimator = RandomForestClassifier(n_estimators=100, criterion="entropy", max_depth=10, min_samples_split=2)
    param_test2= {'min_samples_leaf':range(1,50,1)}
    gsearch2= GridSearchCV(estimator, param_grid = param_test2, iid=False, cv=5)
    gsearch2.fit(X,y)
    print(gsearch2.cv_results_,gsearch2.best_params_, gsearch2.best_score_)
    


def RandomForest(embedded_dir, train_name_list, test_name_list, train_label_list, test_label_list, test_set_predict_path, model_path, 
                                                                                    max_depth, min_samples_split=2, min_samples_leaf=1):
    train_vec_list = GetVecList(embedded_dir, train_name_list)
    test_vec_list = GetVecList(embedded_dir, test_name_list)

    model = RandomForestClassifier(n_estimators=100, criterion="entropy", max_depth=max_depth, min_samples_split=min_samples_split, min_samples_leaf=min_samples_leaf)
    classifier = model.fit(train_vec_list, train_label_list)
    utils.Save_pkl(classifier, model_path)
    predictions = classifier.predict_proba(test_vec_list)
    predict_label_list = np.argsort(-predictions, axis=1) 
    
    sum_acc = GetAcc(predict_label_list, test_label_list)
    print(sum_acc)

    test_set_predict = GeneratePredictResult(test_name_list, predict_label_list, test_set_predict_path)
    Statistic(test_name_list, test_set_predict)

def Statistic(test_name_list, test_set_predict):
    new_format = utils.ReadJson(utils.new_format_json_path)
    result = {}
    for name in test_name_list:
        if name in new_format:
            result[name] = test_set_predict[name][0]
    if len(result.keys()) != 0:
        statistic_dic = utils.Statistic([result])
        print(statistic_dic)


if __name__ == '__main__':
    root_path = utils.root_path

    embedding_date_0 = "2021-1-2_v0.1"
    embedding_date_1 = "2020-12-24_v1.1"
    embedding_date_2 = "2021-1-2_v2.2"
    # embedding_date_0 = "2020-12-11_v0"
    # embedding_date_1 = "2020-12-24_v1.1"
    # embedding_date_2 = "2020-12-24_v2.1"

    embedded_dir_0 = "/mnt/hd0/DeepChecker/embedding/embedded/" + embedding_date_0
    embedded_dir_1 = "/mnt/hd0/DeepChecker/embedding/embedded/" + embedding_date_1
    embedded_dir_2 = "/mnt/hd0/DeepChecker/embedding/embedded/" + embedding_date_2

    train_name_list_path = root_path + "train_name_list.json"
    train_label_dic_path = root_path + "train_label_dic.json"
    test_name_list_path = root_path + "test_name_list.json"
    test_label_dic_path = root_path + "test_label_dic.json"

    train_name_list = utils.ReadJson(train_name_list_path)
    train_label_dic = utils.ReadJson(train_label_dic_path)
    test_name_list = utils.ReadJson(test_name_list_path)
    test_label_dic = utils.ReadJson(test_label_dic_path)

    train_label_list = GetLabelList(train_name_list, train_label_dic)
    test_label_list = GetLabelList(test_name_list, test_label_dic)

    test_set_predict_path_0 = root_path + "test_set_predict_0.json"
    test_set_predict_path_1 = root_path + "test_set_predict_1.json"
    test_set_predict_path_2 = root_path + "test_set_predict_2.json"

    model_path_0 = root_path + "model_0.pkl"
    model_path_1 = root_path + "model_1.pkl"
    model_path_2 = root_path + "model_2.pkl"


    # RandomForestTest(embedded_dir_0, train_name_list, test_name_list, train_label_list, test_label_list, test_set_predict_path_0)
    # RandomForestTest(embedded_dir_1, train_name_list, test_name_list, train_label_list, test_label_list, test_set_predict_path_1)
    # RandomForestTest(embedded_dir_2, train_name_list, test_name_list, train_label_list, test_label_list, test_set_predict_path_2)

    # RandomForest(embedded_dir_0, train_name_list, test_name_list, train_label_list, test_label_list, test_set_predict_path_0, model_path_0, max_depth=10, min_samples_split=2, min_samples_leaf=2)
    # RandomForest(embedded_dir_1, train_name_list, test_name_list, train_label_list, test_label_list, test_set_predict_path_1, model_path_1, max_depth=10, min_samples_split=4, min_samples_leaf=2)
    # RandomForest(embedded_dir_2, train_name_list, test_name_list, train_label_list, test_label_list, test_set_predict_path_2, model_path_2, max_depth=14, min_samples_split=4, min_samples_leaf=1)

    # RandomForest(embedded_dir_0, train_name_list, test_name_list, train_label_list, test_label_list, test_set_predict_path_0, model_path_0, max_depth=1, min_samples_split=2, min_samples_leaf=1)
    # RandomForest(embedded_dir_1, train_name_list, test_name_list, train_label_list, test_label_list, test_set_predict_path_1, model_path_1, max_depth=1, min_samples_split=2, min_samples_leaf=1)
    # RandomForest(embedded_dir_2, train_name_list, test_name_list, train_label_list, test_label_list, test_set_predict_path_2, model_path_2, max_depth=1, min_samples_split=2, min_samples_leaf=1)

    RandomForest(embedded_dir_0, train_name_list, test_name_list, train_label_list, test_label_list, test_set_predict_path_0, model_path_0, max_depth=5, min_samples_split=2, min_samples_leaf=1)
    RandomForest(embedded_dir_1, train_name_list, test_name_list, train_label_list, test_label_list, test_set_predict_path_1, model_path_1, max_depth=5, min_samples_split=2, min_samples_leaf=1)
    RandomForest(embedded_dir_2, train_name_list, test_name_list, train_label_list, test_label_list, test_set_predict_path_2, model_path_2, max_depth=5, min_samples_split=2, min_samples_leaf=1)






















