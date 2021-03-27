import glob
import os
import re
import cv2

def create_emtry_txt() :
     a=0
     for file in glob.glob(r"F:\100.Lesis_final_last\sefl-labeling\label/*.jpg") :

     #print(images_list)
     #for frame in images_list:
      #cap = cv2.VideoCapture(0)
     #for file in glob.glob("data_safe_set/*"):
        #print(file)
        a +=1
        f = open("label/no_label_{}.txt".format(a),"w+")
        f.close()
     #   image = cv2.imread(file, 1)           
        #cv2.imshow("Face Recognizer", image)
        #cv2.imwrite('text/image_no_label_{}.jpg'.format(a),image)
    #cv2.destroyAllWindows()

create_emtry_txt()
#cv2.destroyAllWindows()