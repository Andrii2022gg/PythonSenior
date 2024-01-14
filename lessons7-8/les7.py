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


def degrees(num, max_degrees):
    for i in range(max_degrees):
        yield num ** i

result = degrees(50,10000)

for i in result:
    print(i)