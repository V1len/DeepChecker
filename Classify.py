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

def GeneratePredictResult(test_name_list, predict_label_list, classify_predict_path):
    classify_predict = {}
    method_list = utils.method_list
    for i in range(len(test_name_list)):
        test_name = test_name_list[i]
        temp_predict = []
        for predict in predict_label_list[i]:
            temp_predict.append(method_list[predict])
        classify_predict[test_name] = temp_predict
    utils.WriteJson(classify_predict, classify_predict_path)


    method_list = utils.method_list
    choose_top_method_number = utils.choose_top_method_number
    for i in range(choose_top_method_number):
        top_i_method_dic = {}
        for j in range(len(test_name_list)):
            test_name = test_name_list[j]
            top_i_method_dic[test_name] = classify_predict[test_name][i]
        statistic_dic = utils.Statistic([top_i_method_dic])
        print(statistic_dic)

    return classify_predict

def GetAcc(predict_label_list, test_label_list):
    choose_top_method_number = utils.choose_top_method_number
    sum_acc = 0
    for i in range(choose_top_method_number):
        acc = (predict_label_list[:, i] == test_label_list).sum() / len(test_label_list)
        sum_acc += acc
    return sum_acc

def RandomForestTest(embedded_dir, train_name_list, test_name_list, train_label_list, test_label_list, test_set_predict_path):
    X = utils.GetVecList(embedded_dir, train_name_list)
    test_X = utils.GetVecList(embedded_dir, test_name_list)
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
    
def RandomForest(embedded_dir, train_name_list, test_name_list, train_label_list, test_label_list, classify_predict_path, model_path, importance_path,
                                                                                    max_depth, min_samples_split=2, min_samples_leaf=1):
    train_vec_list = utils.GetVecList(embedded_dir, train_name_list)
    test_vec_list = utils.GetVecList(embedded_dir, test_name_list)
    model = RandomForestClassifier(n_estimators=100, criterion="entropy", max_depth=max_depth, min_samples_split=min_samples_split, min_samples_leaf=min_samples_leaf)
    classifier = model.fit(train_vec_list, train_label_list)
    utils.Save_pkl(classifier, model_path)
    predictions = classifier.predict_proba(test_vec_list)
    predict_label_list = np.argsort(-predictions, axis=1)
    importance = model.feature_importances_
    utils.WriteJson(importance.tolist(), importance_path)
    sum_acc = GetAcc(predict_label_list, test_label_list)
    print(sum_acc)
    classify_predict = GeneratePredictResult(test_name_list, predict_label_list, classify_predict_path)
    Statistic(test_name_list, classify_predict)


def Statistic(test_name_list, classify_predict):
    new_format = utils.ReadJson(utils.new_format_json_path)
    result = {}
    for name in test_name_list:
        if name in new_format:
            result[name] = classify_predict[name][0]
    if len(result.keys()) != 0:
        statistic_dic = utils.Statistic([result])
        print(statistic_dic)


if __name__ == '__main__':
    root_path = utils.root_path
    use_all_methods = utils.use_all_methods

    embedded_dir_0 = utils.embedded_dir_0
    embedded_dir_1 = utils.embedded_dir_1
    embedded_dir_2 = utils.embedded_dir_2

    basic_data_path = utils.basic_data_path
    train_name_list_path = basic_data_path + "train_name_list.json"
    train_label_dic_path = basic_data_path + "train_label_dic.json"
    test_name_list_path = basic_data_path + "test_name_list.json"
    test_label_dic_path = basic_data_path + "test_label_dic.json"

    train_name_list = utils.ReadJson(train_name_list_path)
    train_label_dic = utils.ReadJson(train_label_dic_path)
    test_name_list = utils.ReadJson(test_name_list_path)
    test_label_dic = utils.ReadJson(test_label_dic_path)

    train_label_list = GetLabelList(train_name_list, train_label_dic)
    test_label_list = GetLabelList(test_name_list, test_label_dic)

    classify_predict_path = utils.classify_predict_path
    classify_predict_path_0 = classify_predict_path + "classify_predict_0.json"
    classify_predict_path_1 = classify_predict_path + "classify_predict_1.json"
    classify_predict_path_2 = classify_predict_path + "classify_predict_2.json"

    classify_model_path = utils.classify_model_path
    classify_model_path_0 = classify_model_path + "model_0.pkl"
    classify_model_path_1 = classify_model_path + "model_1.pkl"
    classify_model_path_2 = classify_model_path + "model_2.pkl"
    
    importance_message_path = utils.importance_message_path
    importance_path_0 = importance_message_path + "importance_0.json"
    importance_path_1 = importance_message_path + "importance_1.json"
    importance_path_2 = importance_message_path + "importance_2.json"

    # RandomForestTest(embedded_dir_0, train_name_list, test_name_list, train_label_list, test_label_list, test_set_predict_path_0)
    # RandomForestTest(embedded_dir_1, train_name_list, test_name_list, train_label_list, test_label_list, test_set_predict_path_1)
    # RandomForestTest(embedded_dir_2, train_name_list, test_name_list, train_label_list, test_label_list, test_set_predict_path_2)

    if use_all_methods:
        RandomForest(embedded_dir_0, train_name_list, test_name_list, train_label_list, test_label_list, classify_predict_path_0, classify_model_path_0, importance_path_0, max_depth=1, min_samples_split=2, min_samples_leaf=1)
        RandomForest(embedded_dir_1, train_name_list, test_name_list, train_label_list, test_label_list, classify_predict_path_1, classify_model_path_1, importance_path_1, max_depth=1, min_samples_split=2, min_samples_leaf=1)
        RandomForest(embedded_dir_2, train_name_list, test_name_list, train_label_list, test_label_list, classify_predict_path_2, classify_model_path_2, importance_path_2, max_depth=5, min_samples_split=2, min_samples_leaf=1)
    else:
        RandomForest(embedded_dir_0, train_name_list, test_name_list, train_label_list, test_label_list, classify_predict_path_0, classify_model_path_0, importance_path_0, max_depth=3, min_samples_split=3, min_samples_leaf=1)
        RandomForest(embedded_dir_1, train_name_list, test_name_list, train_label_list, test_label_list, classify_predict_path_1, classify_model_path_1, importance_path_1, max_depth=4, min_samples_split=3, min_samples_leaf=1)
        RandomForest(embedded_dir_2, train_name_list, test_name_list, train_label_list, test_label_list, classify_predict_path_2, classify_model_path_2, importance_path_2, max_depth=None, min_samples_split=3, min_samples_leaf=1)


