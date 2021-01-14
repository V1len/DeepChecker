from sklearn.ensemble import RandomForestRegressor
import utils
import os
import numpy as np
np.seterr(divide='ignore',invalid='ignore')


def GetLabelList(name_list, label_dic):
    label_list = []
    method_list = utils.method_list
    for name in name_list:
        aig_label = label_dic[name]
        assert(aig_label in method_list)
        label = method_list.index(aig_label)
        label_list.append(label)
    return label_list

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


    estimator = RandomForestClassifier(n_estimators=100, criterion="entropy", max_depth=10, min_samples_split=2)
    param_test2= {'min_samples_leaf':range(1,50,1)}
    gsearch2= GridSearchCV(estimator, param_grid = param_test2, iid=False, cv=5)
    gsearch2.fit(X,y)
    print(gsearch2.cv_results_,gsearch2.best_params_, gsearch2.best_score_)
    


def RandomForest(embedded_dir, train_name_list, test_name_list, train_label_list, test_label_list, test_set_predict_path, model_path, importance_path,
                                                                                    max_depth, min_samples_split=2, min_samples_leaf=1):
    train_vec_list = utils.GetVecList(embedded_dir, train_name_list)
    test_vec_list = utils.GetVecList(embedded_dir, test_name_list)
    model = RandomForestRegressor(n_estimators=100, criterion="entropy", max_depth=max_depth, min_samples_split=min_samples_split, min_samples_leaf=min_samples_leaf)
    classifier = model.fit(train_vec_list, train_label_list)
    utils.Save_pkl(classifier, model_path)
    predictions = classifier.predict_proba(test_vec_list)
    predict_label_list = np.argsort(-predictions, axis=1)
    importance = model.feature_importances_
    utils.WriteJson(importance.tolist(), importance_path)
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
    use_all_methods = utils.use_all_methods

    embedded_dir_0 = utils.embedded_dir_0
    embedded_dir_1 = utils.embedded_dir_1
    embedded_dir_2 = utils.embedded_dir_2

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

    test_set_predict_path = root_path + "test_set_predict/"
    test_set_predict_path_0 = test_set_predict_path + "test_set_predict_0.json"
    test_set_predict_path_1 = test_set_predict_path + "test_set_predict_1.json"
    test_set_predict_path_2 = test_set_predict_path + "test_set_predict_2.json"

    model_path = root_path + "model/"
    model_path_0 = model_path + "model_0.pkl"
    model_path_1 = model_path + "model_1.pkl"
    model_path_2 = model_path + "model_2.pkl"
    
    importance_message_path = root_path + "importance_message/"
    tools_importance_path_0 = importance_message_path + "tools_importance_0.json"
    tools_importance_path_1 = importance_message_path + "tools_importance_1.json"
    tools_importance_path_2 = importance_message_path + "tools_importance_2.json"
    
    iimc_importance_path_0 = importance_message_path + "iimc_importance_0.json"
    iimc_importance_path_1 = importance_message_path + "iimc_importance_1.json"
    iimc_importance_path_2 = importance_message_path + "iimc_importance_2.json"


    if use_all_methods:
        RandomForest(embedded_dir_0, train_name_list, test_name_list, train_label_list, test_label_list, test_set_predict_path_0, model_path_0, tools_importance_path_0, max_depth=1, min_samples_split=2, min_samples_leaf=1)
        RandomForest(embedded_dir_1, train_name_list, test_name_list, train_label_list, test_label_list, test_set_predict_path_1, model_path_1, tools_importance_path_1, max_depth=1, min_samples_split=2, min_samples_leaf=1)
        RandomForest(embedded_dir_2, train_name_list, test_name_list, train_label_list, test_label_list, test_set_predict_path_2, model_path_2, tools_importance_path_2, max_depth=5, min_samples_split=2, min_samples_leaf=1)
    else:
        RandomForest(embedded_dir_0, train_name_list, test_name_list, train_label_list, test_label_list, test_set_predict_path_0, model_path_0, iimc_importance_path_0, max_depth=3, min_samples_split=3, min_samples_leaf=1)
        RandomForest(embedded_dir_1, train_name_list, test_name_list, train_label_list, test_label_list, test_set_predict_path_1, model_path_1, iimc_importance_path_1, max_depth=4, min_samples_split=3, min_samples_leaf=1)
        RandomForest(embedded_dir_2, train_name_list, test_name_list, train_label_list, test_label_list, test_set_predict_path_2, model_path_2, iimc_importance_path_2, max_depth=None, min_samples_split=3, min_samples_leaf=1)


