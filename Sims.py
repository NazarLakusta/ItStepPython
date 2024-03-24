from random import *


class Human:
    def __init__(self, name, job=None, home=None, car=None):
        self.name = name
        self.money = 100
        self.gladness = 50
        self.satiety = 50
        self.job = job
        self.car = car
        self.home = home

    def get_home(self):
        self.home = House()

    def get_car(self):
        self.car = Auto(list_of_cars)

    def get_job(self):
        if self.car.drive():
            pass
        else:
            self.to_repair()
            return

        self.job = Job(list_of_jobs)

    def chill(self):
        self.gladness += 10
        self.home.mess += 5

    def clean_home(self):
        self.home.mess = 0
        self.gladness -= 5

    def to_repair(self):
        self.car.hp += 100
        self.money -= 50

    def get_shopping(self, message):
        if self.car.drive():
            pass

        else:
            if self.car.fuel < 20:
                message = "fuel"

            else:
                self.to_repair()
                return

        if message == "fuel":
            print("I bought fuel")
            self.money -= 100
            self.car.fuel += 100

        elif message == "food":
            print("Bought food")
            self.money -= 50
            self.home.food += 50
            self.gladness += 1

        elif message == "delicies":
            print("Hoorayy!!! Delicious!!!!!!! ")
            self.gladness += 10
            self.satiety += 2
            self.money -= 15

    def eat(self):
        if self.home.food <= 0:
            self.get_shopping("food")
        else:
            self.satiety += 5
            self.home.food -= 5

    def work(self):
         if self.car.drive():
             pass
         else:
             if self.car.fuel < 20:
                 self.get_shopping("fuel")
             else:
                 self.to_repair()
                 return

         self.money += self.job.salary  # Corrected from self.job.sallary to self.job.salary
         self.gladness -= self.job.gladness_less
         self.satiety -= 5


    def days_index(self, day):
        print(f"Today the {day} of {self.name}'s live")

        print("====Human parameters====")
        print(f"Money - {self.money}")
        print(f"Satiety - {self.satiety}")
        print(f"Gladness - {self.gladness}")
        print()

        print("====House parameters====")
        print(f"Mess - {self.home.mess}")
        print(f"Food - {self.home.food}")
        print()

        print("====Car parameters====")
        print(f"Car - {self.car.brand} ")
        print(f"Fuel - {self.car.fuel}")
        print(f"Strength - {self.car.hp}")






    def is_alive(self):
        if self.gladness<0:
            print("Depression")
            return False

        if self.satiety<0:
            print("Dead")
            return False

        if self.money<-500:
            print("Bankrupt")
            return False

    def live(self, day):
        if self.is_alive() == False:
            return False

        if self.home is None:
            print("Settled in the house")
            self.get_home()

        if self.car is None:
            self.get_car()
            print(f"I bought a car {self.car.brand}")

        if self.job is None:
            self.get_job()
            print(f"I don't have a job, going to get a job {self.job.job}, with salary"
                  f"{self.job.salary}")


        self.days_index(day)

        dice = randint(1,4)

        if self.satiety < 20:
            print("I'll go eat")
            self.eat()

        elif self.gladness < 20:
            if self.home.mess > 15:
                print("Go to clean home!!!!! ")
                self.clean_home()

            else:
                print("LEts go to chilll")
                self.chill()

        elif self.money < 0:
            print("Start working")
            self.work()

        elif self.car.hp < 15:
            print("I need to repair my car")
            self.to_repair()


        elif dice == 1:
            print("Let's chil")
            self.chill()

        elif dice == 2:
            print("Start working")
            self.work()

        elif dice == 3:
            print("Cleaning time")
            self.clean_home()

        elif dice == 4:
            print("Time for teats")
            self.get_shopping("delicacies")


class Auto:
    def __init__(self, list_of_cars):
        self.brand = choice(list(list_of_cars.keys()))  # Get a random brand from the keys
        car_data = list_of_cars[self.brand]  # Get the corresponding data for that brand
        self.fuel = car_data["fuel"]
        self.consumption = car_data["consumption"]
        self.hp = car_data["hp"]

    def drive(self):
        if self.fuel >= self.consumption and self.hp > 0:
            self.fuel -= self.consumption
            self.hp -= 1
            return True
        else:
            print("The car cannot move")
            return False


class Job:
    def __init__(self, list_of_jobs):
        self.job = choice(list(list_of_jobs.keys()))  # Get a random job from the keys
        job_data = list_of_jobs[self.job]  # Get the corresponding data for that job
        self.salary = job_data["salary"]  # Corrected typo from "sallary" to "salary"
        self.gladness_less = job_data["gladness_less"]



class House:
    def __init__(self):
        self.mess = 0
        self.food = 0


list_of_cars = {"BMW": {"fuel": 100, "hp": 100, "consumption": 6},
                "Lada": {"fuel": 30, "hp": 20, "consumption": 5},
                "Mercedes": {"fuel": 70, "hp": 80, "consumption": 10}}

list_of_jobs = {"Python developer": {"salary": 50, "gladness_less": 10},
                "Teacher ItStep": {"salary": 200, "gladness_less": 1},
                "Photoshop designe": {"salary": 100, "gladness_less": 5}}



Sasha = Human("Sasha Didenko")

for day in range(1,8):
    if Sasha.live(day) == False:
        break

print("Game Over")
