def organizeShoes(shoes:list[dict])->list:
    inventory = {}

    for shoe in shoes:
        size = shoe["size"]
        side = shoe["type"]
        if size not in inventory:
            inventory[size] = {"I": 0, "R": 0}
        inventory[size][side] += 1  

    pairs = []
    for size, count in inventory.items():
        left = count["I"]
        right = count["R"]
        pairs_count = min(left, right)  
        for _ in range(pairs_count):
            pairs.append(size)  
    return pairs     
    


""" shoes = [
  { "type": 'I', "size": 38 },
  { "type": 'R', "size": 38 },
  { "type": 'R', "size": 42 },
  { "type": 'I', "size": 41 },
  { "type": 'I', "size": 42 } 
]

organizeShoes(shoes) """

shoes2 = [{ "type": 'I', "size": 38 },
  { "type": 'R', "size": 36 },
  { "type": 'R', "size": 42 },
  { "type": 'I', "size": 41 },
  { "type": 'I', "size": 43 }]

organizeShoes(shoes2)


shoes3 = [
    { "type": 'I', "size": 38 },
  { "type": 'R', "size": 38 },
  { "type": 'I', "size": 38 },
  { "type": 'I', "size": 38 },
  { "type": 'R', "size": 38 }

]

organizeShoes(shoes3)