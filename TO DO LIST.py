from tkinter import *
from tkinter.font import Font
from tkinter import filedialog
import pickle

root = Tk()
root.title("ROHIT - ToDo List!")

# define our font
my_font = Font(
    family="Lucida Calligraphy Italic ",
    size=20,
    weight="bold")


my_frame = Frame(root)
my_frame.pack(pady=10)

# Create listbox
my_list = Listbox(my_frame,
                  font=my_font,
                  width=29,
                  height=5,
                  bg="SystemButtonFace",
                  bd=0,
                  fg="#C00000",
                  highlightthickness=0,
                  selectbackground="#a6a6a6",
                  activestyle="none"
                  )


my_list.pack(side=LEFT, fill=BOTH)

# CREATE SCROLLBAR
my_scrollbar = Scrollbar(my_frame)
my_scrollbar.pack(side=RIGHT, fill=BOTH)


# ADD SCROLLBAR
my_list.config(yscrollcommand=my_scrollbar.set)
my_scrollbar.config(command=my_list.yview)

# CREATE ENTRY BOX TO ADD ITEMS INTO THE LIST
my_entry = Entry(root, font=("Helvetica", 25), width=26)
my_entry.pack(pady=20)
# CREATE A BUTTON FRAME
button_frame = Frame(root)
button_frame.pack(pady=20)

#    FUNCTIONS


def delete_item():
    my_list.delete(ANCHOR)


def add_item():
    my_list.insert(END, my_entry.get())
    my_entry.delete(0, END)


def mark_as_done_item():
    my_list.itemconfig(
        my_list.curselection(),
        fg="#000000")


# GET RID OF SELECTION BAR
my_list.selection_clear(0, END)


def mark_as_incomplete_item():
    my_list.itemconfig(
        my_list.curselection(),
        fg="#C00000")


# GET RID OF SELECTION BAR
my_list.selection_clear(0, END)


def remove_done_item():
    count = 0
    while count < my_list.size():
        if my_list.itemcget(count, "fg") == "#000000":
            my_list.delete(my_list.index(count))
        else:
            count += 1


def save_list():
    file_name = filedialog.asksaveasfilename(
        initialdir="D:\PYTHON CODES",
        title="Save File",
        filetypes=(
            ("Dat Files", "*.dat"),
            ("All Files", "*.*"))
    )
    if file_name:
        if file_name.endswith(".dat"):
            pass
        else:
            file_name = f'{file_name}.dat'
#  DELETE MARK AS DONE ITEMS BEFORE SAVING
        count = 0
        while count < my_list.size():
            if my_list.itemcget(count, "fg") == "#000000":
                my_list.delete(my_list.index(count))
            else:
                count += 1
        # TAKE ALL THE DATA FROM THE LIST
        stuff=my_list.get(0, END)
        # OPEN THE FILE
        output_file=open(file_name,'wb')
        #  ACTUALLY ADD THE STUFF TO THE FILE
        pickle.dump(stuff, output_file)


def open_list():
    file_name=filedialog.askopenfilename(
         initialdir="D:\PYTHON CODES",
        title="Open File",
        filetypes=(
            ("Dat Files", "*.dat"),
            ("All Files", "*.*"))
    )
    if file_name:
        # DELETE CURRENTLY OPEN LIST
        my_list.delete(0, END)

        # OPEN THE FILE
        input_file=open(file_name, 'rb')

        #  LOAD THE THE DATA FROM THE FILE
        stuff=pickle.load(input_file)

        #  OUTPUT STUFF TO THE SCREEN
        for item in stuff:
            my_list.insert(END, item)

    
def delete_list():
    my_list.delete(0, END)


#  CREATE MENU
my_menu = Menu(root)
root.config(menu=my_menu)


# ADD ITEMS TO THE MENU
file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="File", menu=file_menu)


#   ADD DROPDOWN ITEMS
file_menu.add_command(label="save list", command=save_list)
file_menu.add_command(label="open list", command=open_list)
file_menu.add_separator()
file_menu.add_command(label="clear list", command=delete_list)


# ADD SOME BUTTONS
delete_button = Button(button_frame, text=" Delete Item", command=delete_item)
add_button = Button(button_frame, text=" Add Item", command=add_item)
mark_as_done_button = Button(
    button_frame, text=" Mark as done ", command=mark_as_done_item)
mark_as_incomplete_button = Button(
    button_frame, text=" Mark_as_incomplete ", command=mark_as_incomplete_item)
remove_done_item_button = Button(
    button_frame, text=" Delete completed Item", command=remove_done_item)


delete_button.grid(row=0, column=0)
add_button.grid(row=0, column=1, padx=20)
mark_as_done_button.grid(row=0, column=2)
mark_as_incomplete_button.grid(row=0, column=3, padx=20)
remove_done_item_button.grid(row=0, column=4)


root.mainloop()
