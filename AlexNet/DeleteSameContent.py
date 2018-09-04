import pandas as pd
from os import listdir

import argparse

parser = argparse.ArgumentParser(description='filename')
parser.add_argument('filename1', help='Input filename')
parser.add_argument('filename2', help='Input filename')
args = parser.parse_args()

# get the incorrect list of all photos and labels
df1 = pd.read_csv(args.filename1, names=["file", "label"], delimiter=" ")
df2 = pd.read_csv(args.filename2, names=["file", "label"], delimiter=" ")

# delete any rows which is in df2
df1 = df1[~df1.file.isin(df2.file)]
print(df1)

# generate the correct list of photos
df1.to_csv(args.filename1, index=False, header=None, sep=" ")
