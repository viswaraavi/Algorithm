import heapq
def mergesort(list_of_lists, key=None):

    heap = []
    z=[iter(pl) for pl in list_of_lists]
    for i, itr in enumerate(z):
        try:
            item = itr.next()
            toadd = (item,itr)
            heap.append(toadd)
        except StopIteration:
            pass
    heapq.heapify(heap)
    while heap:
        item,  itr = heap[0]
        yield item
        try:
            heapq.heapreplace(heap, (itr.next(), itr))
        except StopIteration:
            heapq.heappop(heap)

for i in mergesort([[1, 2, 3, 4,20,21],[2, 3.5, 3.7, 4.5, 6, 7], [2.6, 3.6, 6.6, 9]]):
    print i
