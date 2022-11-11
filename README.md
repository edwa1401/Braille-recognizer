# Braille recognizer

Braille recognizer является web-приложением по распознованию текста,
написанного шрифтом Брайля, и его перевод в плоскопечатный текст.
Пользователь может загрузить фотографию в формате jpg или
jpeg и получить перевод, нанесённый на фотографию, и в виде текста.

![Иллюстрация к проекту](https://github.com/edwa1401/Braille-recognizer/raw/main/cover_image.png)

Подробней о шрифте Брайля:
https://ru.wikipedia.org/wiki/Шрифт_Брайля

## Источники
При разработке проекта использован 
Angelina Braille Images Dataset

https://github.com/IlyaOvodov/AngelinaDataset

## Установка

1. Клонируйте репозиторий с github 
```
git clone https://github.com/edwa1401/Braille-recognizer.git
```
2. Создайте виртуальное окружение 
3. Установите зависимости 
```
pip install -r requirements.txt
```
4. Добавьте в корень проекта папку `downloads` для хранения фотографий

## Запуск web-приложения
* Для ОС Mac и Linux
```
chmod +x run.sh
./run.sh
```
* Для Windows: создайте файл `run.bat` в корне проекта, в который добавьте 
`set FLASK_APP=webapp && set FLASK_ENV=development && set FLASK_DEBUG=1
            && flask run`
```
run.bat
```