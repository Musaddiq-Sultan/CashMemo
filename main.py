#-----Importing Modules-----#
from tkinter import *
from tkinter import filedialog, messagebox

#-----Creating Root Window-----#
root = Tk()
root.title("Cash Memo")
root.geometry("300x500")
root.resizable(0, 0)

#-----Creating Variables-----#
name = quantity = price = total = None

#-----Adding Functions-----#
def submit():
    # Get input values
    name = str(name_entry.get()).lstrip().rstrip()
    quantity = quantity_entry.get().replace(" ", "")
    price = price_entry.get().replace(" ", "")

    # Check for errors
    if name.lstrip().rstrip() == "":
        messagebox.showerror("Error", "Name can't be empty")
        return
    elif len(name) > 18:
        messagebox.showerror("Error", "Name can't be longer than 18 characters")
        return
    if not quantity.isnumeric():
        messagebox.showerror("Error", "Quantity must be a number")
        return
    if not price.isnumeric():
        messagebox.showerror("Error", "Price must be a number")
        return

    # Convert inputs to integers
    quantity = int(quantity)
    price = int(price)
    total = price * quantity

    # Clear input fields
    name_entry.delete(0, END)
    quantity_entry.delete(0, END)
    price_entry.delete(0, END)

    # Display input values in message box
    display_message(f"Item Name: {name}")
    display_message(f"Quantity: {quantity}")
    display_message(f"Unit Price: {price}")
    display_message(f"Total Price: {total}")
    display_message("")

def display_message(message):
    # Inserts message into listbox widget
    listbox.insert(END, message)

def export_results():
    items = listbox.get(0, END)
    text = "\n".join(items)

    filetypes = (
        ("Text Files", "*.txt"),
        ("All Files", "*.*")
    )

    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt", 
        filetypes=filetypes
    )

    with open(file_path, "w") as file:
        file.write(text)

def clear_results():
    listbox.delete(0, END)

#-----Creating Frames-----#
frame_01 = Frame(root)
frame_02 = Frame(root)
frame_03 = Frame(root)
frame_04 = LabelFrame(root, text="Data")
frame_05 = Frame(root)

#-----Creating Labels-----#
item_name = Label(frame_01 ,text="Item Name")
item_quantity = Label(frame_02, text="Quantity")
item_price = Label(frame_03, text="Unit Price")

#-----Creating Entries-----#
name_entry = Entry(frame_01)
quantity_entry = Entry(frame_02)
price_entry = Entry(frame_03)

#-----Creating Listbox-----#
scrollbar = Scrollbar(frame_04)
listbox = Listbox(frame_04 ,yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

#-----Creating Buttons-----#
submit_button = Button(frame_05, text="Submit", command=submit)
clear_button = Button(frame_05, text="Clear", command=clear_results)
export_button = Button(frame_05, text="Export", command=export_results)

#-----Adding Widgets-----#
frame_01.pack(fill="both", padx=5, pady=5)
frame_02.pack(fill="both", padx=5, pady=(0, 5))
frame_03.pack(fill="both", padx=5, pady=(0, 5))
frame_04.pack(fill="both", expand=True, padx=5, pady=(0, 5))
frame_05.pack(fill="both", padx=5, pady=(0, 5))

item_name.pack(side="left")
name_entry.pack(side="right")

item_quantity.pack(side="left")
quantity_entry.pack(side="right")

item_price.pack(side="left")
price_entry.pack(side="right")

listbox.pack(side="left",fill="both", expand=True, padx=2, pady=(0,2))
scrollbar.pack(side="right", fill="y")

clear_button.grid(padx=(0, 5), row=0, column=0, sticky="ew")
export_button.grid(padx=(0, 5), row=0, column=1, sticky="ew")
submit_button.grid(row=0, column=2, sticky="ew")

for i in range(3):
    frame_05.columnconfigure(i, weight=1)

root.mainloop()