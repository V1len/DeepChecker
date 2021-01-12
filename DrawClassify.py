import matplotlib.pyplot as plt
import csv
import utils

if __name__ == '__main__':
    root_path = utils.root_path
    method_list = utils.method_list
    method_list.append("DeepChecker0")
    method_list.append("DeepChecker1")
    method_list.append("DeepChecker2")
    method_list.append("GroundTruth")

    predict_data_path = root_path + "predict_data.csv"
    save_path = root_path + "Test.png"

    maxtime = 3600
    with open(predict_data_path, newline='') as csvfile:
        data = list(csv.reader(csvfile))

    xaxis = list(range(1, maxtime + 1))
    data = data[1:]
    plt.subplot(1,2,1)
    for method in method_list:
        solved_num_list = [0] * maxtime
        for line in data:
            pointer = method_list.index(method) + 1
            if line[pointer] != "timeout" and line[pointer] != "failed" and line[pointer] != "":
                lowerbound = float(line[pointer]) + 1.0
                for index in range(len(solved_num_list)):
                    if float(index) >= lowerbound:
                        solved_num_list[index] += 1
        plt.plot(xaxis, solved_num_list, label=method)

    maxtime = 20
    with open(predict_data_path, newline='') as csvfile:
        data = list(csv.reader(csvfile))

    xaxis = list(range(1, maxtime + 1))
    data = data[1:]
    plt.subplot(1,2,2)
    for method in method_list:
        solved_num_list = [0] * maxtime
        for line in data:
            pointer = method_list.index(method) + 1
            if line[pointer] != "timeout" and line[pointer] != "failed" and line[pointer] != "":
                lowerbound = float(line[pointer]) + 1.0
                for index in range(len(solved_num_list)):
                    if float(index) >= lowerbound:
                        solved_num_list[index] += 1
        plt.plot(xaxis, solved_num_list, label=method)
    

    plt.savefig(save_path)
    plt.show()

    