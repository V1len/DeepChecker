import utils
import matplotlib.pyplot as plt

if __name__ == '__main__':
<<<<<<< HEAD
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
=======
    root_path = utils.root_path
    importance_message_path = root_path + "importance_message/"
    save_fig_path = utils.root_path + "importance/"

    tools_importance_path_0 = importance_message_path + "tools_importance_0.json"
    tools_importance_path_1 = importance_message_path + "tools_importance_1.json"
    tools_importance_path_2 = importance_message_path + "tools_importance_2.json"   
    iimc_importance_path_0 = importance_message_path + "iimc_importance_0.json"
    iimc_importance_path_1 = importance_message_path + "iimc_importance_1.json"
    iimc_importance_path_2 = importance_message_path + "iimc_importance_2.json"

    tools_importance_0 = utils.ReadJson(tools_importance_path_0)
    tools_importance_1 = utils.ReadJson(tools_importance_path_1)
    tools_importance_2 = utils.ReadJson(tools_importance_path_2)
    iimc_importance_0 = utils.ReadJson(iimc_importance_path_0)
    iimc_importance_1 = utils.ReadJson(iimc_importance_path_1)
    iimc_importance_2 = utils.ReadJson(iimc_importance_path_2)

    tools_importance_0_save_path = save_fig_path + "tools_importance_0.pdf"
    tools_importance_1_save_path = save_fig_path + "tools_importance_1.pdf"
    tools_importance_2_save_path = save_fig_path + "tools_importance_2.pdf"
    iimc_importance_0_save_path = save_fig_path + "iimc_importance_0.pdf"
    iimc_importance_1_save_path = save_fig_path + "iimc_importance_1.pdf"
    iimc_importance_2_save_path = save_fig_path + "iimc_importance_2.pdf"

    plt.figure()
    plt.bar(range(len(tools_importance_0)), tools_importance_0)
    plt.savefig(tools_importance_0_save_path)
    plt.show()

    plt.figure()
    plt.bar(range(len(tools_importance_1)), tools_importance_1)
    plt.savefig(tools_importance_1_save_path)
    plt.show()

    plt.figure()
    plt.bar(range(len(tools_importance_2)), tools_importance_2)
    plt.savefig(tools_importance_2_save_path)
    plt.show()

    plt.figure()
    plt.bar(range(len(iimc_importance_0)), iimc_importance_0)
    plt.savefig(iimc_importance_0_save_path)
    plt.show()

    plt.figure()
    plt.bar(range(len(iimc_importance_1)), iimc_importance_1)
    plt.savefig(iimc_importance_1_save_path)
    plt.show()

    plt.figure()
    plt.bar(range(len(iimc_importance_2)), iimc_importance_2)
    plt.savefig(iimc_importance_2_save_path)
>>>>>>> 6d584c5a3dced798dab67ab69c8c123d0a71adae
    plt.show()