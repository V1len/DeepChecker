import utils
import csv

def CalculateWeightedLoss(predict_data_path):
    with open(predict_data_path, newline='') as csvfile:
        data = list(csv.reader(csvfile))
    data = data[1:]
    test_num = len(data)
    method_list = utils.method_list
    encoding_layer_list = utils.encoding_layer_list
    for layer in encoding_layer_list:
        sum_weighted_loss = 0.0
        for line in data:
            predict_time = line[len(method_list) + encoding_layer_list.index(layer) + 1]
            truth_time = line[len(method_list) + len(encoding_layer_list) + 1]
            if predict_time == "failed" or predict_time == "timeout" or predict_time == "0.0":
                sum_weighted_loss += (3600.0 - float(truth_time))
            else:
                sum_weighted_loss += (float(predict_time)- float(truth_time))
        print(sum_weighted_loss / test_num)


if __name__ == '__main__':
    classify_basic_data_path = utils.classify_basic_data_path
    predict_data_path = classify_basic_data_path + "classify_predict_data.csv"
    train_predict_data_path = classify_basic_data_path + "classify_train_predict_data.csv"

    print("train")
    CalculateWeightedLoss(train_predict_data_path)
    print("test")
    CalculateWeightedLoss(predict_data_path)
    



    

                
