import random
import logging
import time

def time_decor(func):
    def timing(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        logging.debug(f"Function time '{func.__name__}': {elapsed_time:.10f} seconds")
        return result
    return timing
class Human:
    @time_decor
    def __init__(self, name="Human", job=None, home=None, car=None):
        self.name = name
        self.money = 100
        self.gladness = 50
        self.satiety = 50
        self.job = job
        self.car = car
        self.home = home

        self.childs = []

    @time_decor
    def get_home(self):
        self.home = House()

    @time_decor
    def get_car(self):
        self.car = Auto(brands_of_car)

    @time_decor
    def get_job(self):

        if self.car.drive():
            pass
        else:
            self.to_repair()
            return
        self.job = Job(job_list)

    @time_decor
    def eat(self):
        if self.home.food < 20:
            self.shopping("food")
        else:
            if self.satiety >= 100:
                self.satiety = 100

        self.satiety += 10
        self.home.food -= 5

    @time_decor
    def work(self):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                self.shopping("fuel")
                return
            else:
                self.to_repair()
                return
        self.money += self.job.salary
        self.gladness -= self.job.gladness_less
        self.satiety -= 15

    @time_decor
    def shopping(self, manage):

        if self.home.food <= 30:
            logging.debug("Bought food")
            self.money -= 50
            self.home.food += 50

        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                manage = "fuel"
            else:
                self.to_repair()
            return
        if manage == "fuel":
            logging.info("I bought fuel")
            self.money -= 100
            self.car.fuel += 100
        elif manage == "food":
            logging.info("Bought food")
            self.money -= 50
            self.home.food += 50
        elif manage == "delicacies":
            logging.info("Hooray! Delicious!")
            self.gladness += 10
            self.satiety += 2
            self.money -= 15

    @time_decor
    def chill(self):
        self.gladness += 30
        self.home.mess += 5

    @time_decor
    def clean_home(self):
        self.gladness -= 15
        self.home.mess = 0

    @time_decor
    def to_repair(self):
        self.car.strength += 100
        self.money -= 50

    @time_decor
    def days_indexes(self, day):
        day = f" Today the {day} of{self.name}'s life "
        logging.info(f"{day:=^50}")
        human_indexes = self.name + "'s indexes"
        logging.info(f"{human_indexes:^50}")
        logging.info(f"Money = {self.money}")
        logging.info(f"Satiety = {self.satiety}")
        logging.info(f"Gladness = {self.gladness}")
        home_indexes = "Home indexes"
        logging.info(f"{home_indexes:^50}")
        logging.info(f"Food = {self.home.food}")
        logging.info(f"Mess = {self.home.mess}")
        car_indexes = f"{self.car.brand} car indexes"
        logging.info(f"{car_indexes:^50}")
        logging.info(f"Fuel = {self.car.fuel}")
        logging.info(f"Strength = {self.car.strength}")

        logging.info(f"Live childrens: ")
        for i in self.childs:
            logging.info(i.status())

    @time_decor
    def is_alive(self):
        if self.gladness < 0:
            logging.debug("Depression…")
            return False
        if self.satiety < 0:
            logging.debug("Dead…")
            return False
        if self.money < -500:
            logging.debug("Bankrupt…")
            return False

    @time_decor
    def live(self, day):
        if self.is_alive() == False:
            return False
        if self.home is None:
            logging.debug("Settled in the house")
            self.get_home()
        if self.car is None:
            self.get_car()
            logging.debug(f"I bought a car{self.car.brand}")
        if self.job is None:
            self.get_job()
            logging.debug(f"I don't have a job, going to get a job {self.job.job} with salary {self.job.salary}")
        self.days_indexes(day)

        dice = random.randint(1, 4)
        if self.satiety < 20:
            logging.info("I'll go eat")
            self.eat()
        elif self.gladness < 20:
            if self.home.mess > 15:
                logging.info("I want to chill, but there is so much mess…\n So I will clean the house ")
                self.clean_home()
            else:
                logging.info("Let`s chill!")
                self.chill()
        if self.money < 100:
            logging.info("Start working")
            self.work()
        if self.car.strength < 10:
            logging.info("I need to repair my car")
            self.to_repair()
        if dice == 1:
            logging.info("Let`s chill!")
            self.chill()
        if dice == 2:
            logging.info("Start working")
            self.work()
        if dice == 3:
            logging.info("Cleaning time!")
            self.clean_home()
        if dice == 4:
            logging.info("Time for treats!")
            self.shopping(manage="delicacies")

        self.childs_live()

    @time_decor
    def add_child(self, *_child):
        for __child in _child:
            self.childs.append(__child)

    @time_decor
    def childs_live(self):
        for child in self.childs:
            child.eat()
            child.cheal_child()
            child.stady()
            if child.child_is_alive() == False:
                logging.info(f"Child: '{child.name}' death")
                self.childs.remove(child)


class Auto:
    @time_decor
    def __init__(self, brand_list):

        self.brand = random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]["fuel"]
        self.strength = brand_list[self.brand]["strength"]
        self.consumption = brand_list[self.brand]["consumption"]

    @time_decor
    def drive(self):
        if self.strength > 10 and self.fuel >= 20:
            self.fuel -= round(self.consumption / 3)
            self.strength -= 1
            return True
        else:
            logging.debug("The car cannot move")
            return False


