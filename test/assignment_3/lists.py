##########################################################################
##########################################################################
###                                                                    ###
###                       UNC CS301  Spring 2025                       ###
###                             Assignment 3                           ###
###                                 Lists                              ###
###                                                                    ###
##########################################################################
##########################################################################

""" For this and other assignments in CS301,
    replace the lines
         # TODO:  Implement me!
         pass
    in the given stencil code with your own solutions.
    Don't change the names of the given functions
    or else the autograder won't be able to evaluate
    your code.  The autograder will automatically
    evaluate your code each time you commit it to
    GitHub.  You may submit it as may times as
    you want before the submission deadline.
"""

######  Problem #1 #########################

class Stack:

    def __init__(self):
      self.list = []
      
        
    def __repr__(self):
      return "Stack: "+str(self.list)
        
    def push(self, item): 
      self.list.append(item)
    
    def pop(self):
        temp=self.list[len(self.list)-1]
        self.list.remove(self.list[len(self.list)-1])
        return temp

    def peek(self):  
      return self.list[len(self.list)-1]

        
    def isEmpty(self): 
      if len(self.list) == 0:
        return True
      else:
        return False

    def size(self):
      return len(self.list)

"""
####  Explaination of the Big O running time ####
####  of your implemented methods:           ####



"""

######  Problem #2 #########################


class Queue:

    def __init__(self):
      self.list = []
      pass

    def __repr__(self):
      return "Queue: "+str(self.list)
        
    def enqueue(self, item): 
      self.list.append(item)
    
    def dequeue(self):  
      temp=self.list[0]
      self.list.remove(self.list[0])
      return temp
    
    def isEmpty(self):  
      if len(self.list) == 0:
        return True
      else:
        return False
          
    def size(self):
      return len(self.list)

"""
####  Explaination of the Big O running time ####
####  of your implemented methods:           ####



"""

######  Problem #3 #########################


class Deque:

    def __init__(self):
      self.list = []
      pass

    def __repr__(self):
      return "Deque: "+str(self.list)
    
    def addFront(self, item): 
      self.list.insert(0,item)
    
    def removeFront(self):  
      temp=self.list[0]
      self.list.remove(self.list[0])
      return temp

    def addRear(self, item): 
      self.list.append(item)
    
    def removeRear(self):  
      temp=self.list[len(self.list)-1]
      self.list.remove(self.list[len(self.list)-1])
      return temp
    
    def isEmpty(self):  
      if len(self.list) == 0:
        return True
      else:
        return False
    
    def size(self):
      return len(self.list)

"""
####  Explaination of the Big O running time ####
####  of your implemented methods:           ####



"""


######  Problem #4 #########################

class Node:

    def __init__(self, InputValue=None):
      self.data = InputValue
      self.next = None

    def __repr__(self):
      return "Node: "+str(self.data)
    
    # Also TO DO:  Implement the rest of the Node class!

class Linked_List:

    def __init__(self):
      self.firstnode=None
      pass

    def __repr__(self):
      output="start--->"
      current=self.firstnode
      while current != None:
        output=output+str(current.data)+"--->"
        current=current.next
      output=output+"end"
      return output
      
    
    def add(self, item): 
      newnode=Node(item)
      newnode.next=self.firstnode
      self.firstnode=newnode
    
    def remove(self, item):  
      current=self.firstnode
      previous=None
      found=False
      while not found:
        if current.data==item:
          found=True
        else:
          previous=current
          current=current.next
      if previous==None:
        self.firstnode=current.next
      else:
        previous.next=current.next
      return found
        
            
    def search(self, item):
      current=self.firstnode
      found=False
      while current != None and not found:
        if current.data==item:
          found=True
        else:
          current=current.next
      return found

    def isEmpty(self):
      if self.firstnode==None:
        return True
      else:
        return False
    
    def size(self):
      count=0
      current=self.firstnode
      while current != None:
        count+=1
        current=current.next
      return count

    def append(self, item): 
      newnode=Node(item)
      current=self.firstnode
      if current==None:
        self.firstnode=newnode
      else:
        while current.next != None:
          current=current.next
        current.next=newnode
    
    def index(self, item):  
      current=self.firstnode
      found=False
      count=0
      while current != None and not found:
        if current.data==item:
          found=True
        else:
          current=current.next
          count+=1
      if found:
        return count
      else:
        return LookupError("Item not found")
    
    def insert(self, pos, item):  
      current=self.firstnode
      if pos==0:
        newnode=Node(item)
        newnode.next=self.firstnode
        self.firstnode=newnode
      else:
        count=0
        while current != None and count+1 != pos:
          current=current.next
          count+=1
        if current != None:
          newnode=Node(item)
          newnode.next=current.next
          current.next=newnode    
        else: 
          print("Index out of range")


    def pop(self):
      current=self.firstnode
      previous=None
      while current.next != None:
        previous=current
        current=current.next
      if previous==None:
        self.firstnode=None
      else:
        previous.next=None
      return current.data
    
    def popfrom(self, pos):
      current=self.firstnode
      previous=None
      count=0
      if pos==0:
        self.firstnode=self.firstnode.next
      else:
        while current != None and count+1 != pos:
          previous=current
          current=current.next
          count+=1
        if current != None:
          previous.next=current.next
        else:
          print("Index out of range")

"""
####  Explaination of the Big O running time ####
####  of your implemented methods:           ####



"""

######  Problem #5 #########################

class DLL_Node:

    def __init__(self):
      self.firstnode=None
      

    def __repr__(self):
      return "Node: "+str(self.data)   

    # Also TO DO:  Implement the rest of the DLL_Node class!

class Doubly_Linked_List:

    def __init__(self):
      # TO DO:  Implement me!
      pass

    def __repr__(self):
      # TO DO:  Implement me!
      pass       
    
    def add(self, item): 
      # TODO:  Implement me!
      pass
    
    def remove(self, item):  
      # TODO:  Implement me!
      pass
    
    def search(self, item):  
      # TODO:  Implement me!
      pass

    def isEmpty(self):  
      # TODO:  Implement me!
      pass
    
    def size(self):
      # TODO:  Implement me!
      pass

    def append(self, item): 
      # TODO:  Implement me!
      pass
    
    def index(self, item):  
      # TODO:  Implement me!
      pass
    
    def insert(self, pos, item):  
      # TODO:  Implement me!
      pass

    def pop(self):  
      # TODO:  Implement me!
      pass
    
    def popfrom(self, pos):
      # TODO:  Implement me!
      pass

"""
####  Explaination of the Big O running time ####
####  of your implemented methods:           ####



"""

######  Problem #6 #########################
"""
####    Do you think that python's internal representation ####
####    of a list is a linked-list, a doubly-linked list,  ####
####    or something else? Why or why not?                 ####

    
    
    

"""


######  Problem #7 #########################
"""
####    Now that you've implemented linked lists and doubly-linked lists,    ####
####    you have the option of using these in place of python lists inside   ####
####    your implementation of stacks, queues, and dekes. For each of these, ####
####    explain which type of list (python list, linked list, or             ####
####    doubly-linked list) should give the best Big Oh running time.        ####


"""