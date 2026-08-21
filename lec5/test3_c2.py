# more unit test using try and except

from c2 import square

def main():
    test_square()

def test_square():
    try:
        assert square(2) == 4
    except AssertionError:
        print("square of 2 was not 4")

    try:
        assert square(3) == 9
    except AssertionError:
        print("square of 3 was not 9")

if __name__ == "__main__":
    main()

