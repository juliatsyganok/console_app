import os
import shutil
from pathlib import Path

def cat(args):
    if not args:
        raise ValueError("Нт файла")
    
    file_path = Path(args[0])
    
    if not file_path.exists():
        raise FileNotFoundError("Не существует файл")
    if file_path.is_dir():
        raise IsADirectoryError("Каталог")

    with open(file_path, 'r', encoding='utf-8') as f:
        print(f.read())


def cp(args):
    if len(args) < 2:
        raise ValueError("Нет пути")
    
    dop = [x for x in args if x != '-r']
    
    src = Path(dop[0])
    d = Path(dop[1])
    
    if not src.exists():
        raise FileNotFoundError("Не сущетсвует")
     
    if src.is_file():
        shutil.copy2(src, d)
    elif src.is_dir() and '-r' in args:
        shutil.copytree(src, d)
    else:
        raise ValueError("Невозможно выполнить копирование")


def mv(args):
    if len(args) < 2:
        raise ValueError("Нет пути")
    if not Path(args[0]).exists():
        raise FileNotFoundError("Не сущетсвует")
    
    shutil.move(str(Path(args[0])), str(Path(args[1])))


def rm(args):

    if not args:
        raise ValueError("Нет пути")

    dop = [x for x in args if x != '-r']
    
    tg = Path(dop[0])

    if str(tg) in ['/', '..']:
        raise PermissionError("Нельзя удалить корневой каталог")
    
    if not tg.exists():
        raise FileNotFoundError("Не существует")
    
    if tg.is_file():
        os.remove(tg)
    elif tg.is_dir():
        confirm = input("Удалить Y/n?")
        if confirm.lower() == 'y':
            shutil.rmtree(tg)

    else:
        raise ValueError("Невозможно выполнить удаление")