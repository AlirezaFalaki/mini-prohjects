import random
import string

list_of_barcodes = []

def barcode_generator():
    while True:
        barcode_num = random.choices(string.digits, k=8)
        barcode_num = "".join(barcode_num)
        if barcode_num not in list_of_barcodes:
            list_of_barcodes.append(barcode_num)
            break
    return barcode_num

def calculate_median(list_of_costs):
    if len(list_of_costs) % 2 != 0:
        return list_of_costs[int(len(list_of_costs) / 2)]
    else:
        return (list_of_costs[int(len(list_of_costs) / 2)] + list_of_costs[int(len(list_of_costs) / 2) - 1]) / 2

class BST_tree:
    def __init__(self,val, name):
        self.leftChild = None
        self.rightChild = None
        self.val = val
        self.name = name
        self.barcode = None
        self.median = None
        self.list_of_costs = []
        
    def add_node(self, val, name):
        if not self.val:
            self.val = val
            self.barcode = barcode_generator()
            self.name = name
            self.list_of_costs.append(val)
            self.median = calculate_median(self.list_of_costs)
            return
        
        if val < self.val:
            if self.leftChild:
                self.leftChild.add_node(val, name)
                self.leftChild.barcode = barcode_generator()
                return
            
            self.leftChild=BST_tree(val, name)
            self.leftChild.barcode = barcode_generator()
            self.leftChild.list_of_costs.append(val)
            self.leftChild.median = calculate_median(self.leftChild.list_of_costs)
            return
        
        if self.rightChild:
            self.rightChild.add_node(val, name)
            self.rightChild.barcode = barcode_generator()
            return
        
        self.rightChild=BST_tree(val, name)
        self.rightChild.barcode = barcode_generator()
        self.rightChild.list_of_costs.append(val)
        self.rightChild.median = calculate_median(self.rightChild.list_of_costs)
    
    def search_node(self, val, name):
        if self.val == val and self.name == name:
            return self
        if val >= self.val and self.rightChild is not None:
            self = self.rightChild
            return self.search_node(val, name)
        if val < self.val and self.leftChild is not None:
            self = self.leftChild
            return self.search_node(val, name)
        return "Not Found."
    
    def delete_node(self, val, name):
        if self == None:
            return self
        if self.name == name: # These to ifs are for handling the equal nodes
            val = self.val
        if self.val == val and self.name != name:
            val += 1
        if val < self.val:
            if self.leftChild:
                self.leftChild = self.leftChild.delete_node(val, name)
            return self
        if val > self.val:
            if self.rightChild:
                self.rightChild = self.rightChild.delete_node(val, name)      
            return self
        if self.rightChild == None:
            return self.leftChild
        if self.leftChild == None:
            return self.rightChild
        
        MinLargerNode = self.rightChild
        while MinLargerNode.leftChild:
            MinLargerNode = MinLargerNode.leftChild 
        self.val = MinLargerNode.val
        self.name = MinLargerNode.name
        self.barcode = MinLargerNode.barcode
        self.list_of_costs = MinLargerNode.list_of_costs
        self.median = MinLargerNode.median
        self.rightChild = self.rightChild.delete_node(MinLargerNode.val, MinLargerNode.name)
        return self
    
    def GetMinInSubtree(self,val,name):          # مقدار ریشه زیر درخت را دریافت میکند 
        node=self.SearchNode(val,name)
        while node.leftChild  is not None:
            node = node.leftChild
        return node

    def Inorder(self,vals):
        if self.leftChild is not None:
            self.leftChild.Inorder(vals)
        if self.val is not None:
            vals.append(self)
        if self.rightChild is not None:
            self.rightChild.Inorder(vals)
        return vals
        
    def Preorder(self,vals):
        if self.val is not None:
            vals.append(self)
        if self.leftChild is not None:
            self.leftChild.Preorder(vals)
        if self.rightChild is not None:
            self.rightChild.Preorder(vals)
        return vals

    def Postorder(self,vals):
        if self.leftChild is not None:
            self.leftChild.Postorder(vals)
        if self.rightChild is not None:
            self.rightChild.Postorder(vals)
        if self.val is not None:
            vals.append(self)
        return vals

    def Lessthan(self,value):
        arr=[]
        tmp=self.Inorder(arr)
        res=[]
        for i in range(len(tmp)):
            if tmp[i].val < value:
                res.append(tmp[i])
        return res
    
    def Morethan(self,value):
        arr=[]
        tmp=self.Inorder(arr)
        res=[]
        for i in range(len(tmp)):
            if tmp[i].val > value:
                res.append(tmp[i])
        return res

    def BetweenValues(self,value1,value2):
        arr=[]
        tmp=self.Inorder(arr)
        res=[]
        for i in range(len(tmp)):
            if tmp[i].val <= value2 and tmp[i].val >= value1:
                res.append(tmp[i])
        return res
    
    def GetMaxInSubtree(self,val,name):
        node = self.SearchNode(val,name)
        while node.rightChild is not None:
            node = node.rightChild
        return node

        
    def __str__(self):
        return f"Product Name:{self.name}\nCost:{self.val}\nBarcode:{self.barcode}\nList of Costs:{self.list_of_costs}\nMedian:{self.median}\n" + "-" * 20
        
