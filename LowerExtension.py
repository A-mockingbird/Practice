import os.path
import glob
import re

if __name__ == "__main__":
    realpath = os.path.realpath(__file__)
    dirname = os.path.dirname(realpath)
    extension = 'JPG'
    file_list = glob.glob('*.'+extension)
    for filename in file_list:
        #lowerfilename = filename.lower()
        filepath = os.path.join(dirname, filename)
        if re.search(r'\.JPG', filename) != None:
            filename = str.replace(filename, '.JPG', '.jpg')
            #filename=re.sub(r'\.JPG', '.jpg', filename)
            print(filename)
            os.rename(filepath, filename)
