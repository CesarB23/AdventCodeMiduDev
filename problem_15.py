def draw_table(data: list[dict[str, str | int]]) -> str:
  table = []
  new_data = {}
  for item in data:
    item_1, item_2 = item.items()
    if item_1[0] not in new_data or item_2[0] not in new_data:
      new_data[item_1[0]] = [item_1[1]]
      new_data[item_2[0]] = [item_2[1]]
    else:
      new_data[item_1[0]].append(item_1[1])
      new_data[item_2[0]].append(item_2[1])

  title_1,title_2 = new_data.keys()
  
  items_1,items_2 = new_data[title_1],new_data[title_2]
 
  if type(items_2[0]) == int:
    max_lenght_items_1 = max(items_1,key=len)
    max_global = max(max_lenght_items_1,title_1,title_2,key=len)
    
  else:
    max_lenght_items_1 = max(items_1,key=len)
    max_lenght_items_2 = max(items_2,key=len)
    max_global = max(max_lenght_items_1,max_lenght_items_2,title_1,title_2,key=len)
  
  separators = f"+-{'-' * len(max_global)}-+-{'-'* len(max_global)}-+"
  table.append(separators)
  table.append(f"| {title_1.capitalize()}{' '* (len(max_global)-len(title_1))} | {title_2.capitalize()}{' '* (len(max_global)-len(title_2))} |")
  table.append(separators)

  for item1,items2 in zip(items_1,items_2):
    table.append(f"| {item1}{' ' * (len(max_global)-len(str(item1)))} | {items2}{' ' * (len(max_global)-len(str(items2)))} |")
  table.append(separators)

  return "\n".join(table)
  
 
  

result = draw_table([
  { "name": 'Alice', "city": 'London' },
  { "name": 'Bob', "city": 'Paris' },
  { "name": 'Charlie', "city": 'New York' }
])
print(result)

"""
// +---------+-----------+
// | Name    | City      |
// +---------+-----------+
// | Alice   | London    |
// | Bob     | Paris     |
// | Charlie | New York  |
// +---------+-----------+
"""

result = draw_table([
  { "gift": 'Doll', "quantity": 10 },
  { "gift": 'Book', "quantity": 5 },
  { "gift": 'Music CD', "quantity": 1 }
])
print(result)
"""
// +----------+----------+
// | Gift     | Quantity |
// +----------+----------+
// | Doll     | 10       |
// | Book     | 5        |
// | Music CD | 1        |
// +----------+----------+
"""