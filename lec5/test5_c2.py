# test a function with one function via pytest

from c2 import square

def test_sqaure():
    assert square(2)== 4
    assert square(3)== 9
    assert square(-2)== 4
    assert square(-3)== 9
    assert square(0)== 0