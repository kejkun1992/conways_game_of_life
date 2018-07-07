# -*- coding: utf-8 -*-

import glob, os
import math


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


def main_lists(val_list, data_list):
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


def median(numbers):
    numbers = sorted(map(int, numbers))
    if len(numbers) % 2 == 0:
        return int((numbers[int(len(numbers)/2-1)] + numbers[int(len(numbers)/2)]) / 2)
    return numbers[math.ceil(len(numbers)/2)-1]


def average(numbers):
    numbers = sorted(map(int, numbers))
    return sum(numbers)/len(numbers)


def std_deviation(numbers, average):
    numbers = sorted(map(int, numbers))
    return round(math.sqrt(sum([x**2 for x in numbers])/len(numbers) - average**2), 3)


def stat(lists):
    os.chdir('statistics')
    n = int(max([int(name.split('_')[-1].split('.')[0]) for name in glob.glob('*.txt')])) + 1
    # gets the last report number, adds 1
    
    with open('stat_' + str(n) + '.txt', 'w') as stat_n:
        print('value\tsamples_num\taverage\tmedian\tmin\tmax\tstd_deviation',
              file=stat_n)
        for i in range(len(lists[0])):
            print(lists[0][i] + '\t' + str(lists[1][i]) + '\t' + str(average(lists[2][i])),
                  file =stat_n, end='\t')
            print(str(median(lists[2][i])) + '\t' + str(min(map(int, lists[2][i]))),
                  file=stat_n, end='\t')
            print(str(max(map(int, lists[2][i]))) + '\t' + str(std_deviation(lists[2][i], average(lists[2][i]))),
                  file=stat_n)


stat(main_lists(value_list(open_data()), open_data()))