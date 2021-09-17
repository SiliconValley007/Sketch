import tkinter as tk
import cv2
from tkinter import ttk
from tkinter import filedialog as fd
from os import path
from tkinter import messagebox

#function to convert the image to a sketch
def convert():
    #get the file location from the tkinter entry box
    file_location = select_image_entry.get()
    #read the file from its location using the open cv imread() function
    image = cv2.imread(file_location)
    #converting the image to gray and inverting it ultimately resulting in an image that looks like a sketch
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    inverted_image = 255 - gray_image
    blurred = cv2.GaussianBlur(inverted_image, (21,21), 0)
    inverted_blurred = 255 - blurred
    pencil_sketch = cv2.divide(gray_image, inverted_blurred, scale=256.0)
    #editing the file name so the original image does not get overwritten.
    new_file_location = file_location[:-4]+"_sketch"+file_location[-4:]
    cv2.imwrite(new_file_location, pencil_sketch)
    #showing a message telling the user that the file was successfully converted into a sketch
    messagebox.showinfo('Success', 'Image Successfully Converted. File stored at ' +  new_file_location)

def selectfile():
    try:
        filename = fd.askopenfilename(initialdir="/", title="Select a File", filetypes=(("All", "*.*"), ("PNG", "*.png*"), ("JPG", "*.jpg*"), ("JPEG", "*.jpeg*")))
        select_image_entry.delete(0, "end")
        select_image_entry.insert(0, filename)
    except AttributeError:
        pass

root = tk.Tk()
root.title('Sketch')
root.resizable(False, False)
root.geometry('330x150')
root.configure(bg="#ffffff")

s = ttk.Style()
s.configure('TLabel', background='#ffffff')

select_image_label = ttk.Label(root, text="Sketch", padding=10, font=('Helvetica', 24), style="TLabel")
select_image_label.grid(column=0, row=0, columnspan = 3)
root.columnconfigure(0, weight = 1)
root.rowconfigure(0, weight = 1)

select_image_label = ttk.Label(root, text="Select a File  ", padding=10, style="TLabel")
select_image_label.grid(column=0, row=1, sticky=tk.W)

select_image_entry = ttk.Entry(root)
select_image_entry.grid(column = 1, row = 1, sticky=tk.W)

select_image_button = ttk.Button(root, text = "Select Image", command=selectfile, cursor="hand2")
select_image_button.grid(column = 2, row = 1, sticky=tk.W, padx=(10,10))

select_image_button = ttk.Button(root, text = "Convert", command=convert, cursor="hand2")
select_image_button.grid(column = 1, row = 2, pady=10)

root.mainloop()
