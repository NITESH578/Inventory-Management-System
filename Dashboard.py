from tkinter import *
from PIL import Image, ImageTk
from datetime import datetime
from employee import employeeClass
from supplier import supplierClass
from category import categoryClass
from product  import productClass
from sales import salesClass
from billing import BillClass
from tkinter import filedialog
import sqlite3
from tkinter import messagebox
import os
class IMS:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Inventory Management System | Developed By Nitesh Yadav")
        self.root.config(bg="snow")
        self.icon_title = PhotoImage(file=r"C:\Users\NITESH\images\logo1.png")

        title = Label(
        self.root,text="Inventory Managment System",image=self.icon_title,compound=LEFT,font=("times new roman", 40, "bold"),bg="sienna",fg="linen",anchor="w",padx=20)
        title.place(x=0, y=0, relwidth=1, height=70)

        

        # Create the clock label
        current_datetime = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        self.lbl_clock = Label(self.root,text=f"Welcome to Inventory Management System \t\t\t\t\t\t\t\t\t\t\t\t Date: {current_datetime}\t\t",font=("times new roman", 15),bg="peru",fg="white",anchor="sw" )       
        self.lbl_clock.place(x=0, y=70, relwidth=1, height=30)

        # Create LeftMenu frame
        menu_logo_path = r"C:\Users\NITESH\images\menu_im.png"
        self.MenuLogo = Image.open(menu_logo_path)
        self.MenuLogo = self.MenuLogo.resize((200, 200))
        self.MenuLogo = ImageTk.PhotoImage(self.MenuLogo)

        self.LeftMenu = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        self.LeftMenu.place(x=0, y=102, width=200, height=565)

        lbl_menu_logo = Label(self.LeftMenu, image=self.MenuLogo)
        lbl_menu_logo.pack(side=TOP, fill=X)

        self.icon_side = PhotoImage(file=r"C:\Users\NITESH\images\side.png")
        lbl_menu = Label(self.LeftMenu, text="Menu", font=("times new roman", 20), bg="#009688")
        lbl_menu.pack(side=TOP, fill=X)

        btn_employee = Button(self.LeftMenu, text="Employee",command=self.employee,image=self.icon_side,compound=LEFT,padx=5,anchor="w", font=("times new roman", 20, "bold"), bg="white", bd=3, cursor="hand2").pack(side=TOP, fill=X)
        btn_supplier = Button(self.LeftMenu, text="Supplier",command=self.supplier,image=self.icon_side,compound=LEFT,padx=5,anchor="w", font=("times new roman", 20, "bold"), bg="white", bd=3, cursor="hand2").pack(side=TOP, fill=X) 
        btn_category = Button(self.LeftMenu, text="Category",command=self.category,image=self.icon_side,compound=LEFT,padx=5,anchor="w", font=("times new roman", 20, "bold"), bg="white", bd=3, cursor="hand2").pack(side=TOP, fill=X) 
        btn_product = Button(self.LeftMenu, text="Products",command=self.product,image=self.icon_side,compound=LEFT,padx=5,anchor="w", font=("times new roman", 20, "bold"), bg="white", bd=3, cursor="hand2").pack(side=TOP, fill=X)
        btn_sales = Button(self.LeftMenu, text="Sales",command=self.sales,image=self.icon_side,compound=LEFT,padx=5,anchor="w", font=("times new roman", 20, "bold"), bg="white", bd=3, cursor="hand2").pack(side=TOP, fill=X) 
        btn_billing = Button(self.LeftMenu, text="Billing",command=self.billing,image=self.icon_side,compound=LEFT,padx=5,anchor="w", font=("times new roman", 20, "bold"), bg="white", bd=3, cursor="hand2").pack(side=TOP, fill=X) 

        self.lbl_employee=Label(self.root,text="Total Employee\n[ 0 ]",bd=5,relief=RIDGE,bg="steelblue",fg="black",font=("goudy old style",20,"bold"))
        self.lbl_employee.place(x=300,y=120,height=150,width=300)

        self.lbl_supplier=Label(self.root,text="Total Supplier\n[ 0 ]",bd=5,relief=RIDGE,bg="steelblue",fg="black",font=("goudy old style",20,"bold"))
        self.lbl_supplier.place(x=650,y=120,height=150,width=300)

        self.lbl_category=Label(self.root,text="Total Category\n[ 0 ]",bd=5,relief=RIDGE,bg="steelblue",fg="black",font=("goudy old style",20,"bold"))
        self.lbl_category.place(x=1000,y=120,height=150,width=300)

        self.lbl_product=Label(self.root,text="Stocks In Hand\n[ 0 ]",bd=5,relief=RIDGE,bg="steelblue",fg="black",font=("goudy old style",20,"bold"))
        self.lbl_product.place(x=300,y=300,height=150,width=300)
 
        self.lbl_sales=Label(self.root,text="Sales Outward\n[ 0 ]",bd=5,relief=RIDGE,bg="steelblue",fg="black",font=("goudy old style",20,"bold"))
        self.lbl_sales.place(x=650,y=300,height=150,width=300)

        lbl_footer = Label(self.root,text="",font=("times new roman", 12),bg="saddlebrown",fg="white").pack(side=BOTTOM,fill=X)
        
        self.update_content()


    def employee(self):
        self.new_win=Toplevel(self.root)   
        self.new_obj=employeeClass(self.new_win)

    def supplier(self):
        self.new_win=Toplevel(self.root)   
        self.new_obj=supplierClass(self.new_win)

    def category(self):
        self.new_win=Toplevel(self.root)   
        self.new_obj=categoryClass(self.new_win)

    def product(self):
        self.new_win=Toplevel(self.root)   
        self.new_obj=productClass(self.new_win)

    def sales(self):
        self.new_win=Toplevel(self.root)   
        self.new_obj=salesClass(self.new_win)

    def billing(self):
        self.new_win=Toplevel(self.root)   
        self.new_obj=BillClass(self.new_win)


    def update_content(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            cur.execute("select * from product")
            product=cur.fetchall()
            self.lbl_product.config(text=f'Total Product\n[ { str(len(product))} ]')

            cur.execute("select * from supplier")
            supplier=cur.fetchall()
            self.lbl_supplier.config(text=f'Total Supplier\n[ { str(len(supplier))} ]')

            cur.execute("select * from category")
            category=cur.fetchall()
            self.lbl_category.config(text=f'Total Category\n[ { str(len(category))} ]')

            cur.execute("select * from employee")
            employee=cur.fetchall()
            self.lbl_employee.config(text=f'Total Employee\n[ { str(len(employee))} ]')
            bill=len(os.listdir('bill'))
            self.lbl_sales.config(text=f'Total Sales [{str(bill)}]')

            
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to:{str(ex)}",parent=self.root)

        self.lbl_clock.after(1000,self.update_content)

        
if __name__ == "__main__":
    root = Tk()
    obj = IMS(root)
    root.mainloop()