import unittest


while True:
    print("1. Run Test Addition")
    print("2. Run Test Subtraction")
    print("3. Run Test Multiplication")
    print("4. Run Test Division")
    print("5. Run Test Square")
    print("6. Run Test Square Root")
    print("7. Run String Test")

    choice = int(input("Enter choice from above: "))

    if choice == 1:
        from addition import MyAdditionTestCase
        MyAdditionTestCase()
        if __name__ == '__main__':
            unittest.main()

    elif choice == 2:
        from subtraction import MySubtractionTestCase
        MySubtractionTestCase()
        if __name__ == '__main__':
            unittest.main()

    elif choice == 3:
        from multiplication import MyMultiplicationTestCase
        MyMultiplicationTestCase()
        if __name__ == '__main__':
            unittest.main()

    elif choice == 4:
        from division import MyDivisionTestCase
        MyDivisionTestCase()
        if __name__ == '__main__':
            unittest.main()

    elif choice == 5:
        from square import MySquareTestCase
        MySquareTestCase()
        if __name__ == '__main__':
            unittest.main()

    elif choice == 6:
        from squareroot import MySquarerootTestCase
        MySquarerootTestCase()
        if __name__ == '__main__':
            unittest.main()

    elif choice == 7:
        from stringmultiply import MyStringMultiplicationTestCase
        MyStringMultiplicationTestCase()
        if __name__ == '__main__':
            unittest.main()

    else:
       print ("Try again")

    continue


