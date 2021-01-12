import utils
import copy

def ProcessData(others_path, data_path, AVY_dprove_path=""):
    method_list = utils.method_list

    others_list = utils.ReadJson(others_path)
    others_dic = {}
    for i in range(len(others_list)):
        aig = others_list[i]
        aig_name = list(aig.keys())[0]
        run_times = aig[aig_name]
        temp_dic = {}
        for method_time_pair in run_times:
            method = list(method_time_pair.keys())[0]
            time = str(method_time_pair[method])
            temp_dic[method] = time
        others_dic[aig_name] = temp_dic
    others_name_list = list(others_dic.keys())
    print(len(others_name_list))

    AVY_dprove_name_list = []
    AVY_dprove_dic = {}
    if AVY_dprove_path != "":
        AVY_dprove_dic = utils.ReadJson(AVY_dprove_path)
        AVY_dprove_name_list = list(AVY_dprove_dic.keys())
        print(len(AVY_dprove_name_list))

    data_list = []
    if AVY_dprove_path != "":
        others_method_list = copy.deepcopy(method_list)
        others_method_list.remove("dprove")
        for name in AVY_dprove_name_list:
            if all(keyword in others_dic[name].keys() for keyword in others_method_list):
                time_list = [AVY_dprove_dic[name]["dprove"]]
                for method in others_method_list:
                    time_list.append(others_dic[name][method])
                mark = False
                for time in time_list:
                    if time != "timeout" and time != "failed":
                        mark = True
                if mark == True:
                    temp_data = [name, AVY_dprove_dic[name]["dprove"]]
                    for method in others_method_list:
                        temp_data.append(others_dic[name][method])
                    data_list.append(temp_data)
    else:
        for name in others_name_list:
            if all(keyword in others_dic[name].keys() for keyword in method_list):
                time_list = []
                for method in method_list:
                    time_list.append(others_dic[name][method])
                mark = False
                for time in time_list:
                    if time != "timeout" and time != "failed":
                        mark = True
                if mark == True:
                    temp_data = [name]
                    for method in method_list:
                        temp_data.append(others_dic[name][method])
                    data_list.append(temp_data)
    title = "filename"
    for method in method_list:
        title = title + "," + method
    with open(data_path, "w") as writer:
        writer.write(title + ",DeepChecker\n")
        for line in data_list:
            writer.write(",".join(line) + "\n")

def ProcessiimcData(iimc_path, data_path):
    method_list = utils.method_list

    iimc_dic = utils.ReadJson(iimc_path)
    iimc_name_list = list(iimc_dic.keys())
    print(len(iimc_name_list))

    data_list = []
    for name in iimc_name_list:
        if all(keyword in iimc_dic[name].keys() for keyword in method_list):
            time_list = []
            for method in method_list:
                time_list.append(iimc_dic[name][method])
            mark = False
            for time in time_list:
                if time != "timeout" and time != "failed":
                    mark = True
            if mark == True:
                temp_data = [name]
                for method in method_list:
                    temp_data.append(iimc_dic[name][method])
                data_list.append(temp_data)

    title = "filename"
    for method in method_list:
        title = title + "," + method
    with open(data_path, "w") as writer:
        writer.write(title + ",DeepChecker\n")
        for line in data_list:
            writer.write(",".join(line) + "\n")


if __name__ == '__main__':
    root_path = utils.root_path

    AVY_dprove_path = utils.AVY_dprove_path
    others_path = utils.others_path
    iimc_path = utils.iimc_path
    data_path = root_path + "data.csv"

    ProcessData(others_path, data_path, AVY_dprove_path=AVY_dprove_path)
    # ProcessData(others_path, data_path)
    # ProcessiimcData(iimc_path, data_path)