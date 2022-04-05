from os import listdir
from os.path import isfile, join
import pandas as pd
import re


def get_file_names(mypath):
    csv_data = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    files = dict()
    for csv in csv_data:
        name = re.split('\.', csv)
        f_name = name[0]
        print('file name: {}'.format(f_name))
        files[f_name] = csv
    return files


def load_copy_data(files, mypath):
    frames = dict()
    for f_name, file in files.items():
        name = f_name
        f_name = pd.read_csv(mypath + file, encoding="UTF-8", low_memory=False)
        f_name_c = f_name.copy()
        frames[name] = f_name_c
    return frames


def calc_missing (df):
    missing_number = df.isnull().sum().sort_values(ascending=False)
    missing_percent = (df.isnull().sum()/df.isnull().count()).sort_values(ascending=False)
    missing_values = pd.concat([missing_number, missing_percent], axis=1, keys=['Missing_Number', 'Missing_Percent'])
    return missing_values.loc[(missing_values.iloc[:,1:2]!=0).all(1)]


if __name__ == "__main__":
    import sys
    load_data(int(sys.argv[1]))
