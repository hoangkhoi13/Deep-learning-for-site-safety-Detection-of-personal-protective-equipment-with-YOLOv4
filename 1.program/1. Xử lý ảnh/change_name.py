import glob
import os
import re
import cv2

def change_name() :
     a=0
     for file in glob.glob(r"F:\100.Lesis_final_last\sefl-labeling\2/*.jpg") :

     #print(images_list)
     #for frame in images_list:
      #cap = cv2.VideoCapture(0)
     #for file in glob.glob("data_safe_set/*"):
        #print(file)
        a +=1

        image = cv2.imread(file, 1)           
        #cv2.imshow("Face Recognizer", image)
        #image = cv2.resize(image,(416,416))
        cv2.imwrite('label/no_label_{}.jpg'.format(a),image)
    #cv2.destroyAllWindows()

change_name()
#cv2.destroyAllWindows()