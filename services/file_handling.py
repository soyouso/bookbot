import os
import sys

BOOK_PATH = 'book/book.txt'
PAGE_SIZE = 1050

book: dict[int, str] = {}


# Функция, возвращающая строку с текстом страницы и ее размер
def _get_part_text(text: str, start: int, size: int) -> tuple[str, int]:
    res = text[start: size + start]
    if start + size < len(text):
        last = text[start + size]
    else:
        return (text[start:], len(text[start:]))

    for i in reversed(res):
        if i in ',.;:!?' and last not in ',.;:!?':
            return (res, len(res))
        res = res[:-1]
        last = i


    return (text[start: size + start], size)


# Функция, формирующая словарь книги
book: dict[int, str] = {}
PAGE_SIZE = 1050


# Дополните эту функцию, согласно условию задачи
def prepare_book(path: str) -> None:
    with open(path, 'r', encoding='utf-8') as f:
        t = f.read()
        t_length = len(t)
        s = 0
        for i in range(t_length // PAGE_SIZE + 1):
            sheet = _get_part_text(t, s, PAGE_SIZE)
            book[i + 1] = sheet[0].lstrip()
            s += sheet[1]


# Вызов функции prepare_book для подготовки книги из текстового файла
prepare_book(os.path.join(sys.path[0], os.path.normpath(BOOK_PATH)))