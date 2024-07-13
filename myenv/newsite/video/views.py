from django.shortcuts import render
from django.http import HttpResponse, FileResponse
import mimetypes
from .running_string import create_running_string

def video(request):
    # получение текста в качестве параметра строки запроса типа ?text=str
    text = request.GET.get("text")
    print(repr(text))
	
    if text:
        # запуск скрипта для создания видео бегущей строки и получение пути к созданному файлу
        file_path = create_running_string(text)
        
        # определение типа файла для грамотного чтения браузером
        mime_type, _ = mimetypes.guess_type(file_path)
        
        # открытие файла в режиме чтения байт-кода
        file = open(file_path, 'rb')
        
        # создание ответа, содержащего файл и инструкцию с указанием скачать этот файл
        response = FileResponse(file, content_type=mime_type)
        response['Content-Disposition'] = f'attachment; filename="{file_path}"'
        
        # возврат созданного ответа
        return response
        
    else:
        # иначе сообщение об ошибке
        return HttpResponse("Введите текст в адресной строке")
