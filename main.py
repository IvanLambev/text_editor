import tkinter
from tkinter import filedialog
import io

file = None


## create the main window
root = tkinter.Tk()
root.title("Text Editor")
root.geometry("600x400")

## create the menu
menu = tkinter.Menu(root)
root.config(menu=menu)

#logic part
def check_shortcuts(event):
    # Check if the Ctrl and S keys are both pressed
    if event.state == 0x4 and event.keysym == 's':

        save_file()
    # Check if the Ctrl and O keys are both pressed
    if event.state == 0x4 and event.keysym == 'o':
        open_file()

    # Check if the Ctrl and N keys are both pressed
    if event.state == 0x4 and event.keysym == 'n':
        new_file()

    # Check if the Ctrl and Q keys are both pressed
    if event.state == 0x4 and event.keysym == 'q':
        root.quit()


def new_file():
    # delete the current text
    text.delete("1.0", tkinter.END)

def open_file():
    global file
    # delete the current text
    text.delete("1.0", tkinter.END)
    # open the file dialog
    file_path = tkinter.filedialog.askopenfilename(parent=root, title='Select a file')
    if file_path != '':
        with open(file_path, 'r') as file:
            contents = file.read()
            text.insert('1.0', contents)
            file.close()
        # save the file path
        file = file_path

def save_file():
    global file
    if file is None:
        file = save_as_file()
    if file is not None:
        # slice off the last character from get, as an extra return is added
        data = text.get('1.0', tkinter.END+'-1c')
        file.seek(0)
        file.truncate()
        file.write(data)
        file.flush()
        file.close()



def save_as_file():
    file = tkinter.filedialog.asksaveasfile(mode='w')
    ## if the file is not empty save it
    if file != None:
        # slice off the last character from get, as an extra return is added
        data = text.get('1.0', tkinter.END+'-1c')
        file.write(data)
        file.close()
        return file # return the file object

def cut():
    text.event_generate("<<Cut>>")

def copy():
    text.event_generate("<<Copy>>")

def paste():
    text.event_generate("<<Paste>>")



## create the file menu
file_menu = tkinter.Menu(menu)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command= open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Save As", command=save_as_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

## create the edit menu
edit_menu = tkinter.Menu(menu)
menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_separator()
edit_menu.add_command(label="Cut", command=cut)
edit_menu.add_command(label="Copy", command=copy)
edit_menu.add_command(label="Paste", command=paste)




## create the text widget
text = tkinter.Text(root, width=600, height=400)
text.pack()


root.bind('<Key>', check_shortcuts)


## run the main loop
root.mainloop()
