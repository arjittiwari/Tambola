from randomNum import RandomNum
from ticket import *
from color import *

class Tambola:
    def __init__(self,row,column,start,end):
        self.row = row
        self.column = column
        self.start=start
        self.end=end
        self.randNumObj = RandomNum(start,end)
    def startGame(self):
        #RandomNum.printList(self.randnum)
        print(Color.YELLOW+Color.UNDERLINE+"\n\n!!!!!!! Let's start Tambola  !!!!!!!\n\n"+Color.END)
        while len(self.randNumObj.numberList) != 0:
            self.randNumObj.shuffle()
            user_input=input("Press 'enter' for next number or q for exit-> ")
            if user_input in ("p","P"):
                self.printBoard()
                continue
            elif user_input in ("q","Q"):
                exit()
            print(self.randNumObj.numberList.pop())
        else:
            print(Color.GREEN+ "\n\n!!!!!!! Game Over  !!!!!!!\n\n"+Color.END)
    def createTicket(self):
        return Ticket(self.row,self.column,self.start,self.end)
    def printBoard(self):
        line = 0
        for num in range(self.start,self.end+1):
            if num in self.randNumObj.numberList:
                print("%02d" % num,end=" ")
            else:
                print(Color.RED + "%02d" % num + Color.END,end=" ")
            if int(num/10) != line:
                line=int(num/10)
                print("")

if __name__ == "__main__":
    t1 = Tambola(row=3,column=9,start=1,end=90)
    newticket=t1.createTicket()
    newticket.printTicket()
    newticket1 = t1.createTicket()
    newticket1.printTicket()
    t1.startGame()