def prepare_gifts(gifts:list)->list:
  if gifts:
    no_repeted = set(gifts)
    new = list(no_repeted)
    return sorted(new)
  
  return []

gifts1 = [3, 1, 2, 3, 4, 2, 5]
preparedGifts1 = prepare_gifts(gifts1)
print(preparedGifts1) 

gifts2 = [6, 5, 5, 5, 5]
preparedGifts2 = prepare_gifts(gifts2)
print(preparedGifts2)

gifts3 = []
preparedGifts3 = prepare_gifts(gifts3)
print(preparedGifts3) 
