import os
import shutil
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
                print(f"mv: Cannot stat '{source}': No such file or directory")
                return f"mv: Cannot stat '{source}': No such file or directory"
            if not os.access(source, os.R_OK | os.W_OK): # Проверяем права на чтение и удаление источника
                print(f"mv: Permission denied to access '{source}'")
                return f"mv: Permission denied to access '{source}'"
            if os.path.isdir(dest): # Если назначение — существующая директория — перемещаем внутрь
                dest_path = os.path.join(dest, os.path.basename(source))
            else:
                dest_path = dest
            shutil.move(source, dest_path) # Перемещаем
            print(f"Moved '{source}' to '{dest_path}'")
            return None
        except PermissionError:
            print(f"mv: Permission denied: '{source}' -> '{dest}'")
            return f"mv: Permission denied: '{source}' -> '{dest}'"