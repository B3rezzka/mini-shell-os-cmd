import os
import os.path
from datetime import datetime
import pwd

def ls(arguments):
    """
    Просматривает есть ли в строке запрос на длинную форму.
    """
    path = '.'
    l_f = False
    for arg in arguments:
        if arg == "-l":
            l_f = True
        else:
            if path != ".":
                print("ls: Too many arguments")
                return "ls: Too many arguments"
            path = arg
    if l_f:
        ls_l(path)
    else:
        ls_s(path)

def ls_s(path):
    """
    Выводит список файлов и папок в директории (как 'ls').
    """
    if not os.path.exists(path):
        print(f"ls: Cannot access '{path}': No such file or directory")
        return f"ls: Cannot access '{path}': No such file or directory"

    try:
        files = os.listdir(path)
        files.sort()
        print(*files, sep='\t', end='\n')
        return None
    except PermissionError:
        print(f"ls: Cannot open directory '{path}': Permission denied")
        return f"ls: Cannot open directory '{path}': Permission denied"

def ls_l(path):
    """
    Выводит подробный список файлов и папок (как 'ls -l').
    Показывает права, владельца (ID), группу (ID), размер, дату.
    Если путь - файл, выводит информацию о нём.
    """
    if not os.path.exists(path):
        print(f"ls: Cannot access '{path}': No such file or directory")
        return f"ls: Cannot access '{path}': No such file or directory"

    if not os.path.isdir(path):
        # Если указан конкретный файл, а не папка
        stat = os.stat(path)
        perm = get_permissions(stat.st_mode, path)
        nlink = stat.st_nlink
        user_name, group_name = get_user_group_names(stat.st_uid, stat.st_gid)
        size = stat.st_size
        mtime = datetime.fromtimestamp(stat.st_mtime).strftime('%b %d %H:%M')
        print(f"{perm} {nlink:>3} {user_name:>5} {group_name:>5} {size:>8} {mtime} {os.path.basename(path)}")
    try:
        items = os.listdir(path)
        items.sort()
        for item in items:
            full_path = os.path.join(path, item)
            try:
                stat = os.stat(full_path)
                perm = get_permissions(stat.st_mode, full_path)
                nlink = stat.st_nlink
                user_name, group_name = get_user_group_names(stat.st_uid, stat.st_gid)
                size = stat.st_size
                mtime = datetime.fromtimestamp(stat.st_mtime).strftime('%b %d %H:%M')
                print(f"{perm} {nlink:>3} {user_name:>5} {group_name:>5} {size:>8} {mtime} {item}")
            except OSError as e:
                print(f"ls: Unkown information about {item}")
                return f"ls: Unkown information about {item}"
    except PermissionError:
        print(f"ls: Cannot open directory '{path}': Permission denied")
        return f"ls: Cannot open directory '{path}': Permission denied"

def get_user_group_names(uid, gid):
    """
    Пытается получить имя пользователя и группы по ID.
    Возвращает кортеж (user_name, group_name).
    Если не удалось - возвращает (uid, gid) как строки.
    """
    try:
        user_name = pwd.getpwuid(uid).pw_name
    except (ImportError, KeyError):
        user_name = str(uid)  # если не удалось — оставляем ID
    try:
        import grp
        group_name = grp.getgrgid(gid).gr_name
    except (ImportError, KeyError):
        group_name = str(gid)
    return user_name, group_name

def get_permissions(mode, path):
    """
    Преобразует числовое значение прав (mode) в строку вида 'drwxr-xr--'.
    Первый символ - тип файла ('d' для директории, '-' для обычного файла).
    Остальные 9 - права владельца, группы и остальных (rwx).
    """
    perm = 'd' if os.path.isdir(path) else '-'
    for i in range(0, 9, 3):  # 0, 3, 6 — биты для владельца, группы, остальных
        r = 'r' if mode & (1 << (8 - i)) else '-'
        w = 'w' if mode & (1 << (7 - i)) else '-'
        x = 'x' if mode & (1 << (6 - i)) else '-'
        perm += r + w + x
    return perm