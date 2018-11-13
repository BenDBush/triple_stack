class triple_stack(list):
    def __init__(self, top1 = 0, top2 = 0, top3 = 0):
        self.marker1 = 0
        self.marker2 = 1
        self.marker3 = 2
        self = [top1, top2, top3]
        print(self)


    def id_marker(self, stack):
        mark = None
        if stack == 0:
            mark = (self.marker1, self.marker2, self.marker3)
        elif stack == 1:
            mark = (self.marker2, self.marker1, self.marker3)
        elif stack == 2:
            mark = (self.marker3, self.marker1, self.marker2)

        return mark


    def push(self, item, stack):
        mark, oth1, oth2 = self.id_marker(stack)    
        self = self[:mark-1] + [item] + self[mark-1:]


    def pop(self, stack):
        mark, oth1, oth2 = self.id_marker(stack)
        popped_item = self[mark]
        self = self[:mark-1] + self[mark:]
        return popped_item


    

if __name__ == '__main__':
    test_triple_stack = triple_stack()
    test_triple_stack.push(1, 0)
    test_triple_stack.push(5, 1)
    test_triple_stack.push(9, 2)
    print(test_triple_stack)
    print(5==test_triple_stack.pop(1))