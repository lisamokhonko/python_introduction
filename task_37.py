#Task #37
#Реализовать магазин, который продает 3 вида товара. Программа должна показывать,
# сколько осталось в магазине каждого товара и
# какова прибыль на текущий момент продавца по каждому товару и всего (Прибыль = доход - себестоимость товара).
class Shop:
    pass

class Ware:
    def __init__(self, name, price, cost, begin_of_day):
        self.name = name                #title of the ware
        self.price = price              #price per 1 item
        self.cost = cost                #prime cost (net cost)
        self.begin_of_day = begin_of_day #how many wares were at the beginning of the day
        self.current_qty = begin_of_day  #how many wares were left after some time

    def sel_item(self, qty_to_sell):
        if (self.current_qty - qty_to_sell) >= 0:
            self.current_qty -= qty_to_sell
            print(qty_to_sell, 'ware(s) was sold')
        else:
            print('There is no enough %s in the shop to sell' % self.name)

    def calculate_profit_and_remains(self):
        profit = (self.price - self.cost)*(self.begin_of_day - self.current_qty)
        print('%s:\n\tCurrent profit is %.2f\n\tCurrent remains is %d items' % (self.name, profit, self.current_qty))


ware1 = Ware(
    name='Toothpaste',
    price=65,
    cost=50,
    begin_of_day=35
)
ware2 = Ware(
    name='Shampoo',
    price=90,
    cost=70,
    begin_of_day=20
)
ware3 = Ware(
    name='Soap',
    price=10,
    cost=5,
    begin_of_day=50
)

ware1.sel_item(15)
ware2.sel_item(10)
ware3.sel_item(25)
ware2.sel_item(15)
ware1.calculate_profit_and_remains()
ware2.calculate_profit_and_remains()
ware3.calculate_profit_and_remains()