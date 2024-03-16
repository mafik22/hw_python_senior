result = []

def divider(a, b):
    try:
        a = float(a)
        b = float(b)
        if a < b:
            raise ValueError("a має бути більше або рівне b")
        if b == 0:
            raise ZeroDivisionError("Ділення на нуль")
        if b > 100:
            raise IndexError("b має бути менше або рівне 100")
        return a / b
    except ValueError:
        print("ValueError:")
    except ZeroDivisionError:
        print("ZeroDivisionError:")
    except IndexError:
        print("IndexError:")

data = {10: 2, 2: 5, "123": 4, 18: 0, 8: 4}
for key in data:
    res = divider(key, data[key])
    if res is not None:
        result.append(res)

print(result)
