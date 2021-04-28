import cv2
import numpy as np
from tkinter import *
from tkinter.filedialog import askopenfilename

tk = Tk()
tk.withdraw()
tk.update()
photo = askopenfilename()
tk.destroy()
img = cv2.imread(photo)

grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
grey = cv2.medianBlur(grey, 3)
edges = cv2.adaptiveThreshold(grey, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)

#cartoonize
color = cv2.bilateralFilter(img, 9, 250, 250)
cartoon = cv2.bitwise_and(color, color, mask = edges)

resize_original = cv2.resize(img, (600,600))
resize_cartoon = cv2.resize(cartoon, (600,600))
cv2.imshow("Original", resize_original)
cv2.imshow("Cartoon", resize_cartoon)

#save
cv2.imwrite("cartoon.jpg", cartoon)
cv2.waitKey(0)
cv2.destroyAllWindows()
