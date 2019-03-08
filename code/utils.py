#coding=utf-8
import numpy as np
import csv

def remove_zero(x, y):
    """ 获取去除缺失值之后的数据 """
    nozero = np.nonzero(y) # 返回y中非零元素的索引值数组
    y = y[nozero]
    x = np.array(x)
    x = x[nozero]
    return x, y
    
def get_data_from_csv(filename):
    """ 从csv文件中读取数据，并返回字符串数组 """
    data = []
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        count = 0
        for line in reader:
            try:
                data.append(line[0])
                count += 1
            except:
                print('error: ', line, count)
                data.append(' ')
        print('共读取了: {}行'.format(count))
    return data