class House:
    @time_decor
    def __init__(self):
        self.mess = 0
        self.food = 0


job_list = {
    "Java developer":
        {"salary": 500, "gladness_less": 15},
    "Python developer":
        {"salary": 400, "gladness_less": 10},
    "C++ developer":
        {"salary": 800, "gladness_less": 25},
    "Rust developer":
        {"salary": 350, "gladness_less": 1},
}

brands_of_car = {
    "BMW": {"fuel": 100, "strength": 100,
            "consumption": 6},
    "Lada": {"fuel": 50, "strength": 40,
             "consumption": 10},
    "Volvo": {"fuel": 70, "strength": 150,
              "consumption": 8},
    "Ferrari": {"fuel": 80, "strength": 120,
                "consumption": 14},
}


class Job:
    @time_decor
    def __init__(self, job_list):
        self.job = random.choice(list(job_list))
        self.salary = job_list[self.job]["salary"]
        self.gladness_less = job_list[self.job]["gladness_less"]


class Children:
    @time_decor
    def __init__(self, _name, _parent, _age):
        self.name = _name
        self.parent = _parent
        self.home = self.parent.home
        self.age = _age

        self.gladness = 50
        self.satiety = 50

        self.marks = {
            "PE": 12,
            "English": 12,
            "Math": 12,
            "Ukraine": 12,
            "Since": 12,
        }

    @time_decor
    def stady(self):
        for i in self.marks:
            if self.marks[i] > 2:
                self.marks[i] -= random.randint(0, 1)
            if self.marks[i] < 9 and self.parent.money > 150:
                self.marks[i] += random.randint(0, 12 - self.marks[i])
                self.parent.money -= random.randint(1, 10)
                self.gladness -= 1
                self.satiety -= 0.1

    @time_decor
    def cheal_child(self):
        self.gladness -= random.randint(0, 5)
        if self.gladness < 80:
            self.parent.home.mess += 10
            self.gladness += 15

    @time_decor
    def eat(self):
        if self.satiety < 20:
            if self.parent.home.food <= 10:
                self.parent.shopping("food")
            self.satiety += 10
            self.parent.home.food -= round(self.age * 1.1)

    @time_decor
    def child_is_alive(self):
        if self.satiety <= 0:
            logging.debug("Child death (satiety)")
            return False
        if self.gladness <= 0:
            logging.debug("Child depresed (gladness)")
            return False
        if self.parent.money < -500:
            logging.debug("Bankrupt parent…")
            logging.debug("Child haven`t parent (money = -500)")
            return False

    @time_decor
    def status(self):
        logging.debug("Child status")
        logging.info(f"    Name: {self.name}")
        logging.info(f"    Age: {self.age}")
        logging.info(f"    Marks: {self.marks}")
        logging.info(f"    Parent name: {self.parent.name}")

        logging.info(f"    Gladness: {self.gladness}")
        logging.info(f"    Satiety: {self.satiety}")


logging.basicConfig(level=logging.DEBUG,
                    filename="logs.log",
                    filemode="w",
                    format="My logging: %(levelname)s: %(asctime)s: %(message)s")
@time_decor
def main():

    nick = Human(name="Nick")

    child_Alice = Children("Alice", nick, 12)
    child_John = Children("John", nick, 12)

    nick.add_child(child_Alice, child_John)

    days_of_live = 365 * 5

    for day in range(days_of_live):
        if nick.live(day) == False:
            break

    nick.days_indexes(days_of_live)

if __name__ == "__main__":
    main()