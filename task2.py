import re
from functools import partial
from tkinter import *
from tkinter import ttk, messagebox
#importpymysql

# User Credentials
db_host = "localhost"
db_user = "root"
db_password = "your_password"
db_name = "contact_book"

primary_color = "medium sea green"
secondary_color = "light goldenrod yellow"
text_color = "black"
background_color = "ivory"
warning_color = "firebrick"
success_color = "forest green"
primary_font = "calibri"
secondary_font = "helvetica"

columns = ("first_name", "last_name", "address", "contact", "email")

class MyContactApp:
    def __init__(self, root):
        self.window = root
        self.window.title("My Contact App")
        self.window.geometry("940x480")
        self.window.config(bg=background_color)

        # Customization
        self.primary_color = primary_color
        self.secondary_color = secondary_color
        self.text_color = text_color
        self.background_color = background_color
        self.warning_color = warning_color
        self.success_color = success_color
        self.primary_font = primary_font
        self.secondary_font = secondary_font
        self.columns = columns

        # User Credentials
        self.db_host = db_host
        self.db_user = db_user
        self.db_password = db_password
        self.db_name = db_name

        # Left Frame
        self.frame_left = Frame(self.window, bg=primary_color)
        self.frame_left.place(x=0, y=0, width=740, relheight=1)

        # Right Frame
        self.frame_right = Frame(self.window, bg=secondary_color)
        self.frame_right.place(x=740, y=0, relwidth=1, relheight=1)

        # Buttons
        self.add_new_btn = Button(self.frame_right, text='Add New', font=(primary_font, 12), bd=2, command=self.add_contact, cursor="hand2", bg=secondary_color, fg=text_color)
        self.add_new_btn.place(x=50, y=40, width=100)

        self.display_btn = Button(self.frame_right, text='Display', font=(primary_font, 12), bd=2, command=self.display_contacts, cursor="hand2", bg=secondary_color, fg=text_color)
        self.display_btn.place(x=50, y=100, width=100)

        self.search_btn = Button(self.frame_right, text='Search', font=(primary_font, 12), bd=2, command=self.search_contact, cursor="hand2", bg=secondary_color, fg=text_color)
        self.search_btn.place(x=50, y=160, width=100)

        self.clear_btn = Button(self.frame_right, text='Clear', font=(primary_font, 12), bd=2, command=self.clear_screen, cursor="hand2", bg=secondary_color, fg=text_color)
        self.clear_btn.place(x=50, y=340, width=100)

        self.exit_btn = Button(self.frame_right, text='Exit', font=(primary_font, 12), bd=2, command=self.exit_app, cursor="hand2", bg=secondary_color, fg=text_color)
        self.exit_btn.place(x=50, y=400, width=100)

    def selected_contact(self, event):
        self.update_btn = Button(self.frame_right, text='Update', font=(primary_font, 12), bd=2, command=self.update_contact, cursor="hand2", bg=success_color, fg=text_color)
        self.update_btn.place(x=50, y=220, width=100)

        self.delete_btn = Button(self.frame_right, text='Delete', font=(primary_font, 12), bd=2, command=self.delete_contact, cursor="hand2", bg=warning_color, fg=text_color)
        self.delete_btn.place(x=50, y=280, width=100)

    def display_contacts(self):
        self.clear_screen()

        scroll_x = ttk.Scrollbar(self.frame_left, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(self.frame_left, orient=VERTICAL)
        self.tree = ttk.Treeview(self.frame_left, columns=self.columns, height=400, selectmode="extended", yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
        scroll_y.config(command=self.tree.yview)
        scroll_y.pack(side=LEFT, fill=Y)
        scroll_x.config(command=self.tree.xview)
        scroll_x.pack(side=BOTTOM, fill=X)

        for column in self.columns:
            self.tree.heading(column, text=column.capitalize(), anchor=W)

        self.tree.pack()
        self.tree.bind('<Double-Button-1>', self.selected_contact)

        try:
            connection = pymysql.connect(host=self.db_host, user=self.db_user, password=self.db_password, database=self.db_name)
            curs = connection.cursor()
            curs.execute("select * from contact_register")
            rows = curs.fetchall()

            if rows:
                for index, row in enumerate(rows):
                    self.tree.insert("", 'end', text=(index + 1), values=row)
            else:
                messagebox.showinfo("Database Empty", "There is no data to show", parent=self.window)

            connection.close()
        except Exception as e:
            messagebox.showerror("Error!", f"Error due to {str(e)}", parent=self.window)

    def show_contacts(self, rows):
        self.clear_screen()

        scroll_x = ttk.Scrollbar(self.frame_left, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(self.frame_left, orient=VERTICAL)
        self.tree = ttk.Treeview(self.frame_left, columns=self.columns, height=400, selectmode="extended", yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
        scroll_y.config(command=self.tree.yview)
        scroll_y.pack(side=LEFT, fill=Y)
        scroll_x.config(command=self.tree.xview)
        scroll_x.pack(side=BOTTOM, fill=X)

        for column in self.columns:
            self.tree.heading(column, text=column.capitalize(), anchor=W)

        self.tree.pack()
        self.tree.bind('<Double-Button-1>', self.selected_contact)

        for index, row in enumerate(rows):
            self.tree.insert("", 'end', text=(index + 1), values=row)

    def add_contact(self):
        pass  # Add your implementation here

    def update_contact(self):
        pass  # Add your implementation here

    def delete_contact(self):
        pass  # Add your implementation here

    def search_contact(self):
        pass  # Add your implementation here

    def clear_screen(self):
        pass  # Add your implementation here

    def exit_app(self):
        pass  # Add your implementation here

if __name__ == "__main__":
    root = Tk()
    app = MyContactApp(root)
    root.mainloop()
