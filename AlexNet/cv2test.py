import cv2
import glob

files = sorted(glob.glob("../image/*.jpg"))
for f in files:
    if "Birman" in f:
        print(f)
print("end")

cannot_read = []
for f in files:
    img = cv2.imread(f)
    if img is None:
        print(f)
        cannot_read.append(f)

print(cannot_read)
