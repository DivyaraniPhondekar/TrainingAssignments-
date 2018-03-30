class Stack:
     def __init__(self):
         self.items = []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

class main():
    s=Stack()
    while(1):
        x=input("Plase Enter operation no. you want to execute: 1. PUSH 2.POP 3.PEEK 4.EXIT \n")
        if x == 1:
            s.push(input("Enter the value \n"))
        elif x == 2:
            print "Poped value is ",s.pop()
        elif x == 3:
            print "Top of the stack is ",s.peek()
        elif x == 4:
            exit(0)

if __name__ == '__main__':
    main()
