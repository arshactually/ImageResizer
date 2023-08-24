import cv2
#configurable parameters
souce="R.jpg"
destination="New.jpg"
#percent by which the image is resized 
scale_percentage =50

src = cv2.imread(souce, cv2.IMREAD_UNCHANGED)
#cv2.imshow("Porsche 911", src)



#calculate the 50 percent o fthe original dimensions 
new_width= int(src.shape[1] * scale_percentage/100)
new_height= int(src.shape[0] * scale_percentage/100)

#dsize 
dsize = (new_width, new_height)

# resiye image 

output = cv2.resize(src, dsize)

cv2.imwrite(destination, output)
#cv2.waitKey(0)