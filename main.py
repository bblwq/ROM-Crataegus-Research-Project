#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Require Python 2.7
import asset as a
import os
import pandas

def __main__():
    print('Program Start.')
    if not os.path.exists('temp.csv'):
        # Initialize the program if no log file is found.
        with open('Index Table.csv', 'r') as file:
            reader = pandas.read_csv(file, index_col=0)
        a.map_files(reader)
    else:
        # Retrieve the log file.
        with open('temp.csv', 'r') as file:
            reader = pandas.read_csv(file, index_col=0)
    to_do = len(reader[((reader['jpg_paths']!='Done') & (reader['jpg_paths']!='-')) | ((reader['xml_paths']!='Done') & (reader['xml_paths']!='-'))].index)
    plan = int(input('How many specimens do you want to process today out of ' + str(to_do) + ': '))
    a.move_xml(reader, plan)
    a.move_jpg(reader, plan)
    a.save_to_csv(reader)
    print('Program Complete.')

if __name__ == '__main__':
    __main__()