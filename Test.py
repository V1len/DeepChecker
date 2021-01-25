import utils
import numpy as np
import Classify
import matplotlib.pyplot as plt

if __name__ == '__main__':
    # model_path = utils.classify_model_path + "model_2.pkl"
    # embedded_dir_2 = utils.embedded_dir_2
    # test_name_list_path = utils.classify_basic_data_path + "test_name_list.json"
    # test_label_dic_path = utils.classify_basic_data_path + "test_label_dic.json"
    # test_name_list = utils.ReadJson(test_name_list_path)
    # test_label_dic = utils.ReadJson(test_label_dic_path)
    # test_vec_list = utils.GetVecList(embedded_dir_2, test_name_list)

    # model = utils.Load_pkl(model_path)
    # predictions = model.predict_proba(test_vec_list)
    # predict_label_list = np.argsort(-predictions, axis=1)
    # test_label_list = Classify.GetLabelList(test_name_list, test_label_dic)
    # sum_acc = Classify.GetAcc(predict_label_list, test_label_list)
    # print(sum_acc)
    

    x = list(range(100))
 
    fig = plt.figure()
    
    ax1 = fig.add_subplot(221)
    ax1.scatter(x, x)
    

    

 


    # xaxis = list(range(1000))
    # yaxis = list(range(1000))
    # fig, ax = plt.subplots()
    # temp_ax = fig.add_subplot()
    # temp_ax.scatter(xaxis, yaxis, s=2)
    # # temp_ax.set_xscale('linear')
    # # temp_ax.set_yscale('linear')
    # temp_ax.set_title("0")
    # length_list = range(0, len(yaxis), 100)
    # temp_ax.set_xticks(length_list)
    # temp_ax.set_yticks(length_list)
    
    # plt.figure()
    # plt.scatter(xaxis, yaxis, s=2)
    # # temp_ax.set_xscale('linear')
    # # temp_ax.set_yscale('linear')
    # plt.title("0")
    # length_list = range(0, len(yaxis), 100)
    # plt.xticks([])
    # plt.yticks([])
    plt.savefig("/mnt/hd0/DeepChecker/DataForNet/2021-1-20/tools/time/result/0.pdf")
