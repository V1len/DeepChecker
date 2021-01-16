import utils
import matplotlib.pyplot as plt

if __name__ == '__main__':
    importance_message_path = utils.importance_message_path
    importance_path_0 = importance_message_path + "importance_0.json"
    importance_path_1 = importance_message_path + "importance_1.json"
    importance_path_2 = importance_message_path + "importance_2.json"

    importance_0 = utils.ReadJson(importance_path_0)
    importance_1 = utils.ReadJson(importance_path_1)
    importance_2 = utils.ReadJson(importance_path_2)

    importance_fig_path = utils.importance_fig_path
    importance_0_save_path = importance_fig_path + "importance_0.pdf"
    importance_1_save_path = importance_fig_path + "importance_1.pdf"
    importance_2_save_path = importance_fig_path + "importance_2.pdf"
 
    plt.figure()
    plt.bar(range(len(importance_0)), importance_0)
    plt.savefig(importance_0_save_path)
    plt.show()

    plt.figure()
    plt.bar(range(len(importance_1)), importance_1)
    plt.savefig(importance_1_save_path)
    plt.show()

    plt.figure()
    plt.bar(range(len(importance_2)), importance_2)
    plt.savefig(importance_2_save_path)
    plt.show()