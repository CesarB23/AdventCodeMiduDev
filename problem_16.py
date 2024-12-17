def remove_snow(s: str) -> str:
    if len(s) <= 1:
        return s

    copy = list(s)
    position = 0

    while position < len(copy) - 1:
        print(f"Copy: {copy} Position: {position} Actual: {copy[position]} Actual + 1: {copy[position +1 ]}")
        if copy[position] == copy[position + 1]:
           
            del copy[position]
            del copy[position]  
            
            position = 0
        else:
            
            position += 1

    return ''.join(copy)

print(remove_snow('zxxzoz')) #// -> "oz"
#// 1. Eliminamos "xx", quedando "zzoz"
#// 2. Eliminamos "zz", quedando "oz"

print(remove_snow('abcdd')) #// -> "abc"
#// 1. Eliminamos "dd", quedando "abc"

print(remove_snow('zzz')) #// -> "z"
#// 1. Eliminamos "zz", quedando "z"

print(remove_snow('a')) #// -> "a"
#// No hay montículos repetidos