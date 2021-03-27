 # Importing all necessary libraries 
import cv2 
import os 
  
# Read the video from specified path
#cam = cv2.VideoCapture("result/demo3--Labeled.mp4") 
cam = cv2.VideoCapture("lab3.mp4") 
  
try: 
      
    # creating a folder named data 
    if not os.path.exists('data'): 
        os.makedirs('data') 
  
# if not created then raise error 
except OSError: 
    print ('Error: Creating directory of data') 
  
# frame 
currentframe = 0
count = 0  
while(True): 
      
    # reading from frame 
    ret,frame = cam.read() 
    print(ret)
    if ret:
        
        # if video is still left continue creating images 
        name = './data/thesis_2_' + str('label_2') + str(currentframe) + '.jpg'
        print ('Creating...' + name) 
        count += 1
        # writing the extracted images 
        if (count == 20):
           cv2.imwrite(name, frame)
           count = 0 
  
        # increasing counter so that it will 
        # show how many frames are created 
        currentframe += 1
    else: 
        break
  
# Release all space and windows once done 
cam.release() 
cv2.destroyAllWindows() 