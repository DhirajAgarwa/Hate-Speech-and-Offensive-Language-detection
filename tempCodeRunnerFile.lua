
import tkinter as tk

def get_input():
    input_text = text_box.get("1.0", "end-1c")
    input_list = input_text.split("\n")
    print(input_list)

root = tk.Tk()
photo = tk.PhotoImage(file="C:\\Users\\aryan\\OneDrive\\Desktop\\hate_speech\\neither.png") 

label = tk.Label(root, image=photo)
label.pack()
text_box = tk.Text(root, width=40, height=10)
text_box.pack()

enter_button = tk.Button(root, text="Enter", command=get_input)
enter_button.pack()

root.mainloop()