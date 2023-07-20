class Animals:
    def __init__(self, eat, sleep):
        self.food = eat
        self.sleeping = sleep

    def eat(self):
        print("Eating:", self.food)

    def sleep(self):
        print("Sleeping:", self.sleeping)


class Dog(Animals):
    def sound(self):
        print("Woof")


class Monkey(Animals):
    def jump(self):
        print("Jumping")

    def run(self):
        print("running")


class Cat(Animals):

    def chill(self):
        print("cat chill under the son")

    def drink(self):
        print("drink milk")


class Chiken(Animals):

    def egs(self):
        print("do Egs")


class Birdie(Animals):

    def fly(self):
        print("Fly")

    def fall(self):
        print("fallaway")


class Human:
    def __init__(self, eat, study, working):
        self.eat_value = eat
        self.study_value = study
        self.working_value = working

    def eat(self):
        print("Human eating:", self.eat_value)

    def study(self):
        print("Human studying:", self.study_value)

    def work(self):
        print("Human working:", self.working_value)


class Centaur(Animals, Human):
    def talk(self):
        print("Centaur talk")

    def shoot(self):
        print("Centaur shoot with a crossbow")


dog1 = Dog("bones", "10 hours")
dog1.eat()
dog1.sleep()
dog1.sound()
monk = Monkey("banan", "3 Hour")
monk.eat()
monk.sleep()
monk.jump()
monk.run()
cat = Cat("buff", "10 hour")
cat.chill()
cat.eat()
cat.sleep()
cat.drink()
chik = Chiken("rice", "2 hour")
chik.eat()
chik.sleep()
chik.egs()
Bird = Birdie("apple", "3 hour")
Bird.sleep()
Bird.eat()
Bird.fall()
Bird.fly()

human1 = Human("Pizza", "Math", "Office")
human1.eat()
human1.study()
human1.work()

centaur1 = Centaur("beef", "12 hour")
centaur1.eat()
centaur1.sleep()
centaur1.shoot()
centaur1.talk()