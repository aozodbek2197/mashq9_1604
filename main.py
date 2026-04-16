# 1-mashq
class Meta(type):
    def __new__(cls, name, bases, dct):
        dct["id"] = 1
        return super().__new__(cls, name, bases, dct)

class User(metaclass=Meta):
    pass

u = User()
print(u.id)
# 2-mashq
class Data:
    def __init__(self):
        self._data = None

    @property
    def data(self):
        if self._data is None:
            print("Loading...")
            self._data = [1,2,3]
        return self._data
# 3-mashq
class Builder:
    def __init__(self):
        self.value = 0

    def add(self, x):
        self.value += x
        return self

    def mul(self, x):
        self.value *= x
        return self

b = Builder().add(2).mul(3)
print(b.value)
# 4-mashq
class StrategyA:
    def execute(self):
        print("A ishladi")

class StrategyB:
    def execute(self):
        print("B ishladi")

class Context:
    def __init__(self, strategy):
        self.strategy = strategy

    def run(self):
        self.strategy.execute()
# 5-mashq
class Light:
    def on(self):
        print("Yondi")

class Command:
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.on()
