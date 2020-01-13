class SLNode:
    def __init__(self, value):
        self.value= value
        self.next= None

class SList:
    def __init__(self):
        self.head= None
        
    def add_to_front(self, val):        # added this line, takes a value
        new_node= SLNode(val)           # create a new instance of our Node class using the given value
        current_head= self.head         # save the current head in a variable
        new_node.next= current_head     # SET the new node's next TO the list's current head
        self.head= new_node             # SET the list's head TO the node we created in the last step
        return self                     # return self to allow for chaining

    def print_values(self):
        runner=self.head                # a pointer to the list's first node
        while(runner != None):          # iterating while runner is a node and not None
            print(runner.value)         # print the current node's value
            runner= runner.next         # set the runner to its neighbor
        return self                     # once the loop is done, return self to allow for chaining

    def add_to_back(self, val):         # accepts a value
        if self.head == None:           # if the list is empty
            self.add_to_front(val)      # run the add_to_front method
            return self                 # let's make sure the rest of this function doesn't happen if we add to the front
        
        new_node= SLNode(val)           # create a new instance of our Node class with the given value
        runner= self.head               # set an iterator to start at the front of the list
        while(runner.next != None):     # iterator until the iterator doesn't have a neighbor
            runner= runner.next         # increment the runner to the next node in the list
        runner.next= new_node           # increment the runner to the next node in the list
        return self                     # return self to allow for chaining

    def remove_from_front(self):
        runner=self.head
        if runner.next != None:
            print("self.head.value= (%s) is being removed from the singly linked list"%runner.value)
            self.head=runner.next
        return self

    def remove_from_back(self):
        runner= self.head
        if runner == None:
            return self
        elif runner.next == None:
            self.head= None
            return self
        else:
            while(runner.next.next != None):
                runner= runner.next
            runner.next= None
        return self
        
    def remove_val(self,val):
        runner= self.head
        if runner == None:
            return self
        elif runner.value == val:
            self.head= runner.next
            return self
        else:
            while runner.next != None and runner.next.value != val:
                runner= runner.next
            if runner.next == None:
                return self
            else:
                runner.next= runner.next.next
                return self
    
    def insert_at(self,val,n):
        nth_node= SLNode(n)
        runner= self.head
        if runner == None:
            self.head= nth_node
            return self
        elif runner.value == val:
            self.head.next= nth_node
            return self
        else:
            while runner.next != None and runner.next.value != val:
                runner= runner.next
            if runner.next == None:
                return self
            else:
                nth_node.next= runner.next.next
                runner.next.next= nth_node
                return self
    
my_list = SList()                       # create a new instance of a list
my_list.add_to_front("are").add_to_front("Linked lists").add_to_back("fun!").add_to_back("made").add_to_back("progress").insert_at('made','yes').print_values()# chaining, yeah!
