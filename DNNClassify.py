import utils
import DNNStructure

  


if __name__ == '__main__':
    use_all_methods = utils.use_all_methods

    embedded_dir_0 = utils.embedded_dir_0
    embedded_dir_1 = utils.embedded_dir_1
    embedded_dir_2 = utils.embedded_dir_2

    classify_basic_data_path = utils.classify_basic_data_path
    train_name_list_path = classify_basic_data_path + "train_name_list.json"
    train_label_dic_path = classify_basic_data_path + "train_label_dic.json"
    test_name_list_path = classify_basic_data_path + "test_name_list.json"
    test_label_dic_path = classify_basic_data_path + "test_label_dic.json"

    train_name_list = utils.ReadJson(train_name_list_path)
    train_label_dic = utils.ReadJson(train_label_dic_path)
    test_name_list = utils.ReadJson(test_name_list_path)
    test_label_dic = utils.ReadJson(test_label_dic_path)

    train_label_list = utils.GetLabelList(train_name_list, train_label_dic)
    test_label_list = utils.GetLabelList(test_name_list, test_label_dic)

    classify_predict_path = utils.classify_predict_path
    classify_predict_path_0 = classify_predict_path + "DNN_predict_0.json"
    classify_predict_path_1 = classify_predict_path + "DNN_predict_1.json"
    classify_predict_path_2 = classify_predict_path + "DNN_predict_2.json"

    classify_model_path = utils.classify_model_path
    classify_model_path_0 = classify_model_path + "DNN_model_0.pkl"
    classify_model_path_1 = classify_model_path + "DNN_model_1.pkl"
    classify_model_path_2 = classify_model_path + "DNN_model_2.pkl" 