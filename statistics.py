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
        print(item)
        if item not in val_list:
            val_list.append(item)
    return val_list


def main_list(val_list):
    pass

print(value_list(open_data()))
input()