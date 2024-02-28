
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from data_using_prediction import trial
from tkinter import messagebox
import pyttsx3

def text_to_speech(text,rate=150):
    text=' '.join(text.split())
    engine=pyttsx3.init()
    engine.setProperty('rate',rate)
    engine.say(text)
    engine.runAndWait()
def get_input(event=None):
    input_text = text_entry.get("1.0", "end-1c")
    root.unbind_all('<Control-s>')
    if(len(input_text)==0):
        messagebox.showerror("Error!!!","Please Enter the Text !!!")
        root.bind_all('<Control-s>',get_input) # type: ignore
        return 0
    text_entry.delete("1.0", "end-1c")
    
    input_list=[]
    input_list.append(input_text)
    val=trial(input_list)
    hate_speech(input_text,val)

def hate_speech(input_text,val):
    text_box.destroy()
    enter_button.destroy()
    notebook.destroy()
    frame=tk.Frame(root,bg='#fbd2d8')
    text=""
    dict={0:"Hate Speech",1:"Offensive Language",2:"OK"} 
    rel_btn=tk.Button(root, text="Reload", command=des, bg="#fa6b5d", font=('Helvetica', 12, 'bold'))
    if(len(input_text)>170):
        text=f"'{input_text[:170]}'... is {dict[val]}"
    else:
        text=f"'{input_text}' is {dict[val]}"
    
    x=tk.Label(frame,text=text,font=('Helvetica', 11, 'italic'),fg='black',bg='#fbd2d8',wraplength=350,justify="center",anchor="center")
    img = ""
    if(val==1):
        img=Image.open("offensive.png")
        frame.place(x=453,y=10,width=350,height=100)
        x.place(x=0,y=2)
        rel_btn.place(x=630, y=280, width=140, height=35)
    elif(val==0):
        img=Image.open("hate_speech.png")
        frame.place(x=610,y=10,width=350,height=100)
        x.place(x=0,y=2)
        rel_btn.place(x=760, y=190, width=140, height=35)
    elif(val==2):
        frame.config(bg="#fddad6")
        x.config(bg="#fddad6")
        img=Image.open("neither.png")
        frame.place(x=515,y=180,width=300,height=150)
        x.place(x=0,y=2)
        rel_btn.place(x=580, y=335, width=140, height=35)
    photo = ImageTk.PhotoImage(img)
    image_label.config(image=photo)
    image_label.image=photo
    root.update_idletasks()
    text_to_speech(text)
    root.bind('<Control-e>', des) # type: ignore
    

def des(event=None):
    root.unbind_all('<Control-e>')
    global image_label,text_entry,text_box,enter_button,notebook
    style=ttk.Style()
    style.configure('TNotebook',background="#fddad6")
    style.configure('TNotebook.Tab', background='#fddad6', font=('Helvetica', 12, 'bold'))
    # load the image
    image = Image.open("neither.png")
    photo = ImageTk.PhotoImage(image)

    # create an image label
    image_label = tk.Label(root, image=photo)
    image_label.image = photo # keep a reference to the image to prevent it from being garbage collected
    image_label.place(x=0, y=0)

    # create a text box
    notebook = ttk.Notebook(root,style='TNotebook') 
    notebook.place(x=530, y=176, width=280, height=140)

    text_box = ttk.Frame(notebook,style='TNotebook.Tab') 
    notebook.add(text_box, text="Enter your Text")

    text_entry = tk.Text(text_box, width=30, height=10, wrap="word",font=('Helvetica', 11, 'bold'),bg="#fddad6") 
    text_entry.pack(expand=True, fill="both")
    text_entry.delete("1.0", "end-1c")

    # create an "Enter" button
    enter_button = tk.Button(root, text="Enter", command=get_input, bg="#fa6b5d", font=('Helvetica', 12, 'bold'))
    enter_button.place(x=600, y=330, width=140, height=35)
    root.bind_all('<Control-s>',get_input) # type: ignore
    label = tk.Label(root, text="i",font=('Helvetica', 15,'bold'),fg='black',bg="#fa6b5d")
    label.place(x=45,y=28)

    def on_enter(event):
        label.config(text="ctrl+s:- Enter\nctrl+e:- Reload")

    def on_leave(event):
        label.config(text="i")

    label.bind("<Enter>", on_enter)
    label.bind("<Leave>", on_leave)
    

if   __name__=="__main__":
    root = tk.Tk()
    root.title("Hate and Offensive Speech Detection")
    image_l = Image.open("logo.ico")
    image_l=image_l.resize((100,100))
    photo_l = ImageTk.PhotoImage(image_l)
    root.iconphoto(True,photo_l)
    root.geometry("966x750")
    root.resizable(False, False)
    
    des()
    root.mainloop()

