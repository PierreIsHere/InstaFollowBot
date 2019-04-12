import cv2
import numpy as np
import pyautogui
def buttonLoc():
	t = pyautogui.screenshot('test.png')
	img_rgb = cv2.imread('test.png')
	template = cv2.imread('followZ.png')
	w, h = template.shape[:-1]

	res = cv2.matchTemplate(img_rgb, template, cv2.TM_CCOEFF_NORMED)
	threshold = .8
	loc = np.where(res >= threshold)
	temp = []
	coords = []
	for pt in zip(*loc[::-1]):
		temp.append(pt)
	if(len(temp) > 0):
		n = temp[0][0]
		# print(temp)
		for i in range (0,len(temp)):
			# print(temp[i])
			if(len(coords) == 0):
				coords.append(temp[i])
			if(coords[-1][1] == temp[i][1]):
				# print(temp[i])
				continue
			elif(((coords[-1][1] - 5) > temp[i][1]) and ((coords[-1][1] + 5 ) < temp[i][1])):
				# print(temp[i])
				continue
			else:
				coords.append(temp[i])
	return coords
print(buttonLoc())