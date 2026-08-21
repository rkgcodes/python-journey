

from c4 import hello

def test_default():
    assert hello()=="hello, world"


def test_argument():
    for name in ["Hermione", "Haryy", "Ron"]:
        assert hello(name) == f"hello, {name}"

        