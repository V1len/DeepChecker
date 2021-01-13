import csv
import sys
import utils

def GenerateLabel(data_path, name_list_path, label_dic_path):
    with open(data_path, "r") as csvfile:
        data = list(csv.reader(csvfile))

    name_list = []
    label_dic = {}
    for line in data:
        method = "None"
        time = float(sys.maxsize)
        for index in range(len(utils.method_list)):
            if line[index + 1] != "timeout" and line[index + 1] != "failed" and line[index + 1] != "0.0" and float(line[index + 1]) < time:
                time = float(line[index + 1])
                method = utils.method_list[index]
        if method != "None":
            name_list.append(line[0])
            label_dic[line[0]] = method
        else:
            print(line[0])
    utils.WriteJson(name_list, name_list_path)
    utils.WriteJson(label_dic, label_dic_path)

def Statistic(train_label_dic_path, test_label_dic_path):
    train_label_dic = utils.ReadJson(train_label_dic_path)
    test_label_dic = utils.ReadJson(test_label_dic_path)
    statistic_dic = utils.Statistic([train_label_dic])
    print("train_data")
    print(statistic_dic)
    statistic_dic = utils.Statistic([test_label_dic])
    print("test_data")
    print(statistic_dic)
    statistic_dic = utils.Statistic([train_label_dic, test_label_dic])
    print("all_data")
    print(statistic_dic)
    


if __name__ == '__main__':
    root_path = utils.root_path

    train_data_path = root_path + "train_data.csv"
    test_data_path = root_path + "test_data.csv"
    train_name_list_path = root_path + "train_name_list.json"
    train_label_dic_path = root_path + "train_label_dic.json"
    test_name_list_path = root_path + "test_name_list.json"
    test_label_dic_path = root_path + "test_label_dic.json"

    GenerateLabel(train_data_path, train_name_list_path, train_label_dic_path)
    GenerateLabel(test_data_path, test_name_list_path, test_label_dic_path)

    Statistic(train_label_dic_path, test_label_dic_path)


