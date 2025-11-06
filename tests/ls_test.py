import pytest
import sys
import os


project_root = os.path.dirname(os.path.dirname(__file__))  # поднимаемся на 2 уровня вверх
sys.path.insert(0, project_root)


from src.ls_comm import ls


def test_positive():
    assert ls([]) == None

def test_positive_long():
    assert ls(['-l']) == None

def test_no_directory():
    assert ls(['valorant']) == "ls: Cannot access 'valorant': No such file or directory"

def test_too_many_args():
    assert ls(['52', '42', '1984']) == "ls: Too many arguments"

def test_permission_denied():
    assert ls(['/root']) == "ls: Cannot open directory '../root': Permission denied"