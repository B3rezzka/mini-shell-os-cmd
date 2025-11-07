import pytest
import sys
import os


project_root = os.path.dirname(os.path.dirname(__file__))  # поднимаемся на 2 уровня вверх
sys.path.insert(0, project_root)


from src.mv_comm import mv


def test_positive():
    assert mv(['72.txt', 'fortests']) == None

def test_missing_operand():
    assert mv(['lol']) ==  "mv: missing file operand"

def test_dang():
    assert mv(['/root', 'sooskin']) == "mv: Permission denied to access '/root'"