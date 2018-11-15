class triple_stack:
    def __init__(self, top1 = 0, top2 = 0, top3 = 0):
        mark1, mark2, mark3 = (0,1,2)
        self.markers = [mark1,mark2,mark3]
        self.list = [top1, top2, top3]



    def push(self, item, stack):
        mark = self.markers[stack]    
        self.list = self.list[:mark] + [item] + self.list[mark:]
        for i in range(len(self.markers)):
            if self.markers[i] > mark:
                self.markers[i] += 1




    def pop(self, stack):
        mark = self.markers[stack]
        popped_item = self.list[mark]
        self.list = self.list[:mark] + self.list[mark+1:]
        for i in range(len(self.markers)):
            if self.markers[i] > mark:
                self.markers[i] -= 1


        return popped_item


    

if __name__ == '__main__':
    test_triple_stack = triple_stack(top1=1, top2 = 2, top3 = 3)
    print(test_triple_stack.list)
    test_triple_stack.push(13, 0)
    test_triple_stack.push(5, 1)
    test_triple_stack.push(9, 2)
    print(test_triple_stack.list)
    print(test_triple_stack.markers)
    print(test_triple_stack.pop(1))
    print(test_triple_stack.list)
    print(test_triple_stack.markers)