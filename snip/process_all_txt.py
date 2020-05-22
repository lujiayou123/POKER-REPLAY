import os

def process_txt(file_path):
    f = open(file_path, mode='r', encoding='utf-8')
    space_counter = 0
    buffer = []
    num = 1
    id = file_path[15:-4]
    for line in f:
        if line.strip() == "":  # 判断是否是空行
            space_counter += 1  # 是的话空行+1
            # print(space_counter)
        if space_counter == 0:  # 当前不是空行
            buffer.append(line)  # 塞入Buffer

        if space_counter == 1:  # 第一个空行
            # 把buffer里面的东西写入文件,num.txt
            length = len(buffer)
            path = "./hands/pluribus_" + id + "_" + str(num) + ".txt"
            file = open(path, mode='w')
            for i in range(length):
                file.write(buffer[i])
        if space_counter == 2:  # 第二个空行
            buffer = []  # 重置Buffer
            space_counter = 0  # 重置space_counter
            num += 1  # 开启下一个

if __name__ == '__main__':
    path = "../out"
    for i,j,k in os.walk(path):
        txts = k
    num_txt = len(txts)
    for i in range(num_txt):
        file_path = "./out/"+txts[i]
        # print(file_path)
        process_txt(file_path)
    # for id in range(30,119):
    #     file_path = "./out/pluribus_30.txt"
    #     process_txt(file_path)
