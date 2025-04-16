import heapq as heap
def sortUnion(arr: list[list]) -> list:
    minHeap = []

    for i in range(len(arr)):
        for j in (len(arr[i])):
            heap.heappush(minHeap, arr[i][j])

    merged = []
    while len(minHeap):
        merged.append(heap.heappop(minHeap))
    
    return merged