import json
import pickle


method_list = ["dprove", "pdr", "iimc", "IC3"]
# method_list = ["iimcbw", "iimcfw", "iimcic3", "iimcic3lr", "iimcic3r"]

choose_top_method_number = 1
sum_method_number = len(method_list)

date = "2021-1-12"
root_path = "/mnt/hd0/DeepChecker/DataForNet/" + date + "/"

# AVY_dprove_path = "/mnt/hd0/DeepChecker/dataset/2021-1-6/AVY_dprove_clean.json"
AVY_dprove_path = "/mnt/hd0/DeepChecker/DataForNet/2021-1-10/data_clean.json"
others_path = "/mnt/hd0/DeepChecker/dataset/2021-1-6/others.json"
iimc_path = "/mnt/hd0/DeepChecker/dataset/2021-1-8/iimc_benchmark.json"
# pdr_IC3_path = "/mnt/hd0/DeepChecker/dataset/2020-1-6/AVY_dprove_clean.json"
new_format_json_path = "/mnt/hd0/DeepChecker/new_format.json"


def WriteJson(my_json, json_path):
    with open(json_path, 'w')as file_obj:
        json.dump(my_json, file_obj)
        file_obj.close()

def ReadJson(json_path):
    with open(json_path, 'r') as load_f:
        load_json = json.load(load_f)
        load_f.close()
    return load_json

def Save_pkl(obj, pkl_name):
    with open(pkl_name, 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

def Load_pkl(pkl_name):
    with open(pkl_name, 'rb') as f:
        return pickle.load(f)

def InitialDic():
    statistic_dic = {}
    for method in method_list:
        statistic_dic[method] = 0
    return statistic_dic

def Statistic(dic_list):
    statistic_dic = InitialDic()
    for dic in dic_list:
        for key in dic.keys():
            value = dic[key]
            statistic_dic[value] += 1
    return statistic_dic