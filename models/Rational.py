from typing import Self


class Rational:
    def __init__(self, n: int, d: int) -> None:
        self.num = n
        self.den = d

        self.simplify()

    def __eq__(self, other: Self) -> bool:
        if not isinstance(other, self.__class__):
            raise NotImplementedError

        return self.num == other.num and self.den == other.den

    def simplify(self) -> None:
        if self.den < 0:
            self.num *= -1
            self.den *= -1

        a, b = abs(self.num), self.den
        while a != b:
            if a > b:
                a -= b
            else:
                b -= a
        
        self.num //= a
        self.den //= b

