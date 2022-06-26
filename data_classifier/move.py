from pathlib import Path
import shutil
import os
#Label 파일의 첫 번째 줄은 비어있어야 합니다.
total_label=[]
with open("label.txt", "r") as f:
    for line in f:
        total_label.append(line.strip())

print(total_label)

file_source ='./'
file_destination_abnormal ='./abnormal'
file_destination_normal ='./normal'
def move(file,file_destination):
    shutil.move(os.path.join(file_source,file),file_destination)

# label can be changed so it need to be passed by param
def isNormalOrNot(filename,label):
    if label[int(filename[0:1])] == "0":
        return True
    elif label[int(filename[0:1])] == "1":
        return False
def __main__():
    for file in Path(file_source).glob('./*.jpg'):
        print(file)
        if isNormalOrNot(str(file),total_label):
            move(file,file_destination_normal)
        else:
            move(file,file_destination_abnormal)
__main__()