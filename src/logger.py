from datetime import datetime
import os

def log_command(cmd_str = '', success=True, error_msg=None):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    curr_dir = os.path.dirname(os.path.abspath(__file__))
    log_file_path =os.path.join(curr_dir, "shell.log")
    with open(log_file_path, "a", encoding="utf-8") as f:
        if success:
            f.write(f"[{timestamp}] {cmd_str}\n")
        else:
            f.write(f"[{timestamp}] ERROR: {error_msg}\n")