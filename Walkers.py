import cv2


# Create our body classifier
bodycascade=cv2.CascadeClassifier("haarcascade_fullbody.xml")

# Initiate video capture for video file
cap = cv2.VideoCapture('walking.avi')

# Loop once video is successfully loaded
while True:
    
    # Read first frame
    ret, frame = cap.read()

    #Convert Each Frame into Grayscale
    grayimage=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    bodies=bodycascade.detectMultiScale(grayimage,1.2,3)
    # Pass frame to our body classifier
    for x,y,w,h in bodies:

     cv2.rectangle(frame,(x,y),(x+w,y+h),(0,225,0),2)
    cv2.imshow("video",frame)
   
    
    # Extract bounding boxes for any bodies identified
    

    if cv2.waitKey(1) == 32: #32 is the Space Key
        break

cap.release()
cv2.destroyAllWindows()
