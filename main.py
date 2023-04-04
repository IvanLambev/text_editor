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

##Create the preference menu
preference_menu = tkinter.Menu(menu)
menu.add_cascade(label="Preference", menu=preference_menu)

preference_menu.add_command(label="Color")

##Create popup to select font
font_menu = tkinter.Menu(preference_menu)
preference_menu.add_cascade(label="Font", menu=font_menu)
font_menu.add_command(label="Arial", command= lambda: text.configure(font=("Arial", 12)))
font_menu.add_command(label="Times New Roman", command= lambda: text.configure(font=("Times New Roman", 12)))
font_menu.add_command(label="Courier New", command= lambda: text.configure(font=("Courier New", 12)))

##Create popup to select font size
font_size_menu = tkinter.Menu(preference_menu)
preference_menu.add_cascade(label="Font Size", menu=font_size_menu)
font_size_menu.add_command(label="10", command= lambda: text.configure(font=("Arial", 10)))
font_size_menu.add_command(label="12", command= lambda: text.configure(font=("Arial", 12)))
font_size_menu.add_command(label="14", command= lambda: text.configure(font=("Arial", 14)))
font_size_menu.add_command(label="16", command= lambda: text.configure(font=("Arial", 16)))
font_size_menu.add_command(label="18", command= lambda: text.configure(font=("Arial", 18)))
font_size_menu.add_command(label="20", command= lambda: text.configure(font=("Arial", 20)))

##Create popup to select font color
font_color_menu = tkinter.Menu(preference_menu)
preference_menu.add_cascade(label="Theme", menu=font_color_menu)
font_color_menu.add_command(label="Black", command= lambda: text.configure(background='black', foreground='white'))
font_color_menu.add_command(label="White", command= lambda: text.configure(background='white', foreground='black'))



## create the text widget
text = tkinter.Text(root, width=600, height=400)

text.pack()

##Create the status bar at the bottom of the window to display the number of characters and lines

status_bar = tkinter.Label(root, text="Line: 1 | Column: 1", bd=1, relief=tkinter.SUNKEN, anchor=tkinter.W)
status_bar.pack(side=tkinter.BOTTOM, fill=tkinter.X)

def update_status_bar(event):
    line, column = event.widget.index(tkinter.INSERT).split('.')
    status_bar.config(text="Line: {} | Column: {}".format(line, column))

text.bind('<KeyRelease>', update_status_bar)



root.bind('<Key>', check_shortcuts)


## run the main loop
root.mainloop()
