string = """
/*
____*____
___***___
__*****__
_*******_
*********
____#____
____#____
*/
"""

def createXmasTree(height: int,ornament:str)->str:
    lines = []
    padding = height - 1
    base = f"{"_" * padding }#{"_" * padding}"
    n_lines = [i for i in range(1,((height*2)+1)) if i %2 != 0]
    for index,line in enumerate(n_lines):
        lines.append(f"{"_" * (height-index-1)}{ornament*line}{"_" * (height-index-1)} ")
    lines.append(base)
    lines.append(base)
    
    return "\n".join(lines)


tree = createXmasTree(1, '*')
print(tree)

tree2 = createXmasTree(3, '+')
print(tree2)

tree3 = createXmasTree(6, '@')
print(tree3)


