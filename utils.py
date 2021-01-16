import json
import pickle
import os

<<<<<<< HEAD
use_all_methods = True
=======
use_all_methods = False
>>>>>>> 6d584c5a3dced798dab67ab69c8c123d0a71adae
if use_all_methods:
    method_list = ["dprove", "pdr", "iimc", "IC3"]
else:
    method_list = ["iimcbw", "iimcfw", "iimcic3", "iimcic3lr"]

DeepChecker_list = ["DeepChecker0", "DeepChecker1", "DeepChecker2"]

choose_top_method_number = 1
sum_method_number = len(method_list)

<<<<<<< HEAD
date = "2021-1-16-Test"
=======
date = "2021-1-15"
>>>>>>> 6d584c5a3dced798dab67ab69c8c123d0a71adae
root_path = "/mnt/hd0/DeepChecker/DataForNet/" + date + "/"
if use_all_methods:
    basic_path = root_path + "tools/"
else:
    basic_path = root_path + "iimc/"

if not os.path.exists(root_path):
    os.mkdir(root_path)
if not os.path.exists(basic_path):
    os.mkdir(basic_path)
classify_model_path = basic_path + "classify_model/"
classify_predict_path = basic_path + "classify_predict/"
time_model_path = basic_path + "time_model/"
time_predict_path = basic_path + "time_predict/"
importance_message_path = basic_path + "importance_message/"
importance_fig_path = basic_path + "importance_figure/"
statistic_sample_distribution_path = basic_path + "statistic_sample_distribution/"
basic_data_path = basic_path + "basic_data/"
path_list = [classify_model_path, classify_predict_path, time_model_path, time_predict_path, 
    importance_message_path, importance_fig_path, statistic_sample_distribution_path, basic_data_path]
for temp_path in path_list:
    if not os.path.exists(temp_path):
        os.mkdir(temp_path)

# AVY_dprove_path = "/mnt/hd0/DeepChecker/dataset/2021-1-6/AVY_dprove_clean.json"
# AVY_dprove_path = "/mnt/hd0/DeepChecker/DataForNet/2021-1-10/data_clean.json"
AVY_dprove_path = "/mnt/hd0/DeepChecker/dataset/2020-1-12/AVY_dprove_clean.json"
pdr_IC3_path = "/mnt/hd0/DeepChecker/dataset/2020-1-12/pdr_IC3_clean.json"
others_path = "/mnt/hd0/DeepChecker/dataset/2020-1-12/others.json"

iimc_path = "/mnt/hd0/DeepChecker/dataset/2021-1-8/iimc_benchmark.json"
new_format_json_path = "/mnt/hd0/DeepChecker/new_format.json"

embedding_date_0 = "2021-1-2_v0.1"
embedding_date_1 = "2020-12-24_v1.1"
embedding_date_2 = "2021-1-2_v2.2"
# embedding_date_0 = "2020-12-11_v0"
# embedding_date_1 = "2020-12-24_v1.1"
# embedding_date_2 = "2020-12-24_v2.1"

embedded_dir_0 = "/mnt/hd0/DeepChecker/embedding/embedded/" + embedding_date_0
embedded_dir_1 = "/mnt/hd0/DeepChecker/embedding/embedded/" + embedding_date_1
embedded_dir_2 = "/mnt/hd0/DeepChecker/embedding/embedded/" + embedding_date_2


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

def GetVec(dir, name):
    aig_name = name + ".vector"
    aig_path = os.path.join(dir, aig_name)
    assert(os.path.isfile(aig_path))
    vector = []
    with open(aig_path, encoding='utf-8') as fp:
        line = fp.readlines()[0].split("[")[1].split("]")[0]
        items = line.split(", ")
        for item in items:
            vector.append(int(item))
        fp.close()
    return vector

def GetVecList(dir, name_list):
    vec_list = []
    for name in name_list:
        vector = GetVec(dir, name)
        vec_list.append(vector)
    return vec_list 
