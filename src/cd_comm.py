import os
from src.logger import log_command

def cd(commands = ['cd']):
    """
    Команда cd: переход в указанный каталог.
    """
    if len(commands) == 1:
        target = os.path.expanduser("~")
    else:
        target = commands[1]
    match target:
        case "..":
            target = ".."
        case "~":
            target = os.path.expanduser("~")
    try:
        os.chdir(target)
        return None
    except FileNotFoundError:
        print(f"cd: No such directory: {target}")
        return f"cd: No such directory: {target}"
    except PermissionError:
        print(f"cd: Permission denied: {target}")
        return f"cd: Permission denied: {target}"

def cat(arguments):
    """
    Команда cat: выводит содержимое файла в консоль.
    Если передан каталог или файл не существует - ошибка и запись в журнал.
    """
    if len(arguments) == 0:
        print("cat: Missing file operand")
        return "cat: Missing file operand"
    for filepath in arguments:
        try:
            if os.path.isdir(filepath):
                print(f"cat: {filepath}: Is a directory")
                log_command('', False, f"cat: {filepath}: Is a directory")
                continue

            # Проверяем существование файла
            if not os.path.exists(filepath):
                print(f"cat: {filepath}: No such file or directory")
                log_command('', False, f"cat: {filepath}: No such file or directory")
                continue

            # Читаем и выводим содержимое файла
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                print(content, end='')  # end='' чтобы не добавлять лишний перевод строки
                return None

        except PermissionError:
            print(f"cat: {filepath}: Permission denied")
            return f"cat: {filepath}: Permission denied"
        except UnicodeDecodeError:
            print(f"cat: {filepath}: Not a text file (encoding error)")
            return f"cat: {filepath}: Not a text file (encoding error)"