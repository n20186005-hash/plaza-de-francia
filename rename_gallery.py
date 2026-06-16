import os
import sys

gallery_dir = r"c:\Users\Administrator\Documents\GitHub\巴拿马\plaza-de-francia\public\gallery"

os.chdir(gallery_dir)
count = 0
for f in os.listdir('.'):
    if f.startswith('plaza-de-francia') and '(' in f and f.endswith('.jpg'):
        new_name = f.replace(' (', '-').replace(')', '')
        os.rename(f, new_name)
        count += 1
        print(f"Renamed: {f} -> {new_name}")

print(f"Total renamed: {count}")
