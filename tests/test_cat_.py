import pytest
import os
from pathlib import Path
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from cat_cp_mv_rm import cat, cp, mv, rm

def test_cat_works():
    """Просто проверяем что cat не падает с ошибкой"""
    cat(['test_file.txt'])

def test_cat_no_file():
    """Проверяем ошибку когда файла нет"""
    with pytest.raises(FileNotFoundError):
        cat(['нет_файла.txt'])

def test_cat_no_args():
    """Проверяем ошибку когда нет аргументов"""
    with pytest.raises(ValueError):
        cat([])




def test_cp_file():
    """Проверяем копирование файла"""
    with open('original.txt', 'w') as f:
        f.write('текст')
    
    cp(['original.txt', 'copy.txt'])
    assert os.path.exists('copy.txt')
    os.remove('original.txt')
    os.remove('copy.txt')

def test_cp_no_args():
    """Проверяем ошибку когда мало аргументов"""
    with pytest.raises(ValueError):
        cp(['один_аргумент'])




def test_mv_file():
    """Проверяем перемещение файла"""
    with open('move_me.txt', 'w') as f:
        f.write('текст')
    
    mv(['move_me.txt', 'moved.txt'])
    assert not os.path.exists('move_me.txt')
    assert os.path.exists('moved.txt')
    os.remove('moved.txt')

def test_mv_no_args():
    """Проверяем ошибку когда мало аргументов"""
    with pytest.raises(ValueError):
        mv(['один_аргумент'])





def test_rm_file():
    """Проверяем удаление файла"""
    with open('delete_me.txt', 'w') as f:
        f.write('текст')
    rm(['delete_me.txt'])
    assert not os.path.exists('delete_me.txt')

def test_rm_no_args():
    """Проверяем ошибку когда нет аргументов"""
    with pytest.raises(ValueError):
        rm([])

def test_rm_protected_paths():
    """Проверяем что нельзя удалить системные пути"""
    with pytest.raises(PermissionError):
        rm(['/'])
    
    with pytest.raises(PermissionError):
        rm(['..'])
