class Rational:
    def __init__(self, n: int, d: int) -> None:
        self.num = n
        self.den = d

        self.simplify()

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

        

