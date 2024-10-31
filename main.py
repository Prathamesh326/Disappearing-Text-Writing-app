from tkinter import *
import tkinter.messagebox
import ttkbootstrap as ttk 

user_text = ""
timer = None

# Functions
def start_calculating(event):
    global timer, user_text
    if timer is not None:
        window.after_cancel(timer)

    if event.keysym == "BackSpace":
        user_text = user_text[0: len(user_text) - 1]
    elif event.char:
        user_text += event.char
        timer = window.after(5000, reset_app)
    return

def reset_app():
    global timer, user_text̥̥̥
    typing_area.delete('1.0', 'end')
    user_text = ""
    timer = None
    status_var.set("Text cleared after 5 seconds of inactivity.")
    return

def save_text():
    global timer, user_text
    if user_text == "":
        return
    try:
        f = open('writeups.txt', 'r')
    except FileNotFoundError:
        f = open('writeups.txt', 'w')
        f.write(user_text)
        tkinter.messagebox.showinfo("Confirmation",  "Your text is saved successfully!")
        status_var.set("Text saved successfully!")
        user_text = ""
        return
    else:
        con = f.read()
        if con == "":
            text_to_write = user_text
        else:
            text_to_write = f'\n{user_text}'
        
        with open('writeups.txt', 'a') as f:
            f.write(text_to_write)
            tkinter.messagebox.showinfo("Confirmation",  "Your text is saved successfully!")
            status_var.set("Text saved successfully!")
            user_text = ""
    finally:
        return



#=======UI SETUP========#
window = ttk.Window(themename='cosmo')
window.title('Disappearing Text Desktop App')
window.geometry('900x600')

# fonts and colors
BORDER_COLOR = "#D3D3D3"
BG_COLOR = "#F5F5F5"
FG_COLOR = "#333333"
ACCENT_COLOR = "#0D6EFD"
FONT_MAIN = ('Helvetica', 14, 'bold')
FONT_INSTRUCTION = ('Helvetica', 10, 'italic')

# heading
heading = ttk.Label(
    window,
    text="WRITE WITH MAGICAL INK",
    font=('Helvetica', 24, 'bold'),
    background=BG_COLOR,
    foreground=FG_COLOR
    )
heading.pack(pady=(20, 10))

# instructions
instruction = ttk.Label(
    window,
    text = "If you don't press any key for 5 seconds, the text you have written will disappear",
    font=FONT_INSTRUCTION,
    background=BG_COLOR,
    foreground=FG_COLOR
)
instruction.pack()

# Typing area
typing_area = Text(
    window,
    font=FONT_MAIN,
    bg=BG_COLOR,
    fg=FG_COLOR,
    width=90,
    height=15,
    wrap='word',
    highlightthickness=2,
    highlightbackground=BORDER_COLOR,
    relief=FLAT,
    padx=10,
    pady=10
)
typing_area.bind('<KeyPress>', start_calculating)
typing_area.pack(pady=10)

# Buttons
button_frame = Frame(window, bg=BG_COLOR)
button_frame.pack(pady=10)

reset_btn = ttk.Button(
    button_frame,
    text='Reset',
    style='primary.TButton',
    command=reset_app,
    width=20
)
reset_btn.grid(row=0, column=0, padx=10, pady=10)

save_btn = ttk.Button(
    button_frame,
    text='Save',
    style='success.TButton',
    command=save_text,
    width=20
)
save_btn.grid(row=0, column=1, padx=10, pady=10)

# Status bar
status_var = StringVar()
status_var.set("Welcome to the Disappearing Text App.")
status_bar = ttk.Label(
    window,
    textvariable=status_var,
    font=('Helvetica', 10), 
    background=BG_COLOR,
    foreground=FG_COLOR,
    anchor=W
)
status_bar.pack(side=BOTTOM, fill=X, padx=5, pady=5)

window.config(bg=BG_COLOR)
window.mainloop()