import re 
def compile(instructions:list[str])->int:
  
  registers = {}
  pointer = 0

  while pointer < len(instructions):
    command = instructions[pointer]
    commands = command.split(" ")
    
    if len(commands) > 1 and commands[1] not in registers:
            registers[commands[1]] = 0

    if commands[0] == "MOV":
      if re.search(r"-?\d",commands[1]):
        registers[commands[2]] = int(commands[1])
      else:
        change = registers[commands[1]]
        registers[commands[2]] = change

    elif commands[0] == "INC":
      registers[commands[1]] += 1

    elif commands[0] == "DEC":
      registers[commands[1]] -= 1
    
    elif commands[0] == "JMP":
      if registers[commands[1]] == 0:
        pointer = int(commands[2])
        continue


    pointer += 1

  if registers["A"] == 0:
    return -1
  else:
    return registers["A"]


instructions = [
  'MOV -1 C', #// copia -1 al registro 'C',
  'INC C', #// incrementa el valor del registro 'C'
  'JMP C 1',
  'MOV C A', #// copia el registro 'C' al registro 'a',
  'INC A' #// incrementa el valor del registro 'a'
]



result =compile(instructions)
print(result)

