from sklearn.ensemble import RandomForestRegressor
import utils
import os
import numpy as np
np.seterr(divide='ignore',invalid='ignore')

from sklearn.model_selection import GridSearchCV
from sklearn import metrics

def GetTimeList(name_list, time_message, method):
    time_list = []
    for name in name_list:
        time = time_message[name][method]
        time_list.append(time)
    return time_list

def RandomForest(embedded_dir, train_name_list, test_name_list, train_time_message, time_predict_path, layer,
                                                                                    max_depth, min_samples_split=2, min_samples_leaf=1):
    time_model_path = utils.time_model_path
    train_vec_list = utils.GetVecList(embedded_dir, train_name_list)
    test_vec_list = utils.GetVecList(embedded_dir, test_name_list)
    time_predict_message = {}
    for method in utils.method_list:
        whole_time_model_path = time_model_path + method + "_model_" + layer + ".pkl"
        train_time_list = GetTimeList(train_name_list, train_time_message, method)
        model = RandomForestRegressor(n_estimators=100, criterion="mse", max_depth=max_depth, min_samples_split=min_samples_split, min_samples_leaf=min_samples_leaf)
        model.fit(train_vec_list, train_time_list)
        utils.Save_pkl(model, whole_time_model_path)
        predict_time_list = model.predict(test_vec_list)
        time_predict_message[method] = predict_time_list.tolist()
    utils.WriteJson(time_predict_message, time_predict_path)


if __name__ == '__main__':
    root_path = utils.root_path
    use_all_methods = utils.use_all_methods

    embedded_dir_0 = utils.embedded_dir_0
    embedded_dir_1 = utils.embedded_dir_1
    embedded_dir_2 = utils.embedded_dir_2

    basic_data_path = utils.basic_data_path
    train_name_list_path = basic_data_path + "train_name_list.json"
    train_time_message_path = basic_data_path + "train_time_message.json"
    test_name_list_path = basic_data_path + "test_name_list.json"
    test_time_message_path = basic_data_path + "test_time_message.json"

    train_name_list = utils.ReadJson(train_name_list_path)
    train_time_message = utils.ReadJson(train_time_message_path)
    test_name_list = utils.ReadJson(test_name_list_path)
    test_time_message = utils.ReadJson(test_time_message_path)

    time_predict_path = utils.time_predict_path
    time_predict_path_0 = time_predict_path + "time_predict_0.json"
    time_predict_path_1 = time_predict_path + "time_predict_1.json"
    time_predict_path_2 = time_predict_path + "time_predict_2.json"

    layer_0 = "0"
    layer_1 = "1"
    layer_2 = "2"

    if use_all_methods:
        RandomForest(embedded_dir_0, train_name_list, test_name_list, train_time_message, time_predict_path_0, layer_0, max_depth=1, min_samples_split=2, min_samples_leaf=1)
        RandomForest(embedded_dir_1, train_name_list, test_name_list, train_time_message, time_predict_path_1, layer_1, max_depth=1, min_samples_split=2, min_samples_leaf=1)
        RandomForest(embedded_dir_2, train_name_list, test_name_list, train_time_message, time_predict_path_2, layer_2, max_depth=5, min_samples_split=2, min_samples_leaf=1)
    else:
        RandomForest(embedded_dir_0, train_name_list, test_name_list, train_time_message, time_predict_path_0, layer_0, max_depth=3, min_samples_split=3, min_samples_leaf=1)
        RandomForest(embedded_dir_1, train_name_list, test_name_list, train_time_message, time_predict_path_1, layer_1, max_depth=4, min_samples_split=3, min_samples_leaf=1)
        RandomForest(embedded_dir_2, train_name_list, test_name_list, train_time_message, time_predict_path_2, layer_2, max_depth=None, min_samples_split=3, min_samples_leaf=1)
