import os


class Shuffler:
    def __init__(self):
        self.__secret_key = 53146697128739435

    def encrypt(self, original):
        os.system('cls')
        print(original * self.__secret_key)

    def decrypt(self, encrypted):
        os.system('cls')
        print(encrypted / self.__secret_key)


shuffler = Shuffler()

while True:
    print("0 == Exit\n1 == encrypt\n2 == decrypt")
    buffer = int(input("Select command: "))
    match buffer:
        case 0:
            break
        case 1:
            shuffler.encrypt(int(input("Input number: ")))
        case 2:
            shuffler.decrypt(int(input("Input encrypted number: ")))
