def converter (lbs):
    kg = lbs / 2.24
    return kg

inp = float(input('Enter lb value: '))
result = converter(inp)
print(result)
