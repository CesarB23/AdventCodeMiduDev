def draw_race(indices:list[int], length:int)->str:
  result = []
  for index,element in enumerate(indices):
    snow_line = "~"*length
    if element == 0:
      new_line = f"{' ' * int(len(indices) - (index + 1 ))}{snow_line} /{index+1}"
    else:
      if element > 0:
        reno_line = snow_line[: element] + "r" + snow_line[element + 1 :]
      else:
        reno_line = snow_line[: element] + "r" + "~"* (abs(element) -1)

      new_line = f"{' ' * int(len(indices) - (index + 1 ))}{reno_line} /{index+1}"

    result.append(new_line)
    
  return "\n".join(result)
    
race = draw_race([0,5,-3],10)
print(race)
print("       ")
race = draw_race([2, -1, 0, 5], 8)
print(race)
print("       ")
race = draw_race([3, 7, -2], 12)
print(race)
