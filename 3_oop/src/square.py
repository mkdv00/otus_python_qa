from src.rectangle import RectAngle 


class Square(RectAngle):
    
    def __init__(self, a, name='Square'):
        super().__init__(a, a, name)
