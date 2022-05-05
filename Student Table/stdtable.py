import prettytable
from replit import clear
clear()


class Student:
    def __init__(self):
        self.name_lst = []
        self.mark_lst = []

    def student(self, num):

        for i in range(num):
            name = input("\nEnter the user name : ")
            mark = input("Enter the mark : ")
            self.name_lst.append(name)
            self.mark_lst.append(mark)

    def num_stud(self):
        number = int(input("Enter how many students : "))
        self.student(number)


class Createtable:
    def __init__(self, name, mark):
        self.name_ls = name
        self.mark_ls = mark

    def table(self):
        name = self.name_ls
        mark = self.mark_ls
        a = prettytable.PrettyTable()
        a.field_names = ["Student Name", "Marks"]
        for i in range(len(name)):
            a.add_row([name[i], mark[i]])
        print("\n")
        print(a)


student = Student()
student.num_stud()

table = Createtable(student.name_lst, student.mark_lst)
table.table()
