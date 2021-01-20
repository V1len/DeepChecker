import utils
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    classify_basic_data_path = utils.classify_basic_data_path

    embedded_dir_0 = utils.embedded_dir_0
    embedded_dir_1 = utils.embedded_dir_1
    embedded_dir_2 = utils.embedded_dir_2

    statistic_name_dic_path = classify_basic_data_path + "statistic_name_dic.json"
    statistic_name_dic = utils.ReadJson(statistic_name_dic_path)

    statistic_sample_distribution_path = utils.statistic_sample_distribution_path

    for i in range(len(utils.encoding_layer_list)):
        dir = [embedded_dir_0, embedded_dir_1, embedded_dir_2][i]
        for method in utils.method_list:
            temp_path = statistic_sample_distribution_path + method + "_distribution_" + str(i) + ".pdf"
            plt.figure()
            index = utils.method_list.index(method)
            name_list = statistic_name_dic[method]
            vec_list = utils.GetVecList(dir, name_list)
            statistic_vec = np.log(np.array(vec_list).sum(axis=0) + 1.0).tolist()
            # print(statistic_vec)
            # plt.subplot(2,2,index + 1)
            plt.bar(range(len(statistic_vec)),statistic_vec)
            plt.title(method)
            plt.xlabel('Features')
            plt.ylabel('ln(# Total)')
            plt.savefig(temp_path)
            plt.show()


