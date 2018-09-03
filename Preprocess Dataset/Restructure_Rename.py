
"""
 AUTHOR : Xiaolu Zhang
 PURPOSE : Dataset preprocess
"""

import os
import argparse

parser = argparse.ArgumentParser(description='Input dir path.')
parser.add_argument('path', help='Input dir path')
args = parser.parse_args()

for dir in os.listdir(args.path):
    try:
        count = 1000
        for file in os.listdir(args.path+'/'+dir):
            count = count + 1
            if ".jpg" or ".JPG" in file:
                os.rename(args.path+dir+"/"+file, args.path+dir.capitalize()+"_"+str(count)+".jpg")
            elif ".png" or ".PNG" in file:
                os.rename(args.path+dir+"/"+file, args.path+dir.capitalize()+"_"+str(count)+".png")
            elif ".gif" or ".GIF" in file:
                os.rename(args.path+dir+"/"+file, args.path+dir.capitalize()+"_"+str(count)+".gif")
            elif ".jpeg" or ".JPEG" in file:
                os.rename(args.path+dir+"/"+file, args.path+dir.capitalize()+"_"+str(count)+".jpeg")
    except:
        print('error')