a = BST_tree(None, None)

def main_menu():
    print("-"*15)
    print("1.Add New Product")
    print("2.Choose a Product")
    print("3.Choose a Range of Products")
    print("4.Exit")
    print("-"*15)

def add_new_product():
    product_name = input("Enter the Name of the Product:")
    product_cost = int(input("Enter the Cost of the Product:"))
    a.add_node(product_cost, product_name)
    print("Product Successfully Added.")

def choose_product_menu():
    print("-"*15)
    print("1.Show Product")
    print("2.Change Cost")
    print("3.Delete Product")
    print("4.Show Cheaper Products")
    print("5.Show more Expensive Products")
    print("6.Back")
    print("-"*15)

def show_product(product):
    print(f"Product Name:{product.name}\nCost:{product.val}\nBarcode:{product.barcode}\nList of Costs:{product.list_of_costs}\nMedian:{product.median}\n" + "-" * 20) 

def change_cost(product):
    new_cost = int(input("Enter the new cost:"))
    temp_list = product.list_of_costs
    temp_barcode = product.barcode
    temp_list.append(new_cost)
    temp_name = product.name
    a.delete_node(product.val, temp_name)
    a.add_node(new_cost, temp_name)
    new_node = a.search_node(new_cost, temp_name)
    new_node.barcode = temp_barcode
    new_node.list_of_costs = temp_list
    new_node.median = calculate_median(new_node.list_of_costs)
    print("The cost have been changed successfully.")

def delete_product(product):
    a.delete_node(product.val, product.name)
    print("Product deleted successfully.")


def show_cheaper_products(val):
    products = a.Lessthan(val)
    for product in products:
        print(product)


def show_expensive_products(val):
    products = a.Morethan(val)
    for product in products:
        print(product)

def back_to_main_menu():
    return main_menu()

def second_switcher(sign, user_choice):
    if sign == '1':
        return show_product(user_choice)
    elif sign == '2':
        return change_cost(user_choice)
    elif sign == '3':
        return delete_product(user_choice)
    elif sign == '4':
        return show_cheaper_products(user_choice.val)
    elif sign == '5':
        return show_expensive_products(user_choice.val)
    elif sign == '6':
        return back_to_main_menu()
    else:
        print("Invalid input...\nPlease try again.")

def choose_product():
    while True:
        print("Choose your Product by Name and Cost:")
        print("(Enter 'back' in product name if you want go back to main menu.)")
        product_name = input("Enter the Product Name:")
        if product_name == 'back':
            return
        product_cost = int(input("Enter the Product Cost:"))
        user_choice = a.search_node(product_cost, product_name)
        if user_choice != "Not Found.":
            break
        else:
            print("Not Found.\nPlease try again.")
            print("-"*15)
    print("-"*15)
    while True:
        choose_product_menu()
        sign = input("Enter Your Choice:")
        print("-"*15)
        second_switcher(sign, user_choice)
        print("-"*15)
        if sign == '6' or '3':
            break

def choose_range_products():
    lower_bound = int(input("Enter the lower bound:"))
    upper_bound = int(input("Enter the upper bound:"))
    print("-"*15)
    products = a.BetweenValues(lower_bound, upper_bound)
    for product in products:
        print(product)

def switcher(sign):
    if sign == '1':
        return add_new_product()
    elif sign == '2':
        return choose_product()
    elif sign == '3':
        return choose_range_products()
    elif sign == '4':
        return exit()
    else:
        print("Invalid input...\nPlease try again.")


while True:
    main_menu()
    sign = input("Enter Your Choice:")
    print("-"*15)
    switcher(sign)


