import cv,cv2

# image = cv2.imread('elnazer.jpg')
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(image,'opencv with python',(80,100), font, 1, (255,255,255), 2, cv2.LINE_AA)
cv2.namedWindow('elnazer', cv2.WINDOW_NORMAL)
cv2.imshow('elnazer', image)
cv2.waitKey()
