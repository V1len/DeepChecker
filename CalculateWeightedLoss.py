import utils
import csv

if __name__ == '__main__':
    classify_basic_data_path = utils.classify_basic_data_path
    predict_data_path = classify_basic_data_path + "classify_predict_data.csv"

    with open(predict_data_path, newline='') as csvfile:
        data = list(csv.reader(csvfile))
    data = data[1:]
    test_num = len(data)
    method_list = utils.method_list
    DeepChecker_list = utils.DeepChecker_list
    for DeepChecker in DeepChecker_list:
        print(DeepChecker)
        sum_weighted_loss = 0.0
        for line in data:
            predict_time = line[len(method_list) + DeepChecker_list.index(DeepChecker) + 1]
            truth_time = line[len(method_list) + len(DeepChecker_list) + 1]
            if predict_time == "failed" or predict_time == "timeout" or predict_time == "0.0":
                sum_weighted_loss += (3600.0 - float(truth_time))
            else:
                sum_weighted_loss += (float(predict_time)- float(truth_time))
        print(sum_weighted_loss / test_num)
    

                
