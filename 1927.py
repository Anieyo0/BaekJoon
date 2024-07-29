import sys
input = sys.stdin.readline

def heap_push(heap, item):
    heap.append(item)

    child = len(heap) - 1
    parent = child // 2

    while parent and heap[parent] > heap[child]:
        heap[parent], heap[child] = heap[child], heap[parent]  # 스왑
        child = parent
        parent = child // 2


def heap_pop(heap):
    if len(heap) == 1:
        return

    result = heap[1]
    # 맨 뒤에 있는 녀석을 맨 앞으로 옮겨줌
    heap[1] = heap[-1]
    heap.pop()

    # 자식 노드와 비교해서 옮길 수 있으면 스왑
    parent = 1
    child = parent * 2

    if child+1 <= len(heap)-1:
        if heap[child] > heap[child+1]:
            child += 1
            
    while child <= len(heap)-1 and heap[parent] > heap[child]:
        heap[parent], heap[child] = heap[child], heap[parent]
        parent = child
        child = parent * 2

        # 자식 노드 둘 중에서 더 작은 곳으로
        if child + 1 <= len(heap) - 1:
            if heap[child] > heap[child + 1]:
                child += 1

    return result

N = int(input())
h = ['최소힙:']

for _ in range(N):
    command = int(input())

    if not command:
        if len(h) == 1:
            print(0)
        else:
            print(heap_pop(h))

    if command:
        heap_push(h, command)