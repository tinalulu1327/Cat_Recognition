import pandas as pd
from os import listdir
import os
import argparse

parser = argparse.ArgumentParser(description='filename')
parser.add_argument('filename', help='Input filename')
args = parser.parse_args()

# get the incorrect list of all photos and labels
df = pd.read_csv(args.filename, names=["file", "label"], delimiter=" ")

# get the list of files we actually have
photos = listdir("../image")

name = df.iloc[:,0].values
# delete any rows which aren't in photos
for photo in photos:
    if photo.strip('.jpg') in name:
        print('in')
    else:
        ret = os.system('rm -rf '+ '../image/'+ photo)
        print(ret)
print("end")
