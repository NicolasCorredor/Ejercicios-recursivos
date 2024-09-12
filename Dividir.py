def division(dividendo,divisor):
    if dividendo<divisor:
        return 0
    return 1+division(dividendo-divisor,divisor)

#ejemplo funcionamiento
print(division(30,3))