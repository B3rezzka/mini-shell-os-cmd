import pytest
import sys
import os


project_root = os.path.dirname(os.path.dirname(__file__))  # поднимаемся на 2 уровня вверх
sys.path.insert(0, project_root)


from src.rm_comm import rm


def test_positive():
    assert rm(['52.txt']) == None

def test_cant_remove():
    assert rm(['sooskin']) == "rm: Cannot remove 'sooskin': is a directory (use -r to remove directories)"

def test_dang():
    assert rm(['/']) == "rm: Refusing to remove '/': it is dangerous"