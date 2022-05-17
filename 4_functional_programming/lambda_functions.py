from operator import le
from unicodedata import name


names = ["Геннадий Букин", "Тип Эпл", "Аркадий Волож", "Билл Гейтс", "Илон Маск", "Игорь Николаев", 
         "Джеф Безос", "Майк Тайсон", "Николас Яковидис"]

sorted_names = sorted(names, key=lambda name: name.split(" ")[1][0])
print(sorted_names)
