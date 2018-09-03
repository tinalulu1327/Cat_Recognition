
"""
 AUTHOR : Xiaolu Zhang
 PURPOSE : Dataset preprocess
"""

import os
import argparse

parser = argparse.ArgumentParser(description='Input dir path.')
parser.add_argument('path', help='Input dir path')
args = parser.parse_args()

for file in os.listdir(args.path):
    try:
        if "." in file:
            os.rename(args.path+"/"+file, args.path+"/"+file.replace(" ", "_"))
    except:
        print('error')
