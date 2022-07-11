from pathlib import Path
import cv2 as cv
import os
import numpy as np
file_source ='./'
 

def __main__():
    for file in Path(file_source).glob('./*.jpg'):
        print(file)
        img = cv.imread(str(file),cv.IMREAD_COLOR)
        cv.imwrite(str(file).split(".")[0]+'_flip.jpg',img)
        
__main__()