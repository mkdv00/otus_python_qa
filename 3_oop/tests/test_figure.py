import pytest 

from src.figure import Figure
from src.rectangle import RectAngle


class TestFigure:
    
    def test_create_instance_figure(self):
        with pytest.raises(Exception):
            Figure(2)
            
    def test_add_area_to_not_figure(self):
        rectangle = RectAngle(4, 5)
        not_figure = 0
        
        with pytest.raises(ValueError):
            rectangle.add_area(not_figure)
