import utils

if __name__ == '__main__':
    train1 = utils.ReadJson("/mnt/hd0/DeepChecker/DataForNet/2021-1-18/tools/train_1.json")
    train2 = utils.ReadJson("/mnt/hd0/DeepChecker/DataForNet/2021-1-18/tools/train_2.json")
    test1 = utils.ReadJson("/mnt/hd0/DeepChecker/DataForNet/2021-1-18/tools/test_1.json")
    test2 = utils.ReadJson("/mnt/hd0/DeepChecker/DataForNet/2021-1-18/tools/test_2.json")
    all1 = []
    for name in train1:
        all1.append(name)
    for name in test1:
        all1.append(name)
    all2 = []
    for name in train2:
        all2.append(name)
    for name in test2:
        all2.append(name)
    print(len(all1))
    print(len(all2))
    dif1 = list(set(all1) - set(all2))
    print(len(dif1))
    print(dif1)
    dif2 = list(set(all2) - set(all1))
    print(len(dif2))