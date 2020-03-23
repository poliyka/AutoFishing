from PIL import Image
import numpy as np
import math
import time


percent = 0
med = 0



def get_index():
	global percent
	global med
	return percent, med


def math_image_range():

	try:
        # print(img.size)
		# print(img.format)
		# print(img.mode)

		img = Image.open('test.png')
		w = img.size[0]
		h = img.size[1]
		datas = []
		# 遍歷長寬取出每個pixel的RGB三碼參數(0~255)
		for i in range(0, w):
			for j in range(0, h):
				data = (img.getpixel((i, j)))
				# 判斷黃色，色碼範圍
				if 200 < data[0] < 240 and 170 < data[1] < 220 and 58 < data[2] < 110:
					datas.append([i, j])

		# 以Y軸作為參考重新排序數字大小
		datas = sorted(datas, key=lambda d: d[1])
		datas = np.array(datas)

		# print(datas)
		# print(datas[:,0].min(),datas[:,0].max())
		# print(datas[:,1].min(),datas[:,1].max())
		global percent
		global med
		
		# 將鄰近的兩點相減(排除範圍以外的雜色)
		data = []
		a = []
		for i in range(len(datas)):
			data.append(datas[i] - datas[i-1])

		for i, pixel in enumerate(data[:-2]):
			if (-5 < pixel[0] < 10) and (-5 < pixel[1] < 10):
				a.append([datas[i][0], datas[i][1]])
		datas = np.array(a)

		# 取得黃色範圍面積
		x = datas[:, 0].max()-datas[:, 0].min()
		y = datas[:, 1].max()-datas[:, 1].min()
		# 計算黃色面積在圖形中的占比
		percent = (x*y)/(w*h*math.pi)*100
		print('percent', round(percent, 2))

		# 以擷取畫面二分之一處，取得圓心
		x0 = w/2
		y0 = h/2
		# 計算黃色範圍在圖形中位置(角度)
		datas_angle = []
		for i in datas:
			x1 = i[0]
			y1 = i[1]

			a = angle(x0, y0, x1, y1)
			if a != None:
				datas_angle.append(round(a, 2))
		# 取得範圍內中位數
		color_angles = np.array(datas_angle)
		med = round(np.median(color_angles), 2)
		print(round(np.median(color_angles), 2))

		if percent < 3:
			return False
		else:
			return True
	except:
		return False

def angle(x0, y0, x1, y1):
	if (x1-x0) > 0 and (y1-y0) <0:
		# 第1象限
		r1 = (x1-x0)/(y1-y0)
		d = math.atan(r1)
		ans = d/math.pi*180
		return -ans

	elif (x1-x0) > 0 and (y1-y0) >0:
		# 第2象限
		r1 = (y1-y0)/(x1-x0)
		d = math.atan(r1)
		ans = d/math.pi*180
		return ans + 90

	elif (x1-x0) < 0 and (y1-y0) >0:
		# 第3象限
		r1 = (y1-y0)/(x1-x0)
		d = math.atan(r1)
		ans = d/math.pi*180
		return 360-(90-ans)

	elif (x1-x0) < 0 and (y1-y0) <0:
		# 第4象限
		r1 = (y1-y0)/(x1-x0)
		d = math.atan(r1)
		ans = d/math.pi*180
		return 360-(90-ans)


if __name__ == '__main__':
	print(math_image_range())
