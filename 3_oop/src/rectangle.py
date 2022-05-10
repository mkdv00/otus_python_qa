from src.figure import Figure


class RectAngle(Figure):
    
    def __init__(self, a, b, name='Rectangle') -> None:
        super().__init__(a, name)
        self.a = a
        self.b = b
        
    @property
    def perimeter(self) -> int:
        return 2 * (self.a + self.b)
    
    @property
    def area(self) -> int:
        return self.a * self.b
