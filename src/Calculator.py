from CsvReader import CsvReader
import math

def addition(a, b):
    a = float(a)
    b = float(b)
    c = a + b
    return c

def subtraction(a, b):
    a = float(a)
    b = float(b)
    c = b - a
    return c

def multiplication(a, b):
    a = float(a)
    b = float(b)
    c = a * b
    return c

def division(a, b):
    a = float(a)
    b = float(b)
    c = round(a / b, 9)
    return c

def square(a):
    a = float(a)
    c = a ** 2
    return c

def squarert(a):
    a = float(a)
    b = math.sqrt(a)
    c = float(b)
    return c

def stringmultiplication(a, b):
    a = str(a)
    b = int(b)
    c = (a * b)
    return c

def mean(data):
    mean = data
    return mean


class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = addition(a, b)
        return self.result

    def subtract(self, a, b):
        self.result = subtraction(a, b)
        return self.result

    def multiply(self, a, b):
        self.result = multiplication(a, b)
        return self.result

    def divide(self, a, b):
        self.result = division(a, b)
        return self.result

    def square(self, a):
        self.result = square(a)
        return self.result

    def sqrt(self, a):
        self.result = squarert(a)
        return self.result

    def stringmultiply(self, a, b):
        self.result = stringmultiplication(a, b)
        return self.result

class CSVStats(Calculator):
    data = []

    def __init__(self, data_file):
        self.data = CsvReader(data_file)
        pass

    def mean(self):
        mean(self.data)