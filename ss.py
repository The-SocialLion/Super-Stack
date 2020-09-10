from collections import OrderedDict
class SuperStack:
    def __init__(self):
        self.ss=[]
        self.limit=int(input("enter limit"))
        self.top=None
        self.bottom=None
        self.mid=None
    def isFull(self):
        if len(self.ss)== self.limit:
            return True
        else:
            return False
    def isEmpty(self):
        if len(self.ss)== 0 and self.top==self.bottom:
            return True
        else:
            return False
    def check(self,n,ele):
      if (n//2<=self.limit):
         mid=self.limit//2
         if n<mid:
            self.push_top(n,ele)
         elif n>mid:
            self.push_bottom(n,ele)
         elif n==mid:
             if ele%2==0:
                self.push_top(n,ele)
             else:
                  self.push_bottom(n,ele)
      else:
         print("invalid entry try again")
    def push_top(self,n,ele):
        if self.isFull():
         print("stack overflow")
        else:
         if self.top==None and self.bottom==None:
             self.top=self.bottom=self.mid=0
         else:
            self.mid=(self.top+self.bottom)%self.limit
            self.top=self.mid-1
         self.ss.insert(n,ele)
    def push_bottom(self,n,ele):
        if self.isFull():
         print("stack overflow")
        else:
            if self.top==None and self.bottom==None:
                 self.top=self.bottom=self.mid=0
            else:
                self.mid=(self.top+self.bottom)%self.limit
                self.bottom=self.mid+1
            self.ss.insert(n,ele)
    def pop_top(self):
        if self.isEmpty():
            print("stack underflow")
        else:
             print(self.ss.pop(0))
             if self.top==self.bottom:
               self.top=self.bottom=self.mid=None
             else:
               self.mid=(self.top+self.bottom)%self.limit
             self.top=self.mid+1
    def pop_buttom(self):
         if self.isEmpty():
            print("stack underflow")
         else:
            print(self.ss.pop())
            if self.top==self.bottom:
                self.top=self.bottom=self.mid=None
            else:
                 self.mid=(self.top+self.bottom)%self.limit
                 self.buttom=self.mid-1
    def find(self,ele):
        flag=False
        if self.isEmpty():
          print("stack underflow")
        else:
           for i in range(0,len(self.ss)):
             while (self.ss[i]==ele):
               n=i
               flag=True
               break
        if flag:
          print("element found@",n)
        else:
          print("element not found")
          
    def arrange(self,c):
        if self.isEmpty():
             print("stack underflow")
        elif c==1:
            self.ss.sort(reverse=True)
            print(self.ss)
        else:
            self.ss.sort()
            print(self.ss)     

    def reset(self):
       if self.isEmpty():
        print("stack underflow")
       else:
          self.ss=self.ss.clear()
          print("stack has been reset")
          
    def remove_dup(self):
       if self.isEmpty():
        print("stack underflow")
       else:
        self.ss= list(OrderedDict.fromkeys(self.ss))  
        print("duplicate elements removal succesfull!")
    def xchange(self,ele,pos):
      flag=False
      if self.isEmpty():
        print("stack underflow")
      else:
        for i in range(0,len(self.ss)):
          if i==pos :
            self.ss[i]=ele
            flag=True
            break
        if flag:
          print("element exhange succesfull")
          print(self.ss)
        else:
          print("element exchange unsuccesfull")

    def display(self):
        if self.isEmpty():
            print("stack underflow")
        else:
            for i in self.ss:
             print(i,end=" ")
             print()


ss=SuperStack()
while True:
  print("1.push operation")
  print("2.pop_bottom, 3.pop_top")
  print("4.display,5.find")
  print("6.exchange,7.remove-duplicates")
  print("8.reset,9.arrange,10.exit")
  ch=int(input("enter your choice"))
  if ch==1:
     n=int(input("enter position"))
     ele=int(input("enter element"))
     ss.check(n,ele)
  elif ch==2:
     ss.pop_buttom()
  elif ch==3:
     ss.pop_top()
  elif ch==4:
      ss.display()
  elif ch==5:
      ele=int(input("enter element"))
      ss.find(ele)
  elif ch==6:
      ele=int(input("enter element"))
      pos=int(input("enter position"))
      ss.xchange(ele,pos)  
  elif ch==7:
      ss.remove_dup()
  elif ch==8:
      ss.reset()
  elif ch==9:
       m=int(input("enter sequence"))
       ss.arrange(m)
  elif ch==10:
      break
  else:
      print("invalid choice,try again!")
