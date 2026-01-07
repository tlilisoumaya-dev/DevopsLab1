import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import add

def test_add():
    assert add(7, 3) == 5
    
