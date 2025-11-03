import os
import logging
from datetime import datetime
from ls_cd import ls, cd
from cat_cp_mv_rm import cat, cp, mv, rm
from grep import grep_

COMMANDS = {
    'ls': ls,
    'cd': cd,
    'cat': cat,
    'cp': cp,
    'mv': mv,
    'rm': rm,
    'grep': grep_
}


def log():
    """
    логирует команды в файл sheell.log
    """
    log_dir = "logs"
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    
    log_file = os.path.join(log_dir, "shell.log")

    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format='[%(asctime)s] %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

def shell():
    """
    Омновная функция для обработки ввода пользователя. 
    Запускает обработку и логирование
    """
    print("Для выхода введите 'stop'")
    
    while True:
        cwd = os.getcwd()
        case = input(f"\n{cwd} $ ").strip()

        if not case:
            continue

        logging.info(case)
        if case.lower() == 'stop':
            break

        p = case.split()
        name, args = p[0], p[1:]
    
        
        if name in COMMANDS:
            try:
                COMMANDS[name](args)
            except Exception as e:
                print(f"ERROR: {str(e)}")
                logging.error(f"ERROR: {str(e)}")
        else:
            print("Нет такой команды")
            logging.error("Нет такой команды")