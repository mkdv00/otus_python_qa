from src.circle import Circle


class TestCircle:
    
    def test_create_circle(self):
        circle = Circle(7)
        
        assert isinstance(circle, Circle), "This is not an instance Circle class"
        assert circle.name == 'Circle', f"Wrong name {circle.name}"
        assert circle.radius == 7, f"Wrong radius's circle {circle.radius}"

    def test_circle_perimeter(self):
        circle = Circle(7)
        assert circle.perimeter == 43.982297150257104, f"Wrong perimeter {circle.perimeter}"
        
    def test_circle_area(self):
        circle = Circle(7)
        assert circle.area == 153.93804002589985, f"Wrong area {circle.area}"
        
    def test_add_area_to_circle(self):
        circle_one = Circle(5)
        circle_two = Circle(7)
        area_of_two_circles = circle_one.add_area(circle_two)
        assert area_of_two_circles == 232.4778563656447, f"Wrong area of two figures {area_of_two_circles}"
