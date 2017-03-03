#Program Instruction
1. Install Python 2.7 (32-bit) from: https://www.python.org/ftp/python/2.7.13/python-2.7.13.msi
2. Make sure the following 'Path' are added to 'System variables':
   C:\Python27\
   C:\Python27\Scripts
3. Install all dependncies for pandas: setuptools, Numpy, python-dateutil, pytz.
   CMD Commands: pip install setuptools
                 pip install numpy
                 pip install python-dateutil
                 pip install pytz
4. Install pandas.
   CMD command: pip install pandas
5. Install latest ImageMagick (32-bit) from http://www.imagemagick.org/download/binaries/
6. Make sure the following 'Path' are added to 'System variables':
   C:\Program Files (x86)\ImageMagick-6.9.6-Q8
7. Install Wand (and all dependncies if necessary):
   CMD commands: pip install Wand
8. Run main.py.
9. Choose the directory where all TIFF and XML file will be stored.
10. Choose the directory of original XML files.
11. Choose the directory of original JPG files.
12. Indicate the number of specimens to process.
13. The result will be stored in temp.csv.

##Note:
1. All '|' are replaced by '!' because a filename contains '|' is illegal.
2. All '?' are replaced by '_' because a filename contains '?' is illegal.
