from sklearn.ensemble import RandomForestRegressor
import utils
import os


def GetLabelList(name_list, label_dic):
    label_list = []
    method_list = utils.method_list
    for name in name_list:
        aig_label = label_dic[name]
        if aig_label in method_list:
            label = method_list.index(aig_label)
        else:
            label = -1
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
        temp_predict = method_list[predict_label_list[i]]
        test_set_predict[test_name] = temp_predict
    utils.WriteJson(test_set_predict, test_set_predict_path)
    return test_set_predict

def RandomForest(embedded_dir, train_name_list, test_name_list, test_set_predict_path, new_format):
    train_vec_dic = GetVecList(embedded_dir, train_name_list)
    test_vec_dic = GetVecList(embedded_dir, test_name_list)

    model = RandomForestClassifier(n_estimators=1000, max_depth=None)
    model.fit(train_vec_dic, train_label_list)
    predict_label_list = model.predict(test_vec_dic)

    acc = (predict_label_list == test_label_list).sum() / len(test_label_list)
    print(acc)

    test_set_predict = GeneratePredictResult(test_name_list, predict_label_list, test_set_predict_path)

    result = {}
    for name in test_name_list:
        if name in new_format:
            result[name] = test_set_predict[name]
    print(len(result.keys()))

    method_list = utils.method_list
    statistic_dic = {}
    for method in method_list:
        statistic_dic[method] = 0
    for key in result.keys():
        value = result[key]
        statistic_dic[value] += 1
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

    new_format = utils.ReadJson(utils.new_format_json_path)
    RandomForest(embedded_dir_0, train_name_list, test_name_list, test_set_predict_path_0, new_format)
    RandomForest(embedded_dir_1, train_name_list, test_name_list, test_set_predict_path_1, new_format)
    RandomForest(embedded_dir_2, train_name_list, test_name_list, test_set_predict_path_2, new_format)






















