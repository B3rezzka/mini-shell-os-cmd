import os
import shutil
import sys


def cp(arguments):
    """
    Команда cp: копирует файл или каталог.
    Поддерживает:
      - cp source dest - копирование файла или каталога.
      - cp -r source dest - рекурсивное копирование каталога.
    При ошибках - выводит сообщение и записывает в журнал.
    """
    if len(arguments) < 2:
        print("cp: Missing file operand")
        return "cp: Missing file operand"
    recursive = False
    sources = []
    destination = ''
    i = 0
    while i < len(arguments):
        if arguments[i] == "-r":
            recursive = True
        else:
            sources.append(arguments[i])
        i += 1
    if len(sources) < 2:
        print("cp: Missing destination file operand after source")
        return "cp: Missing destination file operand after source"
    destination = sources[-1] # Последний аргумент - назначение
    sources = sources[:-1]  # всё остальное - источники
    for source in sources:
        try:
            if not os.path.exists(source):
                print(f"cp: Cannot stat '{source}': No such file or directory")
                return f"cp: Cannot stat '{source}': No such file or directory"
            if os.path.isdir(source):
                if not recursive:
                    print(f"cp: Omitting directory '{source}' (use -r to copy directories)")
                    return f"cp: Omitting directory '{source}' (use -r to copy directories)"
                if os.path.exists(destination) and os.path.isdir(destination): # Рекурсивное копирование каталога
                    dest_path = os.path.join(destination, os.path.basename(source))
                else:
                    dest_path = destination
                shutil.copytree(source, dest_path, dirs_exist_ok=True)
                print(f"Copied directory '{source}' to '{dest_path}'")
                return None
            else:
                if os.path.exists(destination) and os.path.isdir(destination): # Копирование файла
                    dest_path = os.path.join(destination, os.path.basename(source))
                else:
                    dest_path = destination
                shutil.copy2(source, dest_path)
                print(f"Copied file '{source}' to '{dest_path}'")
                return None
        except PermissionError:
            print(f"cp: Permission denied: '{source}' -> '{destination}'")
            return f"cp: Permission denied: '{source}' -> '{destination}'"