import pytest
import os
from pathlib import Path

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from ls_cd import ls, cd

def test_ls_current_dir():
    """Простой тест ls в текущей директории"""
    ls([])

def test_ls_detailed_option():
    """Тест ls с опцией -l"""
    ls(['-l'])

def test_cd_home():
    """Тест cd home"""
    cd(['~'])
    assert str(Path.home()) in os.getcwd()

def test_cd_up():
    """Тест cd .."""
    start = os.getcwd()
    cd(['..'])
    cd([start]) 

def test_ls_error():
    """Тест ошибки ls"""
    with pytest.raises(FileNotFoundError):
        ls(['несуществующая_папка'])

def test_cd_error():
    """Тест ошибки cd"""
    with pytest.raises(FileNotFoundError):
        cd(['несуществующая_папка'])