# iteratos

car_lisr = ["tesla", "bmw", "audi"]

for i in car_lisr:
    if i == "bmw":
        print(i.upper())
    else:
        print(i)

print("=========== next ============")

iterator = iter(car_lisr)
print(next(iterator))
print(next(iterator))
print(next(iterator))

print("=========== iter ============")
for it in iterator:
    print(it)


class Counter:
    def __init__(self, max_number):
        self.i = 0
        self.max_number = max_number

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        self.i += 1
        if self.i > self.max_number:
            raise StopIteration
        return self.i


count = Counter(10)

# for item in count:
#     print(item)
print(next(count))
print(count.__next__())

print("============ Generators ============")


def degrees(num, max_degrees):
    # for i in range(max_degrees):
    #     yield num ** i
    i = 0
    while True:
        result = num ** i
        yield result
        if result > 100 ** 20:
            return
        i += 1


result = degrees(1000, 50)

print(type(result))

for i in result:
    print(i)

print("============ Замикання ============")


class Helper:
    def __init__(self, work):
        self.work = work

    def __call__(self, work):
        return "I will help you with your " + self.work \
            + ". Afterwords i will help you with " + work


helper = Helper("classwork")

print(helper("homework"))


def helper(work):
    self_work = work

    def helper(work):
        return "I will help you with your " + self_work \
            + ". Afterwords i will help you with " + work

    return helper


helper = helper("teacher_work")
print(helper("student_work"))
print(helper("doctor_work"))