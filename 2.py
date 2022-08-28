class Human:
    default_name = 'no name'
    default_age = 0

    def __init__(self, name=default_name, age=default_age):
        self.name = name
        self.age = age
        self.__money = 0
        self.__house = None

    def info(self):
        print(f'Имя {self.name}')
        print(f'Возраст {self.age}')
        print(f'Денег {self.__money}')
        print(f'Дом {self.__house}')

    @staticmethod
    def default_info():
        print(Human.default_name, Human.default_age)

    def earn_money(self, amount):
        self.__money += amount

    def __make_deal(self, house, price):
        self.__money -= price
        self.__house = house

    def buy_house(self, discount, house):
        pricee = house.final_price(discount)
        if self.__money >= pricee:
            self.__make_deal(house,pricee)
        else:
            print("Not enough money")


class House:
    def __init__(self, area, price):
        self._area = area
        self._price = price

    def final_price(self, discount):
        self.fin_price = self._price - (self._price * (discount // 100))
        return self.fin_price


class SmallHouse(House):
    default_area = 40

    def __init__(self, price):
        super().__init__(SmallHouse.default_area, price)

a1 = SmallHouse(1000)
print(a1._area)

if __name__ == '__main__':
    Human.default_info()
    Vika = Human('Виктория', 17)
    Vika.info()
    Vika.earn_money(100000000000)
    Vika.info()
    villa = SmallHouse(1000000000000000000)
    Vika.buy_house(5, villa)
    Vika.earn_money(100000000000000000000)
    Vika.info()
    Vika.buy_house(5, villa)
    Vika.info()
