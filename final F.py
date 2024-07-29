import tkinter as tk
from tkinter import ttk
import sqlite3

def create_db():
    con = sqlite3.connect('client.db')
    cur = con.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS CUSTOMER (
                    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    customer_name TEXT NOT NULL,
                    customer_address TEXT NOT NULL,
                    payment_method TEXT NOT NULL
                   )''')
    cur.execute('''CREATE TABLE IF NOT EXISTS SALES (
                    sales_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    product_id TEXT NOT NULL,
                    outlet_id TEXT NOT NULL,
                    sales_date TEXT NOT NULL,
                    quantity_sold INTEGER NOT NULL,
                    unit_price REAL NOT NULL,
                    total_amount REAL NOT NULL,
                    distribution_id TEXT NOT NULL
                   )''')
    con.commit()
    con.close()

create_db()

class MyApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Value Addition Management System")
        self.attributes('-fullscreen', True)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (HomePage, NewWindow):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("HomePage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.config(bg='green')

        menubar = tk.Menu(self)
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Open")
        file_menu.add_command(label="Save")
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.controller.destroy)
        menubar.add_cascade(label="File", menu=file_menu)
        self.controller.config(menu=menubar)

        logo = tk.PhotoImage(file=r"C:\Users\Titus Mwendwa Simeon\PixelSee\Downloads\Green and White Circle Modern Organic Shop Logo.png")
        logo_label = tk.Label(self, image=logo, bg='lightblue')
        logo_label.image = logo
        logo_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        get_started_button = tk.Button(self, text="GET STARTED", command=lambda: controller.show_frame("NewWindow"), font=("Arial", 20, 'bold'), fg="violet", bg="red")
        get_started_button.place(relx=0.5, rely=0.5, anchor=tk.N, y=logo.height()//2 + 20)

        exit_button = tk.Button(self, text="Exit", command=self.controller.destroy, fg="orange", font=("Arial", 14))
        exit_button.place(relx=1.0, rely=1.0, anchor=tk.SE, x=-10, y=-10)

class NewWindow(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.config(bg='lightgreen')

        headinglabel = tk.Label(self, text="VALUE ADDITION MANAGEMENT SYSTEM", font=("times new roman", 30, 'bold'), bg='gray20', fg='gold', bd=12, relief=tk.GROOVE)
        headinglabel.pack(fill=tk.X)

        back_button = tk.Button(self, text="Back to Home", command=lambda: controller.show_frame("HomePage"))
        back_button.pack()

        main_frame = tk.Frame(self, bg='lightgreen')
        main_frame.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)

        sales_frame = tk.Frame(main_frame, bg='lightgreen', bd=2, relief=tk.GROOVE)
        sales_frame.pack(side=tk.LEFT, padx=20, pady=20, fill=tk.BOTH, expand=True)

        sales_button = tk.Label(sales_frame, text="SALES", font=("Arial", 24, 'bold'), fg='red', bg='lightgreen')
        sales_button.pack(pady=10)

        product_button = tk.Button(sales_frame, text="Product", font=("Arial", 14), command=self.toggle_table)
        product_button.pack(pady=10)

        self.add_product_frame = tk.Frame(sales_frame, bg='lightgreen')
        self.add_product_frame.pack(pady=20)

        self.sales_id_var = tk.StringVar()
        self.product_id_var = tk.StringVar()
        self.outlet_id_var = tk.StringVar()
        self.sales_date_var = tk.StringVar()
        self.quantity_sold_var = tk.StringVar()
        self.unit_price_var = tk.StringVar()
        self.total_amount_var = tk.StringVar()
        self.distribution_id_var = tk.StringVar()

        tk.Label(self.add_product_frame, text="Sales ID", bg='lightgreen').grid(row=0, column=0, padx=10, pady=5)
        tk.Entry(self.add_product_frame, textvariable=self.sales_id_var).grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self.add_product_frame, text="Product ID", bg='lightgreen').grid(row=0, column=2, padx=10, pady=5)
        tk.Entry(self.add_product_frame, textvariable=self.product_id_var).grid(row=0, column=3, padx=10, pady=5)

        tk.Label(self.add_product_frame, text="Outlet ID", bg='lightgreen').grid(row=1, column=0, padx=10, pady=5)
        tk.Entry(self.add_product_frame, textvariable=self.outlet_id_var).grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self.add_product_frame, text="Sales Date", bg='lightgreen').grid(row=1, column=2, padx=10, pady=5)
        tk.Entry(self.add_product_frame, textvariable=self.sales_date_var).grid(row=1, column=3, padx=10, pady=5)

        tk.Label(self.add_product_frame, text="Quantity Sold", bg='lightgreen').grid(row=2, column=0, padx=10, pady=5)
        tk.Entry(self.add_product_frame, textvariable=self.quantity_sold_var).grid(row=2, column=1, padx=10, pady=5)

        tk.Label(self.add_product_frame, text="Unit Price", bg='lightgreen').grid(row=2, column=2, padx=10, pady=5)
        tk.Entry(self.add_product_frame, textvariable=self.unit_price_var).grid(row=2, column=3, padx=10, pady=5)

        tk.Label(self.add_product_frame, text="Total Amount", bg='lightgreen').grid(row=3, column=0, padx=10, pady=5)
        tk.Entry(self.add_product_frame, textvariable=self.total_amount_var).grid(row=3, column=1, padx=10, pady=5)

        tk.Label(self.add_product_frame, text="Distribution ID", bg='lightgreen').grid(row=3, column=2, padx=10, pady=5)
        tk.Entry(self.add_product_frame, textvariable=self.distribution_id_var).grid(row=3, column=3, padx=10, pady=5)

        tk.Button(self.add_product_frame, text="Add Product", command=self.add_product).grid(row=4, columnspan=4, pady=10)

        delete_sales_button = tk.Button(sales_frame, text="Delete", font=("Arial", 14), command=self.delete_sales)
        delete_sales_button.pack(pady=10)

        sales_columns = ("sales_id", "product_id", "outlet_id", "sales_date", "quantity_sold", "unit_price", "total_amount", "distribution_id")
        
        self.sales_table_frame = tk.Frame(sales_frame)
        self.sales_table_frame.pack(fill=tk.BOTH, expand=True)
        
        self.sales_table = ttk.Treeview(self.sales_table_frame, columns=sales_columns, show='headings')

        for col in sales_columns:
            self.sales_table.heading(col, text=col)
            self.sales_table.column(col, anchor=tk.CENTER, width=100)

        self.sales_table.pack(fill=tk.BOTH, expand=True)
        self.sales_table.bind('<Double-1>', self.edit_sales_cell)

        customer_frame = tk.Frame(main_frame, bg='lightgreen', bd=2, relief=tk.GROOVE)
        customer_frame.pack(side=tk.LEFT, padx=20, pady=20, fill=tk.BOTH, expand=True)

        customer_button = tk.Label(customer_frame, text="CUSTOMERS", font=("Arial", 24, 'bold'), fg='red', bg='lightgreen')
        customer_button.pack(pady=10)

        self.customer_id_var = tk.StringVar()
        self.customer_name_var = tk.StringVar()
        self.customer_address_var = tk.StringVar()
        self.payment_method_var = tk.StringVar()

        tk.Label(customer_frame, text="Customer ID", bg='lightgreen').pack(pady=5)
        tk.Entry(customer_frame, textvariable=self.customer_id_var).pack(pady=5)

        tk.Label(customer_frame, text="Customer Name", bg='lightgreen').pack(pady=5)
        tk.Entry(customer_frame, textvariable=self.customer_name_var).pack(pady=5)

        tk.Label(customer_frame, text="Customer Address", bg='lightgreen').pack(pady=5)
        tk.Entry(customer_frame, textvariable=self.customer_address_var).pack(pady=5)

        tk.Label(customer_frame, text="Payment Method", bg='lightgreen').pack(pady=5)
        tk.Entry(customer_frame, textvariable=self.payment_method_var).pack(pady=5)

        tk.Button(customer_frame, text="Add Customer", command=self.add_customer).pack(pady=10)
        tk.Button(customer_frame, text="Delete Customer", command=self.delete_customer).pack(pady=10)

        customer_columns = ("customer_id", "customer_name", "customer_address", "payment_method")

        self.customer_table_frame = tk.Frame(customer_frame)
        self.customer_table_frame.pack(fill=tk.BOTH, expand=True)
        
        self.customer_table = ttk.Treeview(self.customer_table_frame, columns=customer_columns, show='headings')

        for col in customer_columns:
            self.customer_table.heading(col, text=col)
            self.customer_table.column(col, anchor=tk.CENTER, width=100)

        self.customer_table.pack(fill=tk.BOTH, expand=True)
        self.customer_table.bind('<Double-1>', self.edit_customer_cell)

        self.update_customer_table()
        self.update_sales_table()

    def toggle_table(self):
        if self.sales_table_frame.winfo_viewable():
            self.sales_table_frame.pack_forget()
        else:
            self.sales_table_frame.pack(fill=tk.BOTH, expand=True)

    def add_product(self):
        con = sqlite3.connect('client.db')
        cur = con.cursor()
        cur.execute("INSERT INTO SALES (product_id, outlet_id, sales_date, quantity_sold, unit_price, total_amount, distribution_id) VALUES (?, ?, ?, ?, ?, ?, ?)",
                    (self.product_id_var.get(), self.outlet_id_var.get(), self.sales_date_var.get(), self.quantity_sold_var.get(), self.unit_price_var.get(), self.total_amount_var.get(), self.distribution_id_var.get()))
        con.commit()
        con.close()
        self.update_sales_table()

    def delete_sales(self):
        selected_item = self.sales_table.selection()[0]
        sales_id = self.sales_table.item(selected_item, "values")[0]
        con = sqlite3.connect('client.db')
        cur = con.cursor()
        cur.execute("DELETE FROM SALES WHERE sales_id=?", (sales_id,))
        con.commit()
        con.close()
        self.sales_table.delete(selected_item)

    def update_sales_table(self):
        con = sqlite3.connect('client.db')
        cur = con.cursor()
        cur.execute("SELECT * FROM SALES")
        rows = cur.fetchall()
        self.sales_table.delete(*self.sales_table.get_children())
        for row in rows:
            self.sales_table.insert('', 'end', values=row)
        con.close()

    def edit_sales_cell(self, event):
        selected_item = self.sales_table.selection()[0]
        col = self.sales_table.identify_column(event.x)
        row = self.sales_table.identify_row(event.y)
        col_index = int(col.replace('#', '')) - 1
        entry_value = self.sales_table.item(selected_item, "values")[col_index]

        entry = tk.Entry(self.sales_table_frame)
        entry.insert(0, entry_value)
        entry.place(x=event.x_root - self.sales_table_frame.winfo_rootx(), y=event.y_root - self.sales_table_frame.winfo_rooty(), anchor="w")

        def save_edit(event):
            new_value = entry.get()
            self.sales_table.set(selected_item, column=col, value=new_value)
            entry.destroy()
            # Update the database with the new value
            columns = ["sales_id", "product_id", "outlet_id", "sales_date", "quantity_sold", "unit_price", "total_amount", "distribution_id"]
            column_name = columns[col_index]
            sales_id = self.sales_table.item(selected_item, "values")[0]
            con = sqlite3.connect('client.db')
            cur = con.cursor()
            cur.execute(f"UPDATE SALES SET {column_name} = ? WHERE sales_id = ?", (new_value, sales_id))
            con.commit()
            con.close()

        entry.bind('<Return>', save_edit)
        entry.focus()

    def add_customer(self):
        con = sqlite3.connect('client.db')
        cur = con.cursor()
        cur.execute("INSERT INTO CUSTOMER (customer_name, customer_address, payment_method) VALUES (?, ?, ?)",
                    (self.customer_name_var.get(), self.customer_address_var.get(), self.payment_method_var.get()))
        con.commit()
        con.close()
        self.update_customer_table()

    def delete_customer(self):
        selected_item = self.customer_table.selection()[0]
        customer_id = self.customer_table.item(selected_item, "values")[0]
        con = sqlite3.connect('client.db')
        cur = con.cursor()
        cur.execute("DELETE FROM CUSTOMER WHERE customer_id=?", (customer_id,))
        con.commit()
        con.close()
        self.customer_table.delete(selected_item)

    def update_customer_table(self):
        con = sqlite3.connect('client.db')
        cur = con.cursor()
        cur.execute("SELECT * FROM CUSTOMER")
        rows = cur.fetchall()
        self.customer_table.delete(*self.customer_table.get_children())
        for row in rows:
            self.customer_table.insert('', 'end', values=row)
        con.close()

    def edit_customer_cell(self, event):
        selected_item = self.customer_table.selection()[0]
        col = self.customer_table.identify_column(event.x)
        row = self.customer_table.identify_row(event.y)
        col_index = int(col.replace('#', '')) - 1
        entry_value = self.customer_table.item(selected_item, "values")[col_index]

        entry = tk.Entry(self.customer_table_frame)
        entry.insert(0, entry_value)
        entry.place(x=event.x_root - self.customer_table_frame.winfo_rootx(), y=event.y_root - self.customer_table_frame.winfo_rooty(), anchor="w")

        def save_edit(event):
            new_value = entry.get()
            self.customer_table.set(selected_item, column=col, value=new_value)
            entry.destroy()
            # Update the database with the new value
            columns = ["customer_id", "customer_name", "customer_address", "payment_method"]
            column_name = columns[col_index]
            customer_id = self.customer_table.item(selected_item, "values")[0]
            con = sqlite3.connect('client.db')
            cur = con.cursor()
            cur.execute(f"UPDATE CUSTOMER SET {column_name} = ? WHERE customer_id = ?", (new_value, customer_id))
            con.commit()
            con.close()

        entry.bind('<Return>', save_edit)
        entry.focus()

if __name__ == "__main__":
    app = MyApp()
    app.mainloop()
