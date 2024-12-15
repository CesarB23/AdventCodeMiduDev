def min_moves_to_stables(reindeer:list[int],stables:list[int])-> int:
    distances = []
    stables = stables.copy()
    for rein in reindeer:
        
        actual_distance = [abs(rein-stable) for stable in stables]
        min_distance = min(actual_distance)
        
        index_min_stable = actual_distance.index(min_distance)
        distances.append(min_distance)
        print(f"Actual Distance: {actual_distance} Min Distance {min_distance} Index Min Distance {index_min_stable}")
        
        stables.pop(index_min_stable)
    
    return sum(distances)
            
           
        
result =min_moves_to_stables([2, 6, 9], [3, 8, 5])
print(result)

result =min_moves_to_stables([1, 1, 3], [1, 8, 4])
print(result)

# POP removes specified index, default -1 """
