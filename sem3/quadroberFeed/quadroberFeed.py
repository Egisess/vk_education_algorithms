def quadroberFeed(animals: list, food: list) -> int:
    if not animals or not food:
        return 0
    
    animals = sorted(animals)
    food = sorted(food)
    i = 0
    j = 0
    
    while i < len(food) and j < len(animals):
        if food[i] >= animals[j]:
            j += 1
            i += 1
        else:
            i += 1
    return j 
    
if __name__ == '__main__':
    sol = quadroberFeed([3, 4], [1, 4])
    print(f'Quadrobers may be fed: {sol}')
    
    sol = quadroberFeed([1, 2, 3, 4], [1, 1])
    print(f'Quadrobers may be fed: {sol}')
    
    sol = quadroberFeed([1, 2, 3, 4], [2, 4])
    print(f'Quadrobers may be fed: {sol}')