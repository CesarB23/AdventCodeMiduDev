import re

def in_box(box:list[str])->bool:
    #print(len(box))
    for row in range(1,len(box)-1):
        pattern = re.search(".[*].",box[row])
        print(f"pattern: {pattern} row {box[row]}")
        if pattern:
            return True
    return False


inBox = ([
  "###",
  "# * #",
  "###"
])

present = in_box(inBox)
print(present)

inBox =([
  "####",
  "#* #",
  "#  #",
  "####"
])

present2 = in_box(inBox)
print(present2)

inBox = ([
  "#####",
  "#   #",
  "#  #*",
  "#####"
])

present3 = in_box(inBox)
print(present3)

inBox = ([
  "#####",
  "#   #",
  "#   #",
  "#   #",
  "#####"
])

present4 = in_box(inBox)
print(present4)
