from src.rectangle import RectAngle


class TestRectangle:
    
    def test_create_rectangle(self):
        rectangle = RectAngle(4, 5)
        
        assert isinstance(rectangle, RectAngle), "This is not an instance RectAngle class"
        assert rectangle.name == 'Rectangle', f"Wrong name {rectangle.name}"
        assert rectangle.a == 4, f"Wrong a - {rectangle.a}"
        assert rectangle.b == 5, f"Wrong b - {rectangle.b}"

    def test_rectangle_perimeter(self):
        rectangle = RectAngle(4, 5)
        assert rectangle.perimeter == 18, f"Wrong perimeter {rectangle.perimeter}"
        
    def test_rectangle_area(self):
        rectangle = RectAngle(4, 5)
        assert rectangle.area == 20, f"Wrong area {rectangle.area}"
        
    def test_add_area_to_rectangle(self):
        rectangle_one = RectAngle(4, 5)
        rectangle_two = RectAngle(5, 4)
        area_of_two_rectangles = rectangle_one.add_area(rectangle_two)
        assert area_of_two_rectangles == 40, f"Wrong area of two rectangle - {area_of_two_rectangles}"
