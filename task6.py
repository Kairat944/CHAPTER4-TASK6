#  Тип домохозяйства, общая площадь и список названий мебели.
# В новом доме мебели нет вообще.
# 2. Мебель имеет название и площадь, из которых кровать: 4 кв. Метра. Шкаф: 2 кв. Метра. Стол:
# 1,5 квадратных метра
# 3. Добавьте три вышеупомянутых предмета мебели в дом
# 4. При печати дома требуется вывод: тип домашнего хозяйства, общая площадь, остальная площадь,
# список наименований мебели.
#
class Home:
    """ Простая модель дома """
    def __init__(self, household_type, total_area, furniture):
        self.household_type = household_type
        self.total_area = total_area
        self.furniture = furniture
        self.remaining_area_reading()                 # 1) Автозапуск  2) Атрибут класса Home

    """ Площадь не занимаемая мебелью """
    def remaining_area_reading(self):
        furniture_area = 0
        for value in self.furniture.values():
            furniture_area += value
        self.remaining_area = self.total_area - furniture_area

    """ Вывод всей информации о доме """
    def print_home(self):
        print(f"Household type: \n\t\t\t{self.household_type.upper()}"
              f"\nTotal area: \n\t\t\t{self.total_area} кв.м"
              f"\nRemaining area: \n\t\t\t{self.remaining_area} кв.м"
              f"\nFurniture name list: "
              )
        for k, v in self.furniture.items():
            print(f"\t\t\t{k.title()} - {v} кв.м")


dom = Home("elite", 70, {"bed": 4, "wardrobe": 2, "table": 1.5})
dom.print_home()
