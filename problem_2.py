def createFrame(names: list[str]) -> str:

    lines = []
    width = len(max(names, key=len)) + 4
        
    lines.append("*" * width)
      
    for name in names:
        padding = width - len(name) - 3
        lines.append(f"* {name}{' ' * padding}*")
       
    lines.append("*" * width)
    
    
    return "\n".join(lines)

names = ['midu', 'madeval', 'educalvolpz']
print(createFrame(names))

names = ['midu']
print(createFrame(names))  

names = ['a', 'bb', 'ccc']
print(createFrame(names))

names =['a', 'bb', 'ccc', 'dddd']
print(createFrame(names))

