# Fraction
# Create a Fraction class, which will represent all basic arithmetic logic for fractions (+, -, /, *) with appropriate
# checking and error handling

class Fraction:
    def __init__(self, numerator: int, denominator: int) -> None:
        self.numerator = numerator
        self.denominator = denominator

        if self.denominator == 0:
            raise ZeroDivisionError("Cannot divide by zero")

        minimum = abs(self.numerator) if abs(self.numerator) < abs(self.denominator) else abs(self.denominator)

        if minimum > 1:
            for num in range(minimum, 1, -1):
                if self.numerator % num == 0 and self.denominator % num == 0:
                    self.numerator /= num
                    self.denominator /= num
                    break

        if self.numerator < 0 and self.denominator < 0:
            self.numerator = abs(self.numerator)
            self.denominator = abs(self.denominator)

    def __add__(self, other: 'Fraction') -> 'Fraction':
        d = self.denominator * other.denominator
        n = self.numerator * other.denominator + self.denominator * other.numerator
        return Fraction(n, d)

    def __sub__(self, other: 'Fraction') -> 'Fraction':
        d = self.denominator * other.denominator
        n = self.numerator * other.denominator - self.denominator * other.numerator
        return Fraction(n, d)

    def __mul__(self, other: 'Fraction') -> 'Fraction':
        n = self.numerator * other.numerator
        d = self.denominator * other.denominator
        return Fraction(n, d)

    def __truediv__(self, other: 'Fraction') -> 'Fraction':
        n = self.numerator * other.denominator
        d = self.denominator * other.numerator
        return Fraction(n, d)

    def __str__(self) -> str:
        return f"{self.numerator:1.0f} / {self.denominator:1.0f}"

    def __eq__(self, other) -> bool:
        return self.numerator == other.numerator and self.denominator == other.denominator


x = Fraction(1, 2)
y = Fraction(1, 4)

assert x + y == Fraction(3, 4)
assert x * y == Fraction(1, 8)
assert x / y == Fraction(2, 1)
assert x - y == Fraction(1, 4)
assert Fraction(2, 4) == Fraction(1, 2)
assert Fraction(-1, -3) == Fraction(1, 3)



