import sys

class Queue:
    def __init__(self, n):
        self.n = n
        self.queue = [0] * n
        self.head = 0
        self.tail = 0

    def enqueue(self, a: int):
        if self.tail - self.head < self.n:
            self.queue[self.tail % self.n] = a
            self.tail += 1
        else:
            print('queue is full')

    def dequeue(self):
        if self.head < self.tail:
            tmp = self.queue[self.head % self.n]
            print(tmp)
            self.head += 1
        else: print('queue is empty')



def main(lines):
    # このコードは標準入力と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。

    #for i, v in enumerate(lines):
    #    print("line[{0}]: {1}".format(i, v))
    Q = int(lines[0])
    K = int(lines[1])
    q = Queue(K)
    i = 2
    while i < len(lines):
        if int(lines[i]) == 1:
            q.enqueue(int(lines[i+1]))
            i += 2
        elif int(lines[i]) == 2:
            q.dequeue()
            i += 1
        else:
            print('Invalid Command.')

        
if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.extend(l.rstrip('\r\n').split())
    main(lines)