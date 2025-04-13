def annagramsGroupping(strings: list[str]) -> list:
    anagram_groups = {}
    
    for s in strings:
        byte_counts = [0] * 256 
        
        for char in s:
            byte_counts[ord(char)] += 1 # Реализуем собственный bytecounter

        byte_key = tuple(byte_counts) # Массив не мб ключом а вот tuple - да
        
        if byte_key in anagram_groups:
            anagram_groups[byte_key].append(s)
        else:
            anagram_groups[byte_key] = [s]
    
    return list(anagram_groups.values())

if __name__ == '__main__':
    test = ["eat","tea","tan","ate","nat","bat"]
    print(annagramsGroupping(test))