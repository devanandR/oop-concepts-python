class Bird:
    def fly(self):
        print("Flying in the sky")

class Airplane:
    def fly(self):
        print("Flying with fuel")

def let_it_fly(flyable):
    flyable.fly()

if __name__ == "__main__":
    for obj in (Bird(), Airplane()):
        let_it_fly(obj)
