import cv2

### Images ####

# IMG="D:\junction\comic1.jpg"
# image=cv2.imread(IMG)
# cv2.imshow('The Image' , image)
# cv2.waitKey(0)
# IMG="D:\junction\comic1modifed.png"
# print(cv2.imwrite(IMG,image))

###################################################q#################
video=cv2.VideoCapture(0)
while True:
    grapped,frame=  video.read()
    if(not grapped):
        break
    frame=cv2.resize(frame,(800,500))
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break
    cv2.imshow('Video',frame)
video.realease
cv2.destroyAllWindows()
###################################################q#################
# video=cv2.VideoCapture("http://192.168.1.126:4747")

