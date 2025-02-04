from src.math_operations import add,sub

def test_add():
    assert add(2,5) == 7
    assert add(5,5) == 10
    assert add(8,7) == 15
    assert add(1,7) == 8

def test_sub():
    assert sub(5,5) == 0
    assert sub(1,1) == 0
    assert sub(8,7) == 1
    assert sub(10,7) == 3