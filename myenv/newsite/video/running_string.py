#!/usr/bin/env python3

import cv2
import sys
import numpy as np
from PIL import ImageFont, ImageDraw, Image

def create_running_string(text):
	# длительность видео и частота кадров
	duration = 3
	fps = 24

	# задание кода идентификации формата данных и размера видео
	fourcc_code = cv2.VideoWriter_fourcc(*"XVID")
	size = (100, 100)

	# название видеофайла с бегущей строкой
	file_path = "video/output.avi"

	# задание шрифта
	font_path = "video/arial.ttf"
	font_size = 40
	font_width = 2
	color = (255, 0, 0)
	font = ImageFont.truetype(font_path, font_size)

	# инициализация пустого кадра
	frame = np.zeros((*size, 3), np.uint8)

	# расчёт размера текста при выводе в данном шрифте
	text_bounds = ImageDraw.Draw(Image.fromarray(frame)).textbbox((10, 10), text, font=font, stroke_width=font_width)
	text_length, text_width = text_bounds[2] - text_bounds[0], text_bounds[3] - text_bounds[1]

	# расчёт начальных координат и общего числа кадров
	x_coord, y_coord = size[0] // 4, size[1]
	total = duration * fps

	# создание видеофайла
	out = cv2.VideoWriter(file_path, fourcc_code, fps, size[::-1])

	for i in range(total):
		# очистка кадра
		frame.fill(255)

		# преобразование в изображение PIL для размещения символов не только из ASCII
		pil = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
		draw = ImageDraw.Draw(pil)

		# размещение текста с постепенным смещением влево
		draw.text((int(y_coord - (text_length + size[1]) * i // (total - 1)), x_coord), text, fill=color[::-1], font=font)

		# обратное преобразование кадра
		frame = cv2.cvtColor(np.asarray(pil), cv2.COLOR_RGB2BGR)

		# запись кадра
		out.write(frame)
		cv2.waitKey(1)

	# закрытие файла
	out.release()
	
	return file_path

if __name__ == "__main__":
	create_running_string("Example string")
