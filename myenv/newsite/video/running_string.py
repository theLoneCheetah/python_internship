#!/usr/bin/env python3

import cv2
import sys
import numpy as np

def create_running_string(text):
	# длительность видео и частота кадров
	duration = 3
	fps = 24

	# захват изображения для считывания разрешения (1280x960)
	cap = cv2.VideoCapture(0)
	fourcc_code = cv2.VideoWriter_fourcc(*"XVID")
	size = (1000, 1000)

	# закрытие захвата камеры
	cap.release()

	# создание видеофайла
	file_path = "output.avi"
	out = cv2.VideoWriter(file_path, fourcc_code, fps, size[::-1])

	# задание шрифта
	font = cv2.FONT_HERSHEY_SIMPLEX
	font_size = 10
	font_width = 20
	color = (255, 0, 0)

	# расчёт размера текста при выводе в данном шрифте
	text_size, _ = cv2.getTextSize(text, font, font_size, font_width)

	# расчёт начальных координат и общего числа кадров
	x_coord, y_coord = size[0] // 3 * 2, size[1] // 2
	total = duration * fps

	# инициализация пустого кадра
	frame = np.zeros((*size, 3), np.uint8)

	for i in range(total):
		# очистка кадра
		frame.fill(255)
		
		# размещение текста с постепенным смещением влево
		cv2.putText(frame, text, (int(y_coord - text_size[0] * i // total), x_coord), font, font_size, color, font_width)
		
		# запись кадра
		out.write(frame)
		cv2.waitKey(1)

	# закрытие файла
	out.release()
	
	return file_path

if __name__ == "__main__":
	create_running_string("Example string")
