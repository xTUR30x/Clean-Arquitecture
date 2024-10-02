#Example Law of Demeter

#Problem
class Engine:

    def start_engine(self):
        pass


class Car:

    def __init__(self):
        self.engine = Engine()

    def get_engine(self):
        return self.engine


if __name__ == '__main__':

    car = Car()
    car.get_engine().start_engine()


#Solution
class Engine:

    def start_engine(self):
        pass


class Car:

    def __init__(self):
        self.engine = Engine()

    def start(self):
        self.engine.start_engine()

if __name__ == '__main__':

    car = Car()
    car.start()
