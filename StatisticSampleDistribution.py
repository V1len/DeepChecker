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

    statistic_sample_distribution_path_0 = statistic_sample_distribution_path + "statistic_sample_distribution_0.pdf"
    statistic_sample_distribution_path_1 = statistic_sample_distribution_path + "statistic_sample_distribution_1.pdf"
    statistic_sample_distribution_path_2 = statistic_sample_distribution_path + "statistic_sample_distribution_2.pdf"


    save_list = [statistic_sample_distribution_path_0, statistic_sample_distribution_path_1, statistic_sample_distribution_path_2]
    for i in range(3):
        dir = [embedded_dir_0, embedded_dir_1, embedded_dir_2][i]
        plt.figure()
        for method in utils.method_list:
            index = utils.method_list.index(method)
            name_list = statistic_name_dic[method]
            vec_list = utils.GetVecList(dir, name_list)
            statistic_vec = np.log(np.array(vec_list).sum(axis=0) + 1.0).tolist()
            # print(statistic_vec)
            plt.subplot(2,2,index + 1)
            plt.bar(range(len(statistic_vec)),statistic_vec)
            plt.title(method)
        plt.savefig(save_list[i])
        plt.show()


