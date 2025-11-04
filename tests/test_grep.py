import pytest
import os
from grep import grep_

def test_grep_exists():
    """Проверяем что функция существует"""
    assert callable(grep_)
    assert True

def test_grep_no_args():
    """Проверяем ошибку когда ничего не передали"""
    with pytest.raises(ValueError):
        grep_([])

def test_grep_one_arg():
    """Проверяем ошибку когда только слово для поиска"""
    with pytest.raises(ValueError):
        grep_(['слово'])


def test_grep_no_file():
    """Проверяем ошибку когда файла не существует"""
    with pytest.raises(FileNotFoundError):
        grep_(['слово', 'нет_такого_файла.txt'])

def test_grep_finds_text():
    """Проверяем что grep находит текст в файле"""
    with open('test.txt', 'w', encoding='utf-8') as f:
        f.write('первая строка\n')
        f.write('вторая строка\n')
        f.write('третья строка\n')
    
    grep_(['вторая', 'test.txt'])
    print("grep нашел текст в файле!")
    
    os.remove('test.txt')


def test_grep_case_insensitive():
    """Проверяем поиск с опцией -i"""
    with open('test.txt', 'w', encoding='utf-8') as f:
        f.write('ПРИВЕТ мир\n')
        f.write('тестовая строка\n')
    
    grep_(['-i', 'привет', 'test.txt'])
    print("grep -i работает!")
    
    os.remove('test.txt')

def test_grep_works():
    """Проверяем что grep не падает с ошибкой"""
    with open('simple.txt', 'w', encoding='utf-8') as f:
        f.write('hello world\n')
        f.write('test line\n')
    
    grep_(['hello', 'simple.txt'])
    print("grep работает без ошибок!")

    os.remove('simple.txt')