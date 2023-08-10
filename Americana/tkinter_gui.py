import tk


def change_text():
    label.config(text="Button clicked!")


root = tk.Tk()
root.title("Interactive GUI Example")

label = tk.Label(root, text="Hello, Tkinter!")
label.pack()

button = tk.Button(root, text="Click Me", command=change_text)
button.pack()

root.mainloop()
