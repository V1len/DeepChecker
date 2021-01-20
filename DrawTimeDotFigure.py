import csv
import utils
import sys
import random
import numpy as np
import matplotlib.pyplot as plt

def ChangeData(data):
    if data != "timeout" and data != "failed" and data != "0.0" and data != "0":
        changed_data = float(data)
    else:
        changed_data = 3600.00
    return changed_data

if __name__ == '__main__':
    classify_basic_data_path = utils.classify_basic_data_path
    predict_data_path = classify_basic_data_path + "classify_predict_data.csv"
    save_path = utils.classify_result_path + "classify.pdf"

    with open(predict_data_path, newline='') as csvfile:
        data = list(csv.reader(csvfile))

    data = data[1:]
    
    truth_data_list = []
    random_data_list = []
    predict_data_list_0 = []
    predict_data_list_1 = []
    predict_data_list_2 = []
    for line in data:
        truth_data_list.append(ChangeData(line[len(utils.method_list) + len(utils.encoding_layer_list) + 1]))
        random_data_list.append(ChangeData(line[len(utils.method_list) + len(utils.encoding_layer_list) + 2]))
        predict_data_list_0.append(ChangeData(line[len(utils.method_list) + 1]))
        predict_data_list_1.append(ChangeData(line[len(utils.method_list) + 2]))
        predict_data_list_2.append(ChangeData(line[len(utils.method_list) + 3]))


    all_data_list = [random_data_list, predict_data_list_0, predict_data_list_1, predict_data_list_2]
    figure_label_list = ["Random", "0-depth Encoding", "1-depth Encoding", "2-depth Encoding"]
    for i in range(len(all_data_list)):
        temp_data_list = all_data_list[i]
        label = figure_label_list[i]
        save_path = utils.classify_result_path + figure_label_list[i] + ".pdf"
        for layer in utils.encoding_layer_list:
            # x=[1000,2000,3000]
            # y=[1000,2000,3000]
            fig, ax = plt.subplots()
            ax.scatter(temp_data_list, truth_data_list)

            # for i in range(len(data)):
            #     ax.scatter(temp_data_list[i], truth_data_list[i])
            # ax.set_tilte(label)
            ax.set_xlabel('Predict Time (s)')
            ax.set_ylabel('Truth Time (s)')
            ax.set_xlim(0, 500)
            ax.set_ylim(0, 500)
            # ax.set_xscale('log')
            # ax.set_yscale('log')
            # ax.xaxis.set_major_locator(ticker.LogLocator(base=100.0, numticks=5))
            # ax.yaxis.set_major_locator(ticker.LogLocator(base=100.0, numticks=5))
            
            # fig = plt.gcf()
            plt.title(label)
            plt.savefig(save_path)


        # for layer in utils.encoding_layer_list:
        #     xticks = [0.01, 0.1, 1, 10, 100, 1000, 3600]
        #     xtickslabel = [0.01, 0.1, 1, 10, 100, 1000, 3600]
        #     yticks = [0.01, 0.1, 1, 10, 100, 1000, 3600]
        #     ytickslabel = [0.01, 0.1, 1, 10, 100, 1000, 3600]
            
        #     plt.figure()
        #     plt.xticks(xticks, xtickslabel)
        #     plt.yticks(yticks, ytickslabel)
        #     plt.xlabel('Predict Time (s)')
        #     plt.ylabel('Truth Time (s)')
        #     for j in range(len(data)):
        #         plt.scatter(temp_data_list[j], truth_data_list[j])
        #     plt.scatter(temp_data_list, truth_data_list)
        #     plt.savefig(save_path)
        #     plt.show()