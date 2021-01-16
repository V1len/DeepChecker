import csv
import utils
import sys
import random

if __name__ == '__main__':
    root_path = utils.root_path
    choose_top_method_number = utils.choose_top_method_number
    sum_method_number = utils.sum_method_number

    test_name_list_path = root_path + "test_name_list.json"
    
    test_set_predict_path = root_path + "test_set_predict/"
    test_set_predict_path_0 = test_set_predict_path + "test_set_predict_0.json"
    test_set_predict_path_1 = test_set_predict_path + "test_set_predict_1.json"
    test_set_predict_path_2 = test_set_predict_path + "test_set_predict_2.json"

    testdata_path = root_path + "test_data.csv"
    predictdata_path = root_path + "predict_data.csv"

    with open(testdata_path, newline='') as csvfile:
        data = list(csv.reader(csvfile))

    test_name_list = utils.ReadJson(test_name_list_path)
    method_list = utils.method_list
    for test_set_predict_path in [test_set_predict_path_0, test_set_predict_path_1, test_set_predict_path_2]:
        predict = utils.ReadJson(test_set_predict_path)
        statistic_dic = utils.InitialDic()
        for index in range(len(data)):
            target_method_list = predict[test_name_list[index]]
            predict_time = "None"
            point = 0
            for i in range(choose_top_method_number):
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
        target_method_list = predict[test_name_list[index]]
        predict_time = "timeout"
        point = 0
        for i in range(sum_method_number):
            target_method = target_method_list[i]
            if target_method in method_list:
                temp_point = method_list.index(target_method) + 1
                temp_time = data[index][temp_point]
                if temp_time != "timeout" and temp_time != "failed" and temp_time != "0.0":
                    if predict_time == "timeout":
                        predict_time = temp_time
                        point = temp_point
                    elif float(temp_time) < float(predict_time):
                        predict_time = temp_time
                        point = temp_point
            else:
                print("no suitable checker")
        data[index].append(predict_time)
        

    title = "filename"
    for method in method_list:
        title = title + "," + method
    for DeepChecker in utils.DeepChecker_list:
        title = title + "," + DeepChecker
    with open(predictdata_path, "w") as writer:
        writer.write(title + ",GroundTruth\n")
        for line in data:
            writer.write(",".join(line)+"\n")