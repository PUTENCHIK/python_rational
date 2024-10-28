from typing import Self


class Rational:
    def __init__(self, n: int, d: int) -> None:
        self.num = n
        self.den = d

    def __eq__(self, other: Self) -> bool:
        if not isinstance(other, self.__class__):
            raise NotImplementedError

        return self.num == other.num and self.den == other.den        

