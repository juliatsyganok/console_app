import os
import stat
import time
from pathlib import Path

def ls(args: list[str]) -> None:
    """
    Показывает содержимое дирректории, обрабатывает аргумент -l
    """
    path = Path.cwd()
    f = False
    for arg in args:
        if arg == '-l':
            f = True
        elif arg[0] != '-': 
            path = Path(arg)

    if not path.exists():
        raise FileNotFoundError("Нет каталога")
    if not path.is_dir():
        raise NotADirectoryError("Не каталог")

    items = list(path.iterdir())

    if not(f):
        for item in items:
            print(item.name)
    else:
        for item in items:
            stat_info = item.stat() 
            mod_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(stat_info.st_mtime))
            size = stat_info.st_size
            permissions = stat.filemode(stat_info.st_mode) 
            
            print(f"{permissions} {size:8} {mod_time} {item.name}")

def cd(args: list[str]) -> None:
    """
    Меняет директорию. Поддерживаются .. и ~
    """
    if not args:
        new = Path.home()
    else:
        case = args[0]
        if case == "..":
            new = Path.cwd().parent
        elif case == "~":
            new = Path.home()
        else:
            new= Path(case)

    if not new.exists():
        raise FileNotFoundError("Нет такого каталога")
    if not new.is_dir():
        raise NotADirectoryError("Не каталог")
    
    os.chdir(new)