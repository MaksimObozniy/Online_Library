# Online_Library

Этот проект — простой сайт, на котором можно полистать книги с разбивкой на страницы. 

Ссылка на рабочий сайт: https://maksimobozniy.github.io/Online_Library/

### Фото с сайта
<img width="847" alt="image" src="https://github.com/user-attachments/assets/78e961ed-28c3-4ab3-a870-371544c80a4a" />

## Как запустить проект у себя

1. Клонируй проект:

```bash
git clone https://github.com/MaksimObozniy/Online_Library.git
cd Online_Library
```

2. Установи зависимости:

```bash
pip install -r requirements.txt
```

3. Запусти сайт локально с автообновлением:

```bash
python render_website.py
```

После запуска сайт откроется по адресу:
```
http://127.0.0.1:5500/
```

Изменения будут подхватываться автоматически, страница будет перезагружаться сама.

## Как сгенерировать сайт для выгрузки на GitHub Pages.

```bash
python render_website.py 
```

В папке `docs/` появится финальная версия сайта.

## Как опубликовать сайт на GitHub Pages

1. Перейди в настройки репозитория
2. В разделе Pages выбери ветку `main` и папку `/docs`
3. Сохрани — сайт будет доступен по ссылке вида:

```
https://<твоё_имя>.github.io/<название_репозитория>/

```

---
