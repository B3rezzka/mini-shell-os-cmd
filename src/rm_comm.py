import os
import shutil
from src.logger import log_command


def rm(arguments):
    """
    Команда rm: удаление файлов и каталогов.
    Поддерживает:
      - rm file.txt - удаление файла.
      - rm -r dir/ - рекурсивное удаление каталога (с подтверждением).
    Запрещено удалять '/' и '..'.
    """
    if len(arguments) == 0:
        print("rm: Missing operand")
        return "rm: Missing operand"
    recursive = False
    targets = []
    i = 0
    while i < len(arguments):
        if arguments[i] == "-r":
            recursive = True
        else:
            targets.append(arguments[i])
        i += 1
    for target in targets:
        try:
            abs_target = os.path.abspath(target)
            if abs_target == "/" or abs_target == os.path.abspath(".."):
                print(f"rm: Refusing to remove '{target}': it is dangerous")
                return f"rm: Refusing to remove '{target}': it is dangerous"
            if not os.path.exists(target):
                print(f"rm: Cannot remove '{target}': No such file or directory")
                return "rm: Cannot remove '{target}': No such file or directory"
            if os.path.isdir(target) and not recursive:
                print(f"rm: Cannot remove '{target}': is a directory (use -r to remove directories)")
                return f"rm: Cannot remove '{target}': is a directory (use -r to remove directories)"
            if os.path.isdir(target) and recursive: # Если это каталог и есть -r - запрашиваем подтверждение
                confirm = input(f"rm: Remove directory '{target}' recursively? (y/n): ").strip().lower()
                if confirm not in ('y', 'yes'):
                    print("Operation cancelled.")
                    log_command('', False, "Operation cancelled.")
                    continue
            if os.path.isfile(target):
                os.remove(target)
                print(f"Removed file: {target}")
                return None
            elif os.path.isdir(target):
                shutil.rmtree(target)
                print(f"Removed directory: {target}")
                return None
        except PermissionError:
            print(f"rm: Permission denied: '{target}'")
            return f"rm: Permission denied: '{target}'"