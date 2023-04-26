def buildMaxHeap(arr):
    n = len(arr)
    for i in range(n//2 - 1, -1, -1):
        maxHeapify(arr, n, i)

def maxHeapify(arr, n, i):
    largest = i
    left = 2*i + 1
    right = 2*i + 2
    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        maxHeapify(arr, n, largest)

def deleteMax(arr, vacant):
    n = len(arr)
    if n == 0:
        return -1
    maxVal = arr[0]
    arr[0] = vacant
    maxHeapify(arr, n, 0)
    return maxVal

def acceleratedHeapsort(arr):
    buildMaxHeap(arr)
    vacant = -float('inf')
    sortedArr = []
    while True:
        maxVal = deleteMax(arr, vacant)
        if maxVal == -1:
            break
        sortedArr.append(maxVal)
    return sortedArr

scores = [5,3,2,1,4]
sortedScores = acceleratedHeapsort(scores)
print("최대힙 자료구조: ", scores)
print("정렬된 시험 점수: ", sortedScores)
print("알고리즘 수행 시간: ", len(scores))  # deleteMax 과정에서 vacant가 변경될 때마다 1초가 소요된다.
