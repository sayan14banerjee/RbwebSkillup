import math
result=list(x for x in range(1, 51) if math.sqrt(x).is_integer())

print(result)