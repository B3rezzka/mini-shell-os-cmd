import os
import sys
import shlex
import src.ls_comm as l
import src.cd_comm as c
import src.cp_comm as k
import src.mv_comm as m
import src.rm_comm as r
from src.logger import log_command

def command_handler(commands):
    cmd_str = " ".join(commands)  # полная строка команды
    match commands[0]:
        case "cd":
            result = c.cd(commands)
            if result is not None:  # если была ошибка
                log_command(cmd_str, success=False, error_msg=result)
        case "ls":
            result = l.ls(commands[1:])
            if result is not None:
                log_command(cmd_str, success=False, error_msg=result)
        case "cat":
            result = c.cat(commands[1:])
            if result is not None:
                log_command(cmd_str, success=False, error_msg=result)
        case "cp":
            result = k.cp(commands[1:])
            if result is not None:
                log_command(cmd_str, success=False, error_msg=result)
        case "mv":
            result = m.mv(commands[1:])
            if result is not None:
                log_command(cmd_str, success=False, error_msg=result)
        case "rm":
            result = r.rm(commands[1:])
            if result is not None:
                log_command(cmd_str, success=False, error_msg=result)
        case "exit":
            sys.exit(0)
        case _:
            print(f"minishell: Command not found: {commands[0]}")
            log_command(cmd_str, False, f"minishell: Command not found: {commands[0]}")

def main() -> None:
    """
    Программа запуска командной строки.
    """
    while True:
        try:
            current_dir = os.getcwd()
        except FileNotFoundError:
            current_dir = ""
            print("minishell: Path not found")
            log_command("", False, "minishell: Path not found")
            break
        prompt = f"{current_dir}$ "
        try:
            request = input(prompt)
            if not request:
                continue
            log_command(request, success=True)
            command_handler(shlex.split(request))
        except EOFError:
            print()  # новая строка при Ctrl+D
            break
        except KeyboardInterrupt:
            print()  # новая строка при Ctrl+C
            continue

if __name__ == "__main__":
    main()
