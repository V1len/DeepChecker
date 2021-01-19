import utils
import numpy as np
import Classify

if __name__ == '__main__':
    model_path = utils.classify_model_path + "model_2.pkl"
    embedded_dir_2 = utils.embedded_dir_2
    test_name_list_path = utils.classify_basic_data_path + "test_name_list.json"
    test_label_dic_path = utils.classify_basic_data_path + "test_label_dic.json"
    test_name_list = utils.ReadJson(test_name_list_path)
    test_label_dic = utils.ReadJson(test_label_dic_path)
    test_vec_list = utils.GetVecList(embedded_dir_2, test_name_list)

    model = utils.Load_pkl(model_path)
    predictions = model.predict_proba(test_vec_list)
    predict_label_list = np.argsort(-predictions, axis=1)
    test_label_list = Classify.GetLabelList(test_name_list, test_label_dic)
    sum_acc = Classify.GetAcc(predict_label_list, test_label_list)
    print(sum_acc)
