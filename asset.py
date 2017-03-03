#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Require Python 2.7
import sys
import tkFileDialog
import re
import os
import shutil
from wand.image import Image

# Prepare for file transfer and converting.
def map_files(reader):
    # Generate the target directories.
    output_dir = ""
    while output_dir == "":
        output_dir = str(tkFileDialog.askdirectory(title='Please choose the target directory.'))
    print('Generating the file directory.')
    for entry in reader.iterrows():
        if entry[1][1] == 'indet.':
            entry[1][1] = output_dir + "/indet_" + entry[1][0]
            entry[1][1] = re.sub("\\|", "!", entry[1][1])
        else:
            entry[1][1] = output_dir + "/" + entry[1][1]
            entry[1][1] = re.sub("\?", "_", entry[1][1])
        #entry[1][1] = re.sub(" \xd7( )?", "/", entry[1][1])
        if not os.path.exists(entry[1][1]):
            # The file directory has not been created.
            os.makedirs(entry[1][1])
    
    print('Retrieving directories of XML files.')
    xml_dir = ""
    while xml_dir == "":
        xml_dir = str(tkFileDialog.askdirectory(title='Please choose the directory of XML files.'))
    reader['xml_paths'] = '-'    # Initialize all xml_paths to '-'.
    for dirname, dirnames, filenames in os.walk(xml_dir):
        if len(filenames) != 0:
            # There are files under the current dirctory.
            regex=re.compile(".*(xml)")
            xml_files = [m.group(0) for l in filenames for m in [regex.search(l)] if m]
            for xml_file in xml_files:
                reader.loc[re.sub(".xml", "", xml_file)][2] = dirname + "/" + xml_file
    
    print('Retrieving directories of JPG files.')
    jpg_dir = ""
    while jpg_dir == "":
        jpg_dir = str(tkFileDialog.askdirectory(title='Please choose the directory of JPG files.'))
    reader['jpg_paths'] = '-'    # Initialize all jpg_paths to '-'.
    for dirname, dirnames, filenames in os.walk(jpg_dir):
        if len(filenames) != 0:
            # There are files under the current directory.
            regex=re.compile(".*(jpg)")
            jpg_files = [m.group(0) for l in filenames for m in [regex.search(l)] if m]
            for jpg_file in jpg_files:
                # Log the directory of the jpg file to the dataframe.
                reader.loc[re.sub(".jpg", "", jpg_file)][3] = dirname + "/" + jpg_file

def move_xml(reader, plan):
    # Generate a to-do list for transfering the xml files.
    xml_to_do = reader[(reader['xml_paths']!='Done') & (reader['xml_paths']!='-')].index
    length = int(len(xml_to_do))
    i = 0
    for entry in xml_to_do:
        i += 1
        print('Moving XML file No.' + str(i) + ' out of ' + str(length) + '.')
        # Copy the xml file from its original directory to the target dirctory.
        #shutil.copy2(reader.loc[entry][2], reader.loc[entry][1])
        # Log to the dataframe.
        reader.loc[entry][2] = 'Done'
        if i >= plan:
            break

def move_jpg(reader, plan):
    # Generate a to-do list for transfering the xml files.
    jpg_to_do = reader[(reader['jpg_paths']!='Done') & (reader['jpg_paths']!='-')].index
    length = int(len(jpg_to_do))
    i = 0
    for entry in jpg_to_do:
        i += 1
        print('Processing JPG file No.' + str(i) + ' out of ' + str(length) + '.')
        # Convert and save the jpg file to the target dirctory.
        #with Image(filename=reader.loc[entry][3]) as jpg:
        #    with jpg.convert('tiff') as converted:
        #        converted.save(filename=reader.loc[entry][1] + '\\' + entry + '.tiff')
        # Log to the dataframe.
        reader.loc[entry][3] = 'Done'
        if i >= plan:
            break

# Save the current status(dataframe) to the csv file.
def save_to_csv(reader):
    print('Saving current working log.')
    with open('temp.csv', 'w') as file:
        reader.to_csv(file)