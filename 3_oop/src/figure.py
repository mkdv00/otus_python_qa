class Figure:
    
    def __init__(self, side, name: None) -> None:
        if self.__class__ == Figure:
            raise Exception('Can not instantiate abstract base class.')
        
        self.side = side
        self.name = name
        
    @property
    def area(self) -> int:
        pass
    
    @property
    def perimeter(self) -> int:
        pass
    
    def add_area(self, figure):
        if not isinstance(figure, Figure):
            raise ValueError('Receive an incorrect class.')
        return self.area + figure.area
