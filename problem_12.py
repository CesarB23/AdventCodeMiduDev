def calculate_price(ornaments:str) -> int:
    prices = {"*":1,
              "o":5,
              "^":10,
              "#":50,
              "@":100}
    
    result = 0

    for index,char in enumerate(ornaments):
        if char not in prices:
            return -1 
        
        if index == len(ornaments)-1:
            result += prices[char]
        else:
            if ornaments[index+1] not in set(prices.keys()):
                return -1
            
            elif (prices[char] < prices[ornaments[index+1]]):
                result += -1*(prices[char])
            else:
                result += prices[char]

    return result

chars = '***'
result = calculate_price(chars)
print(f"Result: {result}")

chars = '*o'
result = calculate_price(chars)
print(f"Result: {result}")
chars = 'o*'   #// 6   5 + 1
result = calculate_price(chars)
print(f"Result: {result}")
chars = '*o*'  #// 5  -1 + 5 + 1 
result = calculate_price(chars)
print(f"Result: {result}")
chars = '**o*' #// 6  1 - 1 + 5 + 1 
result = calculate_price(chars)
print(f"Result: {result}")
chars = 'o***' #// 8   5 + 3
result = calculate_price(chars)
print(f"Result: {result}")
chars = '*o@'  ## 94  -5 - 1 + 100
result = calculate_price(chars)
print(f"Result: {result}")
chars = '*#'   ## 49  -1 + 50
result = calculate_price(chars)
print(f"Result: {result}")
chars = '@@@'  ## 300 100 + 100 + 100
result = calculate_price(chars)
print(f"Result: {result}")
chars = '#@'   ## 50  -50 + 100
result = calculate_price(chars)
print(f"Result: {result}")
chars = '#@Z'  ## undefined (Z es desconocido)
result = calculate_price(chars)
print(f"Result: {result}")