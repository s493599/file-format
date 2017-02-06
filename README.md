# file-format
Консольный клиент для open-file.ru

## Установка
Скопировать файл file-format.py в директорию с исполняемыми файлами и убрать расширение, 
например 

`cp ./file-format.py /usr/local/bin/file-format`

Сделать файл исполняемым

`sudo chmod +x /usr/local/bin/file-format`

Установить неоходимые зависимости (если у вас ещё их нет)
* bs4
* texttable
* requests


## Использование
Например, что бы узнать информацию про формат jpg, необходимо выполнить команду

`file-format jpg`

Резульатом будет следующая таблица

```
  Формат   |                Тип                  |   Описание                      
===========+=====================================+===========================
.jpg       | Файл изображения JPEG               | Растровые изображения                              
.jpg2      | Файл изображения JPEG 2000          | Растровые изображения                              
.jpgw      | JPEG-файл изображения местности     | Географич. файлы                                   
.mjpg      | Видео-файл Motion JPEG              | Видео                                              
.pjpg      | Файл изображения Progressive JPEG   | Растровые изображения  
```

## Возможные ошибки
| Текст ошибки | Описание и метод решения |
|----------|---------|
| Ошибка: Не указан формат. | При запуске программы не передан арумент с названием формата. См. раздел **Использование** | 
| Ошибка: Раширение не найдено | Указанное расширение не найдено в базе. Проверьте правильность написания. |

## Лицензирование
Программа распространяется по MIT License

