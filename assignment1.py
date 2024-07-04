def line():
    print("\n~~~~~~~~~~~~~~~~~~~~~\n")

class Order():
    def __init__(self, meals, table):
        self.meals = meals
        self.table = table
        self.next = None
        self.prev = None

class Kitchen():
    def __init__(self):
        self.head = None
        self.tail = None
    
    def add_order(self, meals, table):
        new_order = Order(meals, table)
        if self.head == None:
            self.head = new_order
            self.tail = new_order
        else:
            self.tail.next = new_order
            new_order.prev = self.tail
            self.tail = new_order
    
    def view_order(self):
        current = self.head
        while current:
            print(f"Table No. {current.table} has an order of {current.meals}")
            current = current.next
    
    def cook_order(self):
        if self.tail == None:
            return "No Orders Pending to be cooked"
        else:
            cooked_order = self.head #Removing the head and assigning to this new variable
            self.head = self.head.next
            if self.head == None:
                self.tail = None
            return (f"Order Cooked Table Number = {cooked_order.table}, Meal Cooked = {cooked_order.meals}")
    
    def delete_order(self, table):
        if self.head == None:
            return "No Orders to Delete"
        current_table = self.head.table
        current = self.head
        while current.table != table:
            # current_table = current_table.next
            # print(f"Table Current : {current.table}")
            current = current.next
        # print(f"Table Current : {current.table}")
        # print(f"Current.next = {current.next.table}")
        if current.next == None:
            deleted = current
            self.tail = deleted.prev
            self.tail.next = None
            return f"Order for Table Number {deleted.table} has been deleted"
        elif current.prev == None:
            deleted = current
            self.head = deleted.next
            return f"Order for Table Number {deleted.table} has been deleted"
        else:
            deleted = current
            # print(f"Current is {current.table}")
            current.next.prev = current.prev
            current.prev.next = current.next
            # print(f"Current previous = {current.prev.table}")
            # print(f"Current Next = {current.next.table}")
            return f"Order for Table Number {deleted.table} has been deleted"

        
    def insert(self, idx, meals, table):
        new_order = Order(meals, table)
        count = 1
        current = self.head
        while count < idx:
            current = current.next
            count += 1
        new_order.next = current.next
        new_order.prev = current
        current.next = new_order
        new_order.next.prev = new_order

kitchen = Kitchen()

kitchen.add_order(["pancake", "eggs", "hashbrown"], 1)
kitchen.add_order(["pancake", "egg"], 10)
kitchen.add_order(["pancake", "egg"], 12)
kitchen.view_order()
line()
kitchen.insert(2, ["pancake", "blah"], 20)
kitchen.view_order()
line()
print(kitchen.delete_order(1))
kitchen.view_order()
# print(kitchen.cook_order())
# print(kitchen.cook_order())
# kitchen.view_order()
# print(kitchen.cook_order())
kitchen.view_order()
print(kitchen.cook_order())
print(kitchen.cook_order())
kitchen.view_order()
print(kitchen.cook_order())
kitchen.view_order()
print(kitchen.cook_order())
kitchen.view_order()