from collections import deque
class FreqStack:

    def __init__(self):
        self.freq = {}
        self.group = {}
        self.max_num = 0

    def push(self, val: int) -> None:
        if val not in self.freq:
            self.freq[val] = 0
        self.freq[val] += 1
        curr_freq = self.freq[val]
        if self.max_num < curr_freq:
            self.max_num = curr_freq
        if curr_freq not in self.group:
            self.group[curr_freq] = deque()
        self.group[curr_freq].append(val)

    def pop(self) -> int:
        val = self.group[self.max_num].pop()
        self.freq[val] -= 1
        if not self.group[self.max_num]:
            self.max_num -= 1
        return val
