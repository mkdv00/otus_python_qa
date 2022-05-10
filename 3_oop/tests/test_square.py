from src.square import Square


class TestSquare:
    
    def test_create_square(self):
        square = Square(5)
        
        assert isinstance(square, Square), f"This is not an instance Square class"
        assert square.name == 'Square', f"Wrong name {square.name}"
        assert square.a == 5, f"Wrong a - {square.a}"
        assert square.b == 5, f"Wrong b - {square.b}"
        
    def test_square_perimeter(self):
        square = Square(5)
        assert square.perimeter == 20, f"Wrong perimeter {square.perimeter}"
        
    def test_square_area(self):
        square = Square(5)
        assert square.area == 25, f"Wrong area {square.area}"
        
    def test_add_area_to_square(self):
        square_one = Square(5)
        square_two = Square(5)
        area_of_two_squares = square_one.add_area(square_two)
        assert area_of_two_squares == 50, f"Wrong area of two squares {area_of_two_squares}"
