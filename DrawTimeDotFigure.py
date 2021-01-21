import csv
import utils
import sys
import random
import numpy as np
import matplotlib.pyplot as plt
import copy

def ChangeData(data):
    if data != "timeout" and data != "failed" and data != "0.0" and data != "0":
        changed_data = float(data)
    else:
        changed_data = 3600.00
    return changed_data

if __name__ == '__main__':
    time_basic_data_path = utils.time_basic_data_path

    time_predict_label_list = ["0-depth Encoding", "1-depth Encoding", "2-depth Encoding"]
    for i in range(len(time_predict_label_list)):
        save_path = utils.time_result_path + time_predict_label_list[i] + "_sort.pdf"
        plt.figure()
        plt.title(time_predict_label_list[i])
        fig, ax = plt.subplots(2, 3)
        for method in utils.method_list:
            predict_name_sort = utils.ReadJson(time_basic_data_path + method + "_name_sort_" + str(i) + ".json")
            truth_name_sort = utils.ReadJson(time_basic_data_path + method + "_name_sort_truth.json")
            yaxis = list(range(len(truth_name_sort)))
            xaxis = []
            for name in predict_name_sort:
                xaxis.append(truth_name_sort.index(name))
            arg = 230 + utils.method_list.index(method) + 1
            temp_ax = fig.add_subplot(arg)
            temp_ax.scatter(xaxis, yaxis, s=2)
            temp_ax.set_xscale('linear')
            temp_ax.set_yscale('linear')
            temp_ax.set_title(method)
        yaxis = list(range(len(truth_name_sort)))
        xaxis = copy.deepcopy(yaxis)
        random.shuffle(xaxis)
        arg = 235
        temp_ax = fig.add_subplot(arg)
        temp_ax.scatter(xaxis, yaxis, s=2)
        temp_ax.set_xscale('linear')
        temp_ax.set_yscale('linear')
        temp_ax.set_title("random")
        
        plt.savefig(save_path)


    predict_data_path = time_basic_data_path + "time_predict_data.csv"

    with open(predict_data_path, newline='') as csvfile:
        data = list(csv.reader(csvfile))

    data = data[1:]        
    truth_dprove_data_list = []
    truth_pdr_data_list = []
    truth_iimc_data_list = []
    truth_IC3_data_list = []
    for line in data:
        truth_dprove_data_list.append(ChangeData(line[1]))
        truth_pdr_data_list.append(ChangeData(line[2]))
        truth_iimc_data_list.append(ChangeData(line[3]))
        truth_IC3_data_list.append(ChangeData(line[4]))

    figure_label_list = ["0-depth Encoding", "1-depth Encoding", "2-depth Encoding"]
    for i in range(len(figure_label_list)):
        label = figure_label_list[i]
        dprove_data_list = []
        pdr_data_list = []
        iimc_data_list = []
        IC3_data_list = []
        for line in data:
            dprove_data_list.append(ChangeData(line[4 * i + 5]))
            pdr_data_list.append(ChangeData(line[4 * i + 6]))
            iimc_data_list.append(ChangeData(line[4 * i + 7]))
            IC3_data_list.append(ChangeData(line[4 * i + 8]))
            
        save_path = utils.time_result_path + label + ".pdf"
        fig, ax = plt.subplots(2, 2)
        ax[0][0].set_title(utils.NameMap("dprove"))
        ax[0][0].scatter(dprove_data_list, truth_dprove_data_list, s=2)
        # ax[0][0].set_xlabel('Predict Time (s)')
        # ax[0][0].set_ylabel('Truth Time (s)')
        ax[0][0].set_xscale('log')
        ax[0][0].set_yscale('log')

        ax[0][1].set_title(utils.NameMap("pdr"))
        ax[0][1].scatter(pdr_data_list, truth_pdr_data_list, s=2)
        ax[0][1].set_xscale('log')
        ax[0][1].set_yscale('log')

        ax[1][0].set_title(utils.NameMap("iimc"))
        ax[1][0].scatter(iimc_data_list, truth_iimc_data_list, s=2)
        ax[1][0].set_xscale('log')
        ax[1][0].set_yscale('log')

        ax[1][1].set_title(utils.NameMap("IC3"))
        ax[1][1].scatter(IC3_data_list, truth_IC3_data_list, s=2)
        ax[1][1].set_xscale('log')
        ax[1][1].set_yscale('log')

        plt.savefig(save_path)