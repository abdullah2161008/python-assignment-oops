#!/usr/bin/env python
# coding: utf-8

# OPPs Assignment

# Bank Account Create a class representing a bank account with attributes like account number, account holder name, and balance. Implement methods to deposit and withdraw money from the account.

# In[1]:


class BankAccount:
    def __init__(self,account_num,acc_holder_name,balance=1000):
        self.account_num=account_num
        self.acc_holder_name=acc_holder_name
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
    def with_draw(self,amount):
        if self.balance>=amount:
            return self.balance
person=BankAccount(12343,"Abdullah")
acc_holder_name=person.acc_holder_name
print(f"The account holder name is {acc_holder_name}")
account_num=person.account_num
print(f"The account number is {account_num} ")


# In[ ]:





# Problem 2: Employee Management Create a class representing an employee with attributes like employee ID, name, and salary. Implement methods to calculate the yearly bonus and display employee details.

# In[2]:


class Employee:
    def __init__(self,employee_id,name,salary):
        self.employee_id=employee_id
        self.name=name
        self.e_salary=salary

    def calculate_yearly_bonus(self, bonus_percentage):
        if bonus_percentage >= 0 and bonus_percentage <= 100:
            bonus_amount = (bonus_percentage / 100) * self.e_salary
            return bonus_amount
        else:
            print("invalid input")
    def employee_details(self):
        print(f"Employee id :{self.employee_id}, Employee name :{self.name},Employee salary: {self.e_salary}")
person=Employee(123,"abdullah",20000)
bonus_percentage=13
bonus_amount=person.calculate_yearly_bonus(bonus_percentage)
print(f"yearly Bonus is {bonus_amount}")
person.employee_details()


# In[ ]:





# Vehicle Rental Create a class representing a vehicle rental system. Implement methods to rent a vehicle, return a vehicle, and display available vehicles.

# In[3]:


class vehicle_rental_system:
    def rent_a_vehicle(self):
        print("I want to rent a vehicle")
    def return_a_vehicle(self):
        print("i want to return a vehicle")
    def available_vehicle(self):
        print("we have 10 cars for rent")

customer=vehicle_rental_system()
customer.return_a_vehicle()
customer.return_a_vehicle()
customer.available_vehicle()


# In[ ]:





# Library Catalog Create classes representing a library and a book. Implement methods to add books to the library, borrow books, and display available books.

# In[1]:


class library:
    def __init__(self,available_books):
        self.__available_books=available_books
    def add_book(self,amount_book):
        self.__available_books=self.__available_books+amount_book
    def borrow_book(self,amount):
        if self.__available_books>=amount:
            self.__available_books=self.__available_books-amount
            return True
        else:
            return False
    def num_of_aval_books(self):
        return self.__available_books

sudh=library(20)
sudh.borrow_book(10)
print(sudh.num_of_aval_books())
sudh.add_book(10)
print(sudh.num_of_aval_books())


# In[ ]:





# Product Inventory Create classes representing a product and an inventory system. Implement methods to add products to the inventory, update product quantity, and display available products.

# In[1]:


class Product:
    def __init__(self, id, name, price, quantity):
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity


class Inventory:
    def __init__(self):
        self.products = {}

    def add_product(self, product):
        self.products.setdefault(product.id, product)

    def update_product(self, product_id, new_quantity):
        self.products.get(product_id, Product(product_id, '', 0, 0)).quantity = new_quantity

    def display_available_products(self):
        available_products = [p for p in self.products.values() if p.quantity > 0]
        message = "Available Products:\n" + "\n".join([f"{p.name} (ID: {p.id}) - Price: ${p.price} - Quantity: {p.quantity}" for p in available_products])
        print(message if available_products else "No available products in the inventory")

# Example usage:
inventory = Inventory()

product1 = Product(1, "Laptop", 999.99, 10)
product2 = Product(2, "Smartphone", 499.99, 15)

inventory.add_product(product1)
inventory.add_product(product2)

inventory.display_available_products()

print("\nUpdating product quantity...")
inventory.update_product(1, 5)

inventory.display_available_products()


# In[ ]:





# Shape Calculation Create a class representing a shape with attributes like length, width, and height. Implement methods to calculate the area and perimeter of the shape.

