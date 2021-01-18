import csv
import sys
import utils

def GenerateLabel(data_path, name_list_path, label_dic_path, time_message_path, timeout_message_path):
    with open(data_path, "r") as csvfile:
        data = list(csv.reader(csvfile))

    name_list = []
    label_dic = {}
    time_message = {}
    timeout_message = {}
    for line in data:
        method = "None"
        time = float(sys.maxsize)
        time_dic = {}
        timeout_dic = {}
        for index in range(len(utils.method_list)):
            if line[index + 1] == "timeout" or line[index + 1] == "failed" or line[index + 1] == "0.0":
                time_dic[utils.method_list[index]] = 3600.0
                timeout_dic[utils.method_list[index]] = True
            else:
                time_dic[utils.method_list[index]] = float(line[index + 1])
                timeout_dic[utils.method_list[index]] = False

            if line[index + 1] != "timeout" and line[index + 1] != "failed" and line[index + 1] != "0.0" and float(line[index + 1]) < time:
                time = float(line[index + 1])
                method = utils.method_list[index]
        time_message[line[0]] = time_dic
        timeout_message[line[0]] = timeout_dic
        if method != "None":
            name_list.append(line[0])
            label_dic[line[0]] = method
        else:
            print(line[0])
    utils.WriteJson(name_list, name_list_path)
    utils.WriteJson(label_dic, label_dic_path)
    utils.WriteJson(time_message, time_message_path)
    utils.WriteJson(timeout_message, timeout_message_path)

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

def StatisticSamples(test_label_dic_path, statistic_name_dic_path):
    test_label_dic = utils.ReadJson(test_label_dic_path)
    statistic_name_dic = {}
    for method in utils.method_list:
        statistic_name_dic[method] = []
    for name in test_label_dic.keys():
        statistic_name_dic[test_label_dic[name]].append(name)
    utils.WriteJson(statistic_name_dic, statistic_name_dic_path)
    
def JudgeSituation15(test_name_list_path):
    test_name_list = utils.ReadJson(test_name_list_path)
    for name in test_name_list:
        vec = utils.GetVec(utils.embedded_dir_1, name)
        if vec[14] != 0:
            print(name)
        

if __name__ == '__main__':
    basic_data_path = utils.basic_data_path
    
    train_data_path = basic_data_path + "train_data.csv"
    test_data_path = basic_data_path + "test_data.csv"
    train_name_list_path = basic_data_path + "train_name_list.json"
    test_name_list_path = basic_data_path + "test_name_list.json"
    train_label_dic_path = basic_data_path + "train_label_dic.json"
    test_label_dic_path = basic_data_path + "test_label_dic.json"
    train_time_message_path = basic_data_path + "train_time_message.json"
    test_time_message_path = basic_data_path + "test_time_message.json"
    train_timeout_message_path = basic_data_path + "train_timeout_message.json"
    test_timeout_message_path = basic_data_path + "test_timeout_message.json"

    statistic_name_dic_path = basic_data_path + "statistic_name_dic.json"

    GenerateLabel(train_data_path, train_name_list_path, train_label_dic_path, train_time_message_path, train_timeout_message_path)
    GenerateLabel(test_data_path, test_name_list_path, test_label_dic_path, test_time_message_path, test_timeout_message_path)

    # Statistic(train_label_dic_path, test_label_dic_path)

    StatisticSamples(test_label_dic_path, statistic_name_dic_path)
 
    # JudgeSituation15(train_name_list_path)
    # JudgeSituation15(test_name_list_path)


