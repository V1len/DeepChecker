import csv
import utils
import sys
import random
import numpy as np
import matplotlib.pyplot as plt

def Sort(test_name_list, time_list):
    index_list = np.array(time_list).argsort()
    name_list = []
    for index in index_list:
        name_list.append(test_name_list[index])
    return name_list

def GetFigData(name_list, method, test_time_message, test_timeout_message):
    sum_time = 0.0
    sum_time_list = []
    solved_number = 0
    solved_number_list = []
    for name in name_list:
        temp_time = test_time_message[name][method]
        is_timeout = test_timeout_message[name][method]
        if is_timeout:
            sum_time += temp_time
            sum_time_list.append(sum_time)
            solved_number_list.append(solved_number)
        else:
            sum_time += temp_time
            sum_time_list.append(sum_time)
            solved_number += 1
            solved_number_list.append(solved_number)
    return sum_time_list, solved_number_list


if __name__ == '__main__':
    time_predict_path = utils.time_predict_path
    time_predict_path_0 = time_predict_path + "time_predict_0.json"
    time_predict_path_1 = time_predict_path + "time_predict_1.json"
    time_predict_path_2 = time_predict_path + "time_predict_2.json"
    time_predict_0 = utils.ReadJson(time_predict_path_0)
    time_predict_1 = utils.ReadJson(time_predict_path_1)
    time_predict_2 = utils.ReadJson(time_predict_path_2)
    time_predict_list = [time_predict_0, time_predict_1, time_predict_2]
    time_predict_label_list = utils.encoding_layer_list

    time_basic_data_path = utils.time_basic_data_path
    test_name_list_path = time_basic_data_path + "test_name_list.json"
    test_time_message_path = time_basic_data_path + "test_time_message.json"
    test_timeout_message_path = time_basic_data_path + "test_timeout_message.json"
    test_name_list = utils.ReadJson(test_name_list_path)
    test_time_message = utils.ReadJson(test_time_message_path)
    test_timeout_message = utils.ReadJson(test_timeout_message_path)

    

    for method in utils.method_list:
        save_path = utils.time_result_path + method + "_time_predict.pdf"
        plt.figure()
        plt.title(method)
        plt.xlabel('Sum Time (s)')
        plt.ylabel('Solved Number')

        test_time_list = []
        for name in test_name_list:
            test_time_list.append(test_time_message[name][method])
        ground_truth_name_list = Sort(test_name_list, test_time_list)        
        ground_truth_sum_time_list, ground_truth_solved_number_list = GetFigData(ground_truth_name_list, method, test_time_message, test_timeout_message)
        plt.plot(ground_truth_sum_time_list, ground_truth_solved_number_list, label="Ground Truth", color="#C0C0C0", linestyle=':')

        for i in range(len(time_predict_label_list)):
            label = time_predict_label_list[i]
            time_predict = time_predict_list[i]
            predict_time_list = time_predict[method]
            predict_name_list = Sort(test_name_list, predict_time_list)
            predict_solved_sum_time_list, predict_solved_number_list = GetFigData(predict_name_list, method, test_time_message, test_timeout_message)
            if label == "0-depth Encoding":
                color = "#FEB64D"
            elif label == "1-depth Encoding":
                color = "#FA816D"
            elif label == "2-depth Encoding":
                color = "#D15B7F"
            plt.plot(predict_solved_sum_time_list, predict_solved_number_list, label=label, color=color)
            
        random_index_list = list(range(len(test_name_list)))
        random.shuffle(random_index_list)
        random_name_list = []
        for index in random_index_list:
            random_name_list.append(test_name_list[index])
        random_sum_time_list, random_solved_number_list = GetFigData(random_name_list, method, test_time_message, test_timeout_message)
        plt.plot(random_sum_time_list, random_solved_number_list, label="random", color="#C0C0C0", linestyle="--")
        plt.legend()
        plt.savefig(save_path)
        plt.show()
        
        