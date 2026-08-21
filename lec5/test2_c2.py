#test the c2 using assert and introduction of AssertionError

from c2 import square

def main():
    test_square()

def test_square():
    assert square(2) == 4
    assert square(3) == 9


if __name__ == "__main__":
    main()
        