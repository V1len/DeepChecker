import matplotlib.pyplot as plt
import csv
import utils
import copy

if __name__ == '__main__':
    root_path = utils.root_path
    method_list = []
    method_list.append("2-depth Encoding")
    method_list.append("1-depth Encoding")
    method_list.append("0-depth Encoding")
    method_list.append("ABC-pdr")
    method_list.append("IImc")
    method_list.append("ABC-dprove")
    method_list.append("IC3ref")
    method_list.append("Ground Truth")
    method_list.append("Random")
    index_list = [7, 6, 5, 2, 3, 1, 4, 8, 9]

    classify_basic_data_path = utils.classify_basic_data_path
    predict_data_path = classify_basic_data_path + "classify_predict_data.csv"
    save_path = utils.classify_result_path + "classify.pdf"

    maxtime = 3600
    with open(predict_data_path, newline='') as csvfile:
        data = list(csv.reader(csvfile))

    xaxis = list(range(1, maxtime + 1))
    data = data[1:]
    # plt.subplot(1,2,1)
    plt.figure()
    for method in method_list:
        solved_num_list = [0] * maxtime
        for line in data:
            pointer = index_list[method_list.index(method)]
            if line[pointer] != "timeout" and line[pointer] != "failed" and line[pointer] != "0.0" and line[pointer] != "0":
                lowerbound = int(float(line[pointer]) + 1)
                for index in range(len(solved_num_list)):
                    if index >= lowerbound:
                        solved_num_list[index] += 1
        if method in utils.method_list:
            method = utils.NameMap(method)
        if method == "0-depth Encoding":
            color = "#FEB64D"
        elif method == "1-depth Encoding":
            color = "#FA816D"
        elif method == "2-depth Encoding":
            color = "#D15B7F"
        elif method == "ABC-pdr":
            # color = "#60ACFC"
            color = "#6495ED"
        elif method == "ABC-dprove":
            color = "#23C2DB"
        elif method == "IImc":
            # color = "#3DB272"
            color = "#2E8B57"
        elif method == "IC3ref":
            color = "#63D5B2"
        elif method == "Ground Truth":
            color = "#C0C0C0"
        elif method == "Random":
            color = "#A9A9A9"
        else:
            color = None
        
        if method == "Ground Truth":
            linestyle = ':'
        elif method == "ABC-pdr" or method == "ABC-dprove" or method == "IImc" or method == "IC3ref":
            linestyle = "--"
        else:
            linestyle = None
        plt.plot(xaxis, solved_num_list, label=method, color=color, linestyle=linestyle)

    # maxtime = 10
    # with open(predict_data_path, newline='') as csvfile:
    #     data = list(csv.reader(csvfile))

    # xaxis = list(range(1, maxtime + 1))
    # data = data[1:]
    # plt.subplot(1,2,2)
    # for method in method_list:
    #     solved_num_list = [0] * maxtime
    #     for line in data:
    #         pointer = method_list.index(method) + 1
    #         if line[pointer] != "timeout" and line[pointer] != "failed" and line[pointer] != "0.0":
    #             lowerbound = int(float(line[pointer]) + 1)
    #             for index in range(len(solved_num_list)):
    #                 if index >= lowerbound:
    #                     solved_num_list[index] += 1
    #     plt.plot(xaxis, solved_num_list, label=method)
    plt.xlabel('Time (s)')
    plt.ylabel('# Solved Benchmarks')
    plt.legend()
    plt.savefig(save_path)
    plt.show()

    