This GitHub repository is for you to work on UNC CS301 Assignment 3.
The problems for you to work on are below.  You should work on them in the
lists.py file, found also in this directory.  You will submit your 
work by committing this file back to your Github repository.  Each time
you commit it, it will be autograded, and you can see the results in the 
"Actions" tab.  You can resubmit as many times as you'd like prior to
the submission deadline.

Now that we've explored some data structures from the outside, we're
going to try to build some of our own. We'll focus on various data types
for organizing ordered collections---that is, different kinds of lists.

We will create our data structures as objects, and as we do so, we want
to think about keeping the big O running time of their methods as low as
possible.

1.  A *stack* is like a list, except that items can only be added or
    removed from one end (the "top" of the stack). It is like a stack of
    books---you can add a book to the top of the stack, or remove a book
    from the top of the stack. Stacks are referred to as LIFO---"Last
    in, First out"---data structures. Implement a stack. This is where
    we start using object oriented programing to create our own data
    structures. Your stack can use a python list internally to hold your
    data.

    Your stack should implement the following methods:

    Stack()

    :   creates a new stack that is empty. It needs no parameters and
        returns an empty stack.

    push(item)

    :   adds a new item to the top of the stack. It needs the item and
        returns nothing.

    pop()

    :   removes the top item from the stack. It needs no parameters and
        returns the item. The stack is modified.

    peek()

    :   returns the top item from the stack but does not remove it. It
        needs no parameters. The stack is not modified.

    isEmpty()

    :   tests to see whether the stack is empty. It needs no parameters
        and returns a boolean value.

    size()

    :   returns the number of items on the stack. It needs no parameters
        and returns an integer.

    You will also want to implement a method to print out your stack in
    order to test your code. In comments, describe the running time of
    each method of your implementation.

2.  A *queue* is just like a stack, except that it has a FIFO---"First
    In, First Out"---structure. Implement a queue. It should have the
    following methods:

    Queue()

    :   creates a new queue that is empty. It needs no parameters and
        returns an empty queue.

    enqueue(item)

    :   adds a new item to the rear of the queue. It needs the item and
        returns nothing.

    dequeue()

    :   removes the front item from the queue. It needs no parameters
        and returns the item. The queue is modified.

    isEmpty()

    :   tests to see whether the queue is empty. It needs no parameters
        and returns a boolean value.

    size()

    :   returns the number of items in the queue. It needs no parameters
        and returns an integer.

    In comments, describe the running time of each method of your
    implementation.

3.  A *deque* is a "double-ended queue." It combines the features of a
    stack and a queue. Implement a deque in python. It should have the
    following methods:

    Deque()

    :   creates a new deque that is empty. It needs no parameters and
        returns an empty deque.

    addFront(item)

    :   adds a new item to the front of the deque. It needs the item and
        returns nothing.

    addRear(item)

    :   adds a new item to the rear of the deque. It needs the item and
        returns nothing.

    removeFront()

    :   removes the front item from the deque. It needs no parameters
        and returns the item. The deque is modified.

    removeRear()

    :   removes the rear item from the deque. It needs no parameters and
        returns the item. The deque is modified.

    isEmpty()

    :   tests to see whether the deque is empty. It needs no parameters
        and returns a boolean value.

    size()

    :   returns the number of items in the deque. It needs no parameters
        and returns an integer.

    In comments, describe the running time of each method of your
    implementation.

4.  Now that we're more experienced making our own data structures,
    we'll build a new type of list, called a linked list. Linked lists
    are made up of nodes. Each node contains one list element, along
    with a link to the next node in the list. (Hence the name.) Create a
    `Linked_List` object that implements a linked list. It should use a
    helper class `Node`. It should implement the following methods:

    Linked_List()

    :   creates a new list that is empty. It needs no parameters and
        returns an empty list.

    add(item)

    :   adds a new item to the beginning of the list. It needs the item
        and returns nothing.

    remove(item)

    :   removes the item from the list. It needs the item and modifies
        the list. If the item isn't in the list, it raises an error.

    search(item)

    :   searches for the item in the list. It needs the item and returns
        a boolean value.

    isEmpty()

    :   tests to see whether the list is empty. It needs no parameters
        and returns a boolean value.

    size()

    :   returns the number of items in the list. It needs no parameters
        and returns an integer.

    append(item)

    :   adds a new item to the end of the list making it the last item
        in the collection. It needs the item and returns nothing.

    index(item)

    :   returns the position of item in the list. It needs the item and
        returns the index. If the item isn't in the list, it raises an
        error.

    insert(pos,item)

    :   adds a new item to the list at position `pos`. It needs the item
        and returns nothing. If the list is too short, then it raises an
        error.

    pop()

    :   removes and returns the last item in the list. It needs nothing
        and returns an item. If the list is empty, it raises an error.

    popfrom(pos)

    :   removes and returns the item at position pos. It needs the
        position and returns the item. If the list is too short, then it
        raises an error.

5.  A *Doubly-linked list* is just like a linked list, except that each
    node is linked in two directions---to the following node, and to the
    previous node. The head of the list should be linked both to the
    beginning and to the end. Thus, it allows traversal in both
    directions. Implement a doubly-linked list.

6.  Do you think that python's internal representation of a list is a
    linked-list, a doubly-linked list, or something else? Why or why
    not? Insert a comment in your code to explain your thinking about
    this.

7.  Now that you've implemented linked lists and doubly-linked lists,
    you have the option of using these in place of python lists inside
    your implementation of stacks, queues, and dekes. For each of these,
    explain which type of list (python list, linked list, or
    doubly-linked list) should give the best Big Oh running time in a
    comment.
