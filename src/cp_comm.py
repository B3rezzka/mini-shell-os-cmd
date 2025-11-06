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
        print("cp: missing file operand", file=sys.stderr)
        sys.exit(0)
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
        print("cp: missing destination file operand after source", file=sys.stderr)
        sys.exit(0)
    destination = sources[-1] # Последний аргумент - назначение
    sources = sources[:-1]  # всё остальное - источники
    for source in sources:
        try:
            if not os.path.exists(source):
                print(f"cp: cannot stat '{source}': No such file or directory", file=sys.stderr)
                continue

            if os.path.isdir(source):
                if not recursive:
                    print(f"cp: omitting directory '{source}' (use -r to copy directories)", file=sys.stderr)
                    continue

                if os.path.exists(destination) and os.path.isdir(destination): # Рекурсивное копирование каталога
                    dest_path = os.path.join(destination, os.path.basename(source))
                else:
                    dest_path = destination

                shutil.copytree(source, dest_path, dirs_exist_ok=True)
                print(f"Copied directory '{source}' to '{dest_path}'")

            else:
                if os.path.exists(destination) and os.path.isdir(destination): # Копирование файла
                    dest_path = os.path.join(destination, os.path.basename(source))
                else:
                    dest_path = destination

                shutil.copy2(source, dest_path)
                print(f"Copied file '{source}' to '{dest_path}'")

        except PermissionError:
            error_msg = f"cp: permission denied: '{source}' -> '{destination}'"
            print(error_msg, file=sys.stderr)
            sys.exit(0)