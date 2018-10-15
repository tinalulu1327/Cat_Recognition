import pandas as pd
from os import listdir

import argparse

parser = argparse.ArgumentParser(description='filename')
parser.add_argument('filename', help='Input filename')
args = parser.parse_args()

# get the incorrect list of all photos and labels
df = pd.read_csv(args.filename, names=["file", "label"], delimiter=" ")
print(df.head())

# get the list of files we actually have
photos = listdir("../image")
photos = [p.strip(".jpg") for p in photos]
print(photos)

# delete any rows which aren't in photos
bad = df[~df.file.isin(photos)]
df = df[df.file.isin(photos)]
print(df)

# generate the correct list of photos
df.to_csv(args.filename, index=False, header=None, sep=" ")
