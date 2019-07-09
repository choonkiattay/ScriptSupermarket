import os
import glob
import shutil


source_dir = "/home/asdruin-ione/Desktop/sample_img/"
dest_dir = "/home/asdruin-ione/Desktop/sample_img_dest/"

_ext_xml = ".xml"
_ext_img = ".jpg"

# change to the source directory
os.chdir(source_dir)

# sort the file alphabetically
list_dir = os.listdir()
list_dir = [file for file in list_dir]
list_dir= sorted(list_dir)

for i,elem in enumerate(list_dir):
  count = i/6;
  
  if (count.is_integer()):
    if not os.path.exists(dest_dir+"/batch_"+str(int(count))):
      # make new directory at the destination folder
      os.mkdir(dest_dir+"/batch_"+str(int(count)))
      flag = int(count)
      pct = count/(len(list_dir)/6)
      print(str(round(pct, 2)) + "% completed...")
  
  shutil.move(os.path.join(source_dir, os.path.basename(elem)), os.path.join(dest_dir+"/batch_"+str(flag), os.path.basename(elem)))
  count += 1

print("100% completed.")
