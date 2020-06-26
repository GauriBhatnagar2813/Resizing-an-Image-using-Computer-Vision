# import the necessary packages
import imutils
import cv2

# load the input image and show its dimensions, keeping in mind that
# images are represented as a multi-dimensional NumPy array with
# shape no. rows (height) x no. columns (width) x no. channels (depth)

image = cv2.imread('/home/gauri/Desktop/sample.jpeg',0)


cv2.imshow("Image", image)

(h, w) = image.shape
print("width={}, height={}".format(w, h))

# fixed resizing and distort aspect ratio so let's resize the width
# to be 300px but compute the new height based on the aspect ratio
r = 300.0 / w
dim = (300, int(h * r))
resized = cv2.resize(image, dim)
cv2.imshow("Aspect Ratio Resize", resized)
cv2.waitKey(0)

# display the image to our screen -- we will need to click the window
# open by OpenCV and press a key on our keyboard to continue execution

