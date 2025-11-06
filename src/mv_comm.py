import os
import shutil
import sys
from src.logger import log_command

def mv(arguments):
    """
    Команда mv: перемещает или переименовывает файл/каталог.
    Если назначение - существующая папка - перемещает внутрь неё.
    Проверяет существование источника и права.
    """
    if len(arguments) < 2:
        print("mv: missing file operand")
        return "mv: missing file operand"

    sources = arguments[:-1]      # все аргументы, кроме последнего — источники
    dest = arguments[-1]   # последний аргумент — назначение

    for source in sources:
        try:
            if not os.path.exists(source):
                print(f"mv: cannot stat '{source}': No such file or directory")
                log_command('', False, f"mv: cannot stat '{source}': No such file or directory")
                continue

            # Проверяем права на чтение и удаление источника
            if not os.access(source, os.R_OK | os.W_OK):
                print(f"mv: permission denied to access '{source}'")
                log_command('', False, f"mv: permission denied to access '{source}'")
                continue

            # Если назначение — существующая директория — перемещаем внутрь
            if os.path.isdir(dest):
                dest_path = os.path.join(dest, os.path.basename(source))
            else:
                dest_path = dest
            shutil.move(source, dest_path) # Перемещаем
            print(f"Moved '{source}' to '{dest_path}'")
            return None
        except PermissionError:
            print(f"mv: permission denied: '{source}' -> '{dest}'")
            return f"mv: permission denied: '{source}' -> '{dest}'"