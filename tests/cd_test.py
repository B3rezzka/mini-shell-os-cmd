import pytest
import sys
import os


project_root = os.path.dirname(os.path.dirname(__file__))  # поднимаемся на 2 уровня вверх
sys.path.insert(0, project_root)


from src.cd_comm import cd


def test_positive():
    assert cd(['cd']) == None

def test_no_directory():
    assert cd(['cd', 'lol']) == "cd: No such directory: lol"

def test_perm_denied():
    assert cd(['cd', '/root']) == "cd: Permission denied: /root"