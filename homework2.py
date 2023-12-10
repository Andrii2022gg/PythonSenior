import random


class Student:
    def __init__(self):
        super().__init__()
        self.name = "John"
        self.age = 17
        self.day_of_live = 365
        self.weight = 75.44
        self.height = 180
        self.money = 100
        self.current_job = ""
        self.need_job = 0

        self.system = {
            "day_of_live": 10,
            "enable_school": 1,
            "enable_job": 1,
            "out_data_every_day": 1,
            "out_data_to_and_after": 1
        }

        self.marks = {
            "PE": 12,
            "English": 12,
            "Math": 12,
            "Ukraine": 12,
            "Since": 12,
        }

        self.jobs = {
            "Courier": {
                "PAY": [15, 80],
                "FREE": 25
            },
            "Cleaner": {
                "PAY": [50, 150],
                "FREE": 15
            },
            "Janitor": {
                "PAY": [10, 50],
                "FREE": 10
            },
        }

    def steady(self):
        for i in self.marks:
            if self.marks[i] > 2:
                self.marks[i] -= random.randint(0, 2)
            if self.marks[i] < 9 and self.money > 80:
                self.marks[i] += random.randint(0, 12 - self.marks[i])
                self.money -= random.randint(10, 50)
    def work(self):

        if self.money < 100:
            self.need_job = 1

        if self.money > 1500:
            self.need_job = 0
            self.current_job = ""

        # RANDOMIZE JOBS COUNT
        for i in self.jobs:
            if self.jobs[i]["FREE"] <= 0:
                self.jobs[i]["FREE"] += 8
                continue
            else:
                self.jobs[i]["FREE"] += random.randint(-8, 4)
                if self.jobs[i]["FREE"] <= 0:
                    self.jobs[i]["FREE"] = 0

        # GET JOB
        if self.need_job == 1 and self.current_job == "":
            job_num = random.randint(0, 2)
            jobs_buf = list(self.jobs.keys())
            if self.jobs[jobs_buf[job_num]]["FREE"] > 0:
                self.jobs[jobs_buf[job_num]]["FREE"] = self.jobs[jobs_buf[job_num]]["FREE"] - 1
                self.current_job = jobs_buf[job_num]
        # JOB
        if self.current_job != "":
            self.money += random.randint(self.jobs[self.current_job]["PAY"][0], self.jobs[self.current_job]["PAY"][1])
    def live(self):
        if self.system["out_data_to_and_after"] == 1:
            print(
                f"TO LIVE\n\n\n"
                f"MAIN DATA \n\n"
                f"NAME: {self.name} \n"
                f"AGE: {self.age} \n"
                f"DAY OF LIVE: {self.day_of_live} \n"
                f"WEIGHT: {self.weight} \n"
                f"HEIGHT: {self.height} \n"
                f"MONEY: {self.money} \n"
                f"CURRENT JOB: {self.current_job} \n"
                f"NEED JOB: {self.need_job} \n\n"
                f"MARKS DATA: \n\n {self.marks} \n\n"
                f"JOBS DATA: \n\n {self.jobs} \n\n"
                f"SYSTEM DATA: \n\n {self.system} \n\n"
            )

        for i in range(self.system["day_of_live"]):
            age = int(self.age + ((i + 1) / 365))
            if self.system["enable_school"] == 1:
                student.steady()
            if self.system["enable_job"] == 1:
                student.work()

            if self.system["out_data_every_day"] == 1:
                print(
                    f"LIVE OF DAY: {i+1}\n\n\n"
                    f"MAIN DATA \n\n"
                    f"NAME: {self.name} \n"
                    f"AGE: {self.age} \n"
                    f"DAY OF LIVE: {self.day_of_live} \n"
                    f"WEIGHT: {self.weight} \n"
                    f"HEIGHT: {self.height} \n"
                    f"MONEY: {self.money} \n"
                    f"CURRENT JOB: {self.current_job} \n"
                    f"NEED JOB: {self.need_job} \n\n"
                    f"MARKS DATA: \n\n {self.marks} \n\n"
                    f"JOBS DATA: \n\n {self.jobs} \n\n"
                    f"SYSTEM DATA: \n\n {self.system} \n\n"
                )

        if self.system["out_data_to_and_after"] == 1:
            print(
                f"AFTER LIVE\n\n\n"
                f"MAIN DATA \n\n"
                f"NAME: {self.name} \n"
                f"AGE: {self.age} \n"
                f"DAY OF LIVE: {self.day_of_live} \n"
                f"WEIGHT: {self.weight} \n"
                f"HEIGHT: {self.height} \n"
                f"MONEY: {self.money} \n"
                f"CURRENT JOB: {self.current_job} \n"
                f"NEED JOB: {self.need_job} \n\n"
                f"MARKS DATA: \n\n {self.marks} \n\n"
                f"JOBS DATA: \n\n {self.jobs} \n\n"
                f"SYSTEM DATA: \n\n {self.system} \n\n"
            )




student = Student()
student.live()
