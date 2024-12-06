
def organizeInventory(inventory:list[dict])->dict:
    if not inventory:
        return {}
    
    ordered = {}
    for toy in inventory:
        category,name,quantity = toy.get('category'),toy.get('name'),toy.get('quantity')
        if category not in ordered:
            ordered[category] = {}
        if name in ordered[category]:
            ordered[category][name] += quantity
        else:
            ordered[category][name] = quantity

    return ordered

toys =  [{ "name": 'doll', "quantity": 5, "category": 'toys' },
        { "name": 'car', "quantity": 3, "category": 'toys' },
        { "name": 'ball', "quantity": 2, "category": 'sports' },
        { "name": 'car', "quantity": 2, "category": 'toys' },
        { "name": 'racket', "quantity": 4, "category": 'sports' }]

organized = organizeInventory(toys)
print(organized)
    
        
inventory2 = [
  { "name": 'book', "quantity": 10, "category": 'education' },
  { "name": 'book', "quantity": 5, "category": 'education' },
  { "name": 'paint', "quantity": 3, "category": 'art' }
]

organized2 = organizeInventory(inventory2)
print(organized2)

    
