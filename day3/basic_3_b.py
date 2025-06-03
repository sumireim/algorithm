import sys

class MyHeap:
    def __init__(self, size):
        self.inf = -(10**9) 
        self.size = size + 1
        self.array = [self.inf]*self.size
        self.last = 0 
        
    def add(self, value: int):
        if self.last < self.size - 1:
            self.last += 1
            self.array[self.last] = value
            self._heapify_up(self.last)

    def remove(self):
        if self.last != 0:
            removed = self.array[1]
            print(removed)
            self.array[1] = self.array[self.last]
            self.last -= 1
            self._heapify_down(1)

    def _heapify_up(self, i):
        while i > 1:
            parent = i // 2
            if self.array[parent] < self.array[i]:
                self.array[parent], self.array[i] = self.array[i], self.array[parent]
                i = parent
            else:
                break

    def _heapify_down(self, i):
        while 2 * i <= self.last:
            left = 2 * i
            right = 2 * i + 1
            largest = i

            if left <= self.last and self.array[left] > self.array[largest]:
                largest = left
            if right <= self.last and self.array[right] > self.array[largest]:
                largest = right

            if largest != i:
                self.array[i], self.array[largest] = self.array[largest], self.array[i]
                i = largest
            else:
                break
    
def main(lines):
    # このコードは標準入力と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。

    #for i, v in enumerate(lines):
    #    print("line[{0}]: {1}".format(i, v))
    Q = int(lines[0])
    h = MyHeap(Q)
    i = 1
    while i < len(lines):
        if int(lines[i]) == 1:
            h.add(int(lines[i + 1])) 
            i += 2
        elif int(lines[i]) == 2:
            h.remove() 
            i += 1
        else:
            print('Invalid Command.')

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.extend(l.rstrip('\r\n').split())
    main(lines)