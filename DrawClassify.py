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
    # index_list = [7, 6, 5, 2, 3, 1, 4, 11, 12]
    index_list = [16, 15, 14, 2, 3, 1, 4, 11, 12]

    classify_basic_data_path = utils.classify_basic_data_path
    predict_data_path = classify_basic_data_path + "classify_predict_data.csv"
    save_path = utils.classify_result_path + "AddEncodingTime.pdf"

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
        if method == "2-depth Encoding":
            color = "#004c6d"
        elif method == "1-depth Encoding":
            color = "#6996b3"
        elif method == "0-depth Encoding":
            color = "#9dc6e0"
        elif method == "ABC-pdr":
            color = "#D68910"
        elif method == "IImc":
            color = "#dd5756"
        elif method == "ABC-dprove":
            color = "#ab4a85"
        elif method == "IC3ref":
            color = "#58508d"
        elif method == "Ground Truth":
            color = "#C3C3C3"
        elif method == "Random":
            color = "#000000"
        else:
            color = None
        
        if method == "Ground Truth":
            linestyle = ':'
        elif method == "Random":
            linestyle = "--"
        else:
            linestyle = None
        plt.plot(xaxis, solved_num_list, label=method, color=color, linestyle=linestyle)


    plt.xlabel('Time (s)')
    plt.ylabel('# Solved Benchmarks')
    plt.legend()
    plt.subplots_adjust(left=0.09, right=0.992, top=0.99, bottom=0.09)
    plt.savefig(save_path)
    plt.show()





    

    