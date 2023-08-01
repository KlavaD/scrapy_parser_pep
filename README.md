# Проект парсинг документов PEP с использованием Scrapy

Автор - 
*   [Клавдия Дунаева](https://www.t.me/klodunaeva)

## Парсинг документов PEP. 

_pep_ДатаВремя.csv_ - Файл со списком PEP имеет три столбца: «Номер», «Название» и «Статус».

_status_summary_ДатаВремя.csv_ - Файлы со сводкой по статусам, в котором перечислены
используемые статусы и их количество.

**Инструменты и стек:**

Python 3.7+,\
[Scrapy](https://docs.scrapy.org/)

**Как запустить проект:**

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/KlavaD/scrapy_parser_pep
```
Создать и активировать виртуальное окружение:

```
python3 -m venv env
```

* Если у вас Linux/macOS

    ```
    source env/bin/activate
    ```

* Если у вас windows

    ```
    source env/scripts/activate
    ```

Обновить pip:

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

В командной строке ввести:

```
scrapy crawl pep  
```