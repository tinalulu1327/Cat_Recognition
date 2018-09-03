
"""
 AUTHOR : Xiaolu Zhang
 PURPOSE : Dataset preprocess
"""

import os;

Subset = 0
for dirs in sorted(os.listdir(".")):
    try:
        count = 0
        for files in sorted(os.listdir(dirs)):
            if ".jpg" or ".png" or ".gif" in files:
                count = count + 1
        Subset = Subset + 1
        file = open("EachBreedNumber.txt",'a')
        file.write(str(Subset) + " Subset contains " + str(count) + " images\n")
        file.close()
    except:
        print("error")
