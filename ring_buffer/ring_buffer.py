class RingBuffer:
  def __init__(self, capacity, oldest = 0):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity
    self.oldest = oldest
  def append(self, item):
    last = len(self.storage)
    for i in range(0,last):
      if self.storage[i] == None:
        self.storage[i] = item
        return 1
    self.storage[self.oldest] = item
    self.oldest += 1
    if self.oldest == last:
      self.oldest = 0
    return self.storage
  def get(self):
    test = [i for i in self.storage]
    for i in range(0, self.capacity):
      if test[i] == None:
        test.pop(i)
    return test