class SLNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class SList:
    def __init__(self):
        self.head = None
    def add_to_front(self, val):	# added this line, takes a value
        new_node = SLNode(val)
        current_head = self.head
        new_node.next = current_head
        self.head = new_node
        return self
    def print_values(self):
            runner = self.head
            while (runner != None):
                print(runner.value)
                runner = runner.next 	# set the runner to its neighbor
            return self
    def add_to_back(self, val):
            if not self:	# if the list is empty
                self.add_to_front(val)	# run the add_to_front method
                return self	# let's make sure the rest of this function doesn't happen if we add to the front
            new_node = SLNode(val)
            runner = self.head
            while (runner.next != None):
                runner = runner.next
            runner.next = new_node	# increment the runner to the next node in the list
            return self 
    def remove_from_front(self):
        if not self:
            return self
        runner = self.head
        self.head = self.head.next
        runner = None
        return self
    def remove_from_back(self):
        if not self:
            return self
        if self.head.next == None:
            self.head == None
            return self
        runner = self.head
        while(runner.next.next):
            runner = runner.next
        runner.next = None
        return self
    def remove_val(self, val):
        runner = self.head
        if runner is not None:
            if runner.value == val:
                self.head = runner.next
                runner = None
                return
        while runner is not None:
            if runner.value == val:
                break
            holder = runner
            runner = runner.next
        if runner == None:
            return
        holder.next = runner.next
        runner = None
        return self
    def insert_at(self, val, n):
        if not self:
            return self
        new_Node = SLNode(val)
        if n == 0:
            new_Node.next = self.head
            self.head.next = new_Node.next.next
            self.head = new_Node
            print(str(new_Node.next.value) + '\n')
            return self
        runner = self.head
        for i in range(n-1):
            runner = runner.next
        new_Node.next = runner.next
        runner.next = new_Node
        return self

new_List = SList()
new_List.add_to_front(5).add_to_front(6).add_to_front(7).add_to_back(4).add_to_front(8).add_to_front(9).add_to_front(10).add_to_back(3).print_values()
print("\n")
new_List.remove_from_front().remove_from_back().remove_val(5).insert_at(15,0)
new_List.print_values()