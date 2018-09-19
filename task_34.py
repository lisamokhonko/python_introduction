#Task #34
#Создать класс Годзилла. При создании Годзиллы указывается объем желудка.
# Написать для данного класса метод поедания людей eat.
# В данный метод должен передаваться объем съеденного человека и соответственно уменьшаться место в желудке.
# Когда Годзилла заполнит желудок на 90%, то Годзилла должен говорить он наелся и больше не может поедать людей.

class Godilla:
    FULLNESS = 0.9
    def __init__(self, stomac_voume):
        self.stomac_voume = stomac_voume
        self.current_volume = 0

    def eat(self, human_volume):
        if (human_volume + self.current_volume) <= self.stomac_voume*self.FULLNESS:
            self.current_volume += human_volume
        else:
            print('Godzilla is full')

godzilla1 = Godilla(100)
godzilla2 = Godilla(10)

godzilla2.eat(30)
godzilla1.eat(30)
godzilla1.eat(30)
godzilla1.eat(30)

print(godzilla1.current_volume)
