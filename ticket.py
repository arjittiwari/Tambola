from randomNum import RandomNum
class Ticket:
    def __init__(self,row,column,start,end):
        self.ticket = [[0]*column]*row
        self.start = start
        self.end = end
        self.randListObj = RandomNum(self.start,self.end)
        self.generateTicket(row,column)
    def printTicket(self):
        for row in self.ticket:
            for col in row:
                print("%02d" % col,end=" ")
            print("")
        print("\n")
    def generateTicket(self,row,column):
        numCount=15
        while numCount>0 and len(self.randListObj.numberList)>0:
            val = self.randListObj.numberList.pop()
            self.randListObj.shuffle()
            column=int(val/10)
            if val == 90:
                column = column - 1
            for index in range(len(self.ticket)):
                if self.ticket[index][column] == 0 and self.ticket[index].count(0)> 4:
                    bcup = self.ticket[index]
                    self.ticket[index] = self.ticket[index][:column]
                    self.ticket[index].append(val)
                    self.ticket[index]=self.ticket[index]+bcup[column+1:]
                    numCount = numCount - 1
                    break
        for index in range(column):
            sortlist=[]
            for x in range(len(self.ticket)):
                if self.ticket[x][index] > 0:
                    sortlist.append(self.ticket[x][index])
            sortlist.sort(reverse=True)
            for x in range(len(self.ticket)):
                if self.ticket[x][index] > 0:
                    self.ticket[x][index] = sortlist.pop()

        
