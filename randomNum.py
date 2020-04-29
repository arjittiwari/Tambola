import random

class RandomNum:
    
    def __init__(self,start,end):
        self.numberList=list(range(start,end+1))
        self.shuffle()

    def printList(self):
        print(self.numberList)
    
    def shuffle(self):
        random.shuffle(self.numberList)


if __name__ == "__main__":
    randnum = RandomNum(1,90)
    randnum.printList()
else:
    pass
