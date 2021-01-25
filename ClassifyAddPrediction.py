import csv
import utils
import sys
import random

def ClassifyAddPrediction(data_path, name_list_path, predict_data_path, 
                        classify_predict_path_0, classify_predict_path_1, classify_predict_path_2):
    with open(data_path, newline='') as csvfile:
        data = list(csv.reader(csvfile))

    name_list = utils.ReadJson(name_list_path)
    method_list = utils.method_list
    for set_predict_path in [classify_predict_path_0, classify_predict_path_1, classify_predict_path_2]:
        predict = utils.ReadJson(set_predict_path)
        statistic_dic = utils.InitialDic()
        for index in range(len(data)):
            target_method_list = predict[name_list[index]]
            predict_time = "None"
            point = 0
            for i in range(utils.choose_top_method_number):
                target_method = target_method_list[i]
                assert(target_method in method_list)
                temp_point = method_list.index(target_method) + 1
                temp_time = data[index][temp_point]
                if predict_time == "None":
                    predict_time = temp_time
                    point = temp_point
                elif temp_time != "timeout" and temp_time != "failed" and temp_time != "0.0":
                    if predict_time == "timeout" or predict_time == "failed" or predict_time == "0.0":
                        predict_time = temp_time
                        point = temp_point
                    elif float(temp_time) < float(predict_time):
                        predict_time = temp_time
                        point = temp_point                
            data[index].append(predict_time)
            statistic_dic[method_list[point - 1]] += 1
        # print(statistic_dic)

    for index in range(len(data)):
        target_method_list = predict[name_list[index]]
        predict_time = "timeout"
        for i in range(utils.sum_method_number):
            target_method = target_method_list[i]
            if target_method in method_list:
                temp_point = method_list.index(target_method) + 1
                temp_time = data[index][temp_point]
                if temp_time != "timeout" and temp_time != "failed" and temp_time != "0.0":
                    if predict_time == "timeout":
                        predict_time = temp_time
                    elif float(temp_time) < float(predict_time):
                        predict_time = temp_time
            else:
                print("no suitable checker")
        data[index].append(predict_time)

    for index in range(len(data)):
        random_point = random.randint(1, len(utils.method_list))
        data[index].append(data[index][random_point])
        
    title = "filename"
    for method in method_list:
        title = title + "," + method
    for encoding_layer_list in utils.encoding_layer_list:
        title = title + "," + encoding_layer_list
    with open(predict_data_path, "w") as writer:
        writer.write(title + ",Ground Truth,Random\n")
        for line in data:
            writer.write(",".join(line) + "\n")


if __name__ == '__main__':
    classify_predict_path = utils.classify_predict_path
    classify_predict_path_0 = classify_predict_path + "classify_predict_0.json"
    classify_predict_path_1 = classify_predict_path + "classify_predict_1.json"
    classify_predict_path_2 = classify_predict_path + "classify_predict_2.json"
    classify_train_predict_path_0 = classify_predict_path + "classify_train_predict_0.json"
    classify_train_predict_path_1 = classify_predict_path + "classify_train_predict_1.json"
    classify_train_predict_path_2 = classify_predict_path + "classify_train_predict_2.json"
    

    classify_basic_data_path = utils.classify_basic_data_path
    test_name_list_path = classify_basic_data_path + "test_name_list.json"
    test_data_path = classify_basic_data_path + "test_data.csv"
    predict_data_path = classify_basic_data_path + "classify_predict_data.csv"
    train_name_list_path = classify_basic_data_path + "train_name_list.json"
    train_data_path = classify_basic_data_path + "train_data.csv"
    train_predict_data_path = classify_basic_data_path + "classify_train_predict_data.csv"

    ClassifyAddPrediction(test_data_path, test_name_list_path, predict_data_path, 
                            classify_predict_path_0, classify_predict_path_1, classify_predict_path_2)
    ClassifyAddPrediction(train_data_path, train_name_list_path, train_predict_data_path, 
                            classify_train_predict_path_0, classify_train_predict_path_1, classify_train_predict_path_2)

