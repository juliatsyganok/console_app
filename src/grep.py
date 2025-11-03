import os
from pathlib import Path


def file(path, ptr, i_arg):
    try:
        with open(path, 'r', encoding='utf-8', errors='ignore') as file:
            for lnum, line in enumerate(file, 1):
                if i_arg:
                    s_line = line.lower()
                else:
                    s_line = line
                if ptr in s_line:
                    new = line.strip()
                    print(f"{path}:{lnum}: {new}")
                    
    except Exception as e:
        print("Ошибка чтения файла")


def direct(path, ptr, rec, i_arg):
    try:
        for item in path.iterdir():
            if item.is_file():
                file(item, ptr, i_arg)
            elif item.is_dir() and rec:
                direct(item, ptr, rec, i_arg)
    except PermissionError:
        print("Невозможно открыть")



def grep_(args):
    if len(args) < 2:
        raise ValueError("Неправильный ввод команды")
    
    ptr = args[0]
    path = args[1]
    rec = '-r' in args
    i_arg = '-i' in args
    
    path = Path(path)
    
    if not path.exists():
        raise FileNotFoundError("Нет такого пути")
  
    if i_arg:
        s_ptr = ptr.lower()
    else:
        s_ptr = ptr
    
    if path.is_file():
        file(path, s_ptr, i_arg)
    elif path.is_dir():
        direct(path, s_ptr, rec, i_arg)
    else:
        raise ValueError("Не директория")
