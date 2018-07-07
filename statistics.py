# -*- coding: utf-8 -*-

def open_data():
    data_list = []
    with open('data.txt') as data:
        for line in data:
            data_list.append(line.split(','))
    return data_list[1::]


def value_list(data_list):
    val_list = []
    for line in data_list:
        item = line[0].split('x')[0] + ' ' + line[-1].split(':')[0]
        if item not in val_list:
            val_list.append(item)
    return val_list


def main_list(val_list, data_list):
    sample_list = []
    val_val_list = []
    for val in val_list:
        temp_list = []
        val = val.split()
        samples_number = 0
        for line in data_list:
            if val[0] in line[0] and val[1] == line[-1][0:len(val[1])]:
                samples_number += 1
                temp_list.append(line[1])
        sample_list.append(samples_number)
        val_val_list.append(temp_list)
    return val_list, sample_list, val_val_list
                


print(main_list(value_list(open_data()), open_data()))
input()