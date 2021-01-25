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
    #plt.title("Importance of 0-depth Encoding")
    plt.bar(range(len(importance_0)), importance_0, width=0.3, color="k")
    #plt.xlabel('Features')
    #plt.ylabel('Importance')
    x = range(0,4,1)
    plt.xticks(x)
    plt.subplots_adjust(left=0.057, right=0.99, top=0.99, bottom=0.05)
    plt.savefig(importance_0_save_path)
    plt.show()

    plt.figure()
    #plt.title("Importance of 1-depth Encoding")
    plt.bar(range(len(importance_1)), importance_1, width=0.5, color="k")
    x = range(0,18,1)
    plt.xticks(x)
    plt.subplots_adjust(left=0.071, right=0.99, top=0.99, bottom=0.05)
    plt.savefig(importance_1_save_path)
    plt.show()

    plt.figure()
    #plt.title("Importance of 2-depth Encoding")
    plt.bar(range(len(importance_2)), importance_2, width=0.5, color="k")
    x = range(0,133,10)
    plt.xticks(x)
    plt.subplots_adjust(left=0.085, right=0.99, top=0.99, bottom=0.05)
    plt.savefig(importance_2_save_path)
    plt.show()