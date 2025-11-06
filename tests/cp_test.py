import pytest
import sys
import os


project_root = os.path.dirname(os.path.dirname(__file__))  # поднимаемся на 2 уровня вверх
sys.path.insert(0, project_root)


from src.cp_comm import cp


def test_positive():
    assert cp(['42.txt', '52.txt']) == None

def test_missing_file_operand():
    assert cp(['../525252.txt']) == "cp: Missing file operand"

def test_no_directory():
    assert cp(['gol.txt', '../sooskin']) == "cp: Cannot stat 'gol.txt': No such file or directory"

def test_permission_denied():
    assert cp(['525252.txt', '../root']) == "cp: Permission denied: '525252.txt' -> '../root'"