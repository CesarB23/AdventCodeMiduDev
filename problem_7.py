def fixPackages(packages:str)->str:
    stack = []  
    current = []  
    # Search for an openin or closing parenthesis, if there's no match the char is added to the current
    # If an opening parenthesis is found all the current content is addded to the stack to "reverse" it
    # If a closing parenthesis is found, the content of the last stack position  via stack.pop is added to the reserved content of the current 
    # Finally the result is returned 
    for char in packages:
        # Search for an opening parenthesis
        print(f"char: {char} stack: {stack} current: {current}")
        if char == '(':
            # Al encontrar un paréntesis de apertura, guardar la subsección actual en la pila
            stack.append(current)

            current = []  # Iniciar una nueva subsección
        elif char == ')':
            # Al encontrar un paréntesis de cierre, voltear la subsección actual
            reversed_content = current[::-1]
            # Recuperar la sección anterior de la pila y añadir el contenido volteado
            current = stack.pop() + reversed_content
        else:
            # Añadir caracteres normales al contenido actual
            current.append(char)

    # Combinar el resultado final
    return ''.join(current)

""" print(fixPackages('a(cb)de'))  # "abcde" """
print(fixPackages('a(bc(def)g)h'))  # "agdefcbh"
""" print(fixPackages('abc(def(gh)i)jk'))  # "abcighfedjk" """
""" print(fixPackages('a(b(c))e'))  # "acbe" """