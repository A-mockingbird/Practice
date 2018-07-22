import os.path
import glob

if __name__ == "__main__":
    realpath = os.path.realpath(__file__)
    dirname = os.path.dirname(realpath)
    extension = 'JPG'
    file_list = glob.glob('*.'+extension)
    for filename in file_list:
        lowerfilename = filename.lower()
        filepath = os.path.join(dirname, filename)
        os.rename(filepath, lowerfilename)
        print(lowerfilename)