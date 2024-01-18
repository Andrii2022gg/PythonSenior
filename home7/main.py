def calcu(func):
    def sumary(expression):
        allowed_operators = set(' +-*/()0123456789')

        if not all(char in allowed_operators for char in expression):
            raise ValueError("Symvol EROR")

        try:
            result = func(expression)
            return result
        except Exception as e:
            raise ValueError(f"Calculate error: {e}")

    return sumary

@calcu
def calculate(expression):
    try:
        return eval(expression)
    except ValueError as ve:
        print(f"Помилка: {ve}")


print("Result:", calculate("2 + 2 * 3"))
