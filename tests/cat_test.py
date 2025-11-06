import pytest
import sys
import os


project_root = os.path.dirname(os.path.dirname(__file__))  # поднимаемся на 2 уровня вверх
sys.path.insert(0, project_root)


from src.cd_comm import cat


def test_positive():
    assert cat(['../525252.txt']) == None

def test_no_file_operand():
    assert cat([]) == "cat: Missing file operand"

def test_is_directory():
    assert cat(['../sooskin']) == "cat: ../sooskin: Is a directory"

def test_no_file_directory():
    assert cat(['../gol']) == "cat: ../gol: No such file or directory"