# In[2]:


class Shape_box:
    def __init__(self,lenght,width,height):
        self.lenght=lenght
        self.width=width
        self.height=height
    def Square_area(self):
        surface_area=2*(self.lenght*self.width+self.width*self.height+self.height*self.lenght)
        return surface_area
    def cal_perimeter(self):
        perimeter=4*(self.lenght+self.width+self.height)
        return perimeter
sudh=Shape_box(12,4,8)
print(f"Area of Square-{sudh.Square_area()}")
print(f"Perimeter of Square-{sudh.cal_perimeter()}")


# In[ ]:





# Student Management Create a class representing a student with attributes like student ID, name, and grades. Implement methods to calculate the average grade and display student details.

# In[3]:


class Student:
    def __init__(self,student_id,name):
        self.student_id=student_id
        self.name=name
        self.grades=[]
    def add_grades(self,grade):
        self.grades.append(grade)
    def cal_avg_grade(self):
        if not self.grades:
            return 0
        return sum(self.grades)/len(self.grades)
    def display_student_details(self):
        print(f"Student ID :{self.student_id}")
        print(f"Name :{self.name}")
        print(f"Average Grade :{self.cal_avg_grade():}")
student1=Student("S1001","Abdullah")
student1.add_grades(90)
student1.add_grades(85)
student1.add_grades(92)
student1.display_student_details()


# In[ ]:





# Email Management Create a class representing an email with attributes like sender, recipient, and subject. Implement methods to send an email and display email details.

# In[4]:


class Email:
    def __init__(self,sender,recipient,subject):
        self.sender=sender
        self.recipient=recipient
        self.subject=subject
        self.message=""
    def compose_email(self,message):
        self.message=message
    def end_email(self):
        if not self.message:
            print("email message is empty")
            return
        print("simulating email send")
        print("Email sent successfully")
    def display_email_details(self):
        print("Email Details:")
        print(f"Sender:{self.sender}")
        print(f"Recipient :{self.recipient}")
        print(f"Subject :{self.subject}")
email=Email("khan@example.com","ahmad@example.com","This is Abdullah khan love from Pakistan")
message="This is a test email message"
email.compose_email(message)
email.display_email_details()


# In[ ]:





# Social Media Profile Create a class representing a social media profile with attributes like username and posts. Implement methods to add posts, display posts, and search for posts by keyword.

# In[5]:


class socialmediaprofile:
    def __init__(self,username):
        self.username=username
        self.posts=[]
    def add_post(self,content):
        self.posts.append(content)
    def display_posts(self):
        if not self.posts:
            print(f"{self.username} has no posts yet.")
        else:
            print(f"posts by {self.username}:")
            for i,post in enumerate(self.posts,start=1):
                print(f"{i}.{post}")
    def search_posts(self, keyword):
        matching_posts = [post for post in self.posts if keyword in post]
        print(f"Posts by {self.username} containing '{keyword}':")
        for i, post in enumerate(matching_posts, start=1):
            print(f"{i}. {post}")
profile=socialmediaprofile("Abdullah9226")
profile.add_post("hello,this is my first post.")
profile.add_post("i am enjoying the day!")
profile.display_posts()
search_keyword="enjoying"
profile.search_posts(search_keyword)


# In[ ]:





# ToDo List Create a class representing a ToDo list with attributes like tasks and due dates. Implement methods to add tasks, mark tasks as completed, and display pending tasks.

# In[6]:


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})

    def mark_task_completed(self, task_name):
        for task in self.tasks:
            if task["task"] == task_name:
                task["completed"] = True

    def display_pending_tasks(self):
        pending_tasks = [task for task in self.tasks if not task["completed"]]
        if not pending_tasks:
            print("No pending tasks.")
        else:
            print("Pending Tasks:")
            for i, task in enumerate(pending_tasks, start=1):
                print(f"{i}. {task['task']}")

todo_list = ToDoList()

todo_list.add_task("Complete assignment")
todo_list.add_task("Buy groceries")
todo_list.add_task("Call the client")

todo_list.display_pending_tasks()

print("\nMarking 'Buy groceries' as completed...")
todo_list.mark_task_completed("Buy groceries")

todo_list.display_pending_tasks()


# In[ ]:




