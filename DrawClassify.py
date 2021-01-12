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
    # method_list.append("RandomPick2")

    predict_data_path = root_path + "predict_data.csv"
    save_path = root_path + "4.png"

    maxtime = 3600

    with open(predict_data_path, newline='') as csvfile:
        data = list(csv.reader(csvfile))

    xaxis = list(range(1, maxtime + 1))
    data = data[1:]

    for method in method_list:
        solved_num_list = [0] * maxtime
        for line in data:
            pointer = method_list.index(method) + 1
            if line[pointer] != "timeout" and line[pointer] != "failed" and line[pointer] != "":
                lowerbound = int(float(line[pointer]))+1
                for index in range(len(solved_num_list)):
                    if index >= lowerbound:
                        solved_num_list[index] += 1
        plt.plot(xaxis, solved_num_list, label=method)


    plt.legend()
    plt.savefig(save_path)
    plt.show()