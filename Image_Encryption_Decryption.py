import tkinter as tk
from tkinter import filedialog,messagebox
from PIL import Image
import numpy as np

def xor_encrypt_decrypt_image(input_image_path, output_image_path, key):
  try:
    image = Image.open(input_image_path)
    image_array = np.array(image)

    key = key % 256

    encrypted_array = image_array ^ key

    encrypted_image = Image.fromarray(encrypted_array.astype(np.uint8))
    encrypted_image.save(output_image_path)

    messagebox.showinfo("Success",f"Image processed and saved to {output_image_path}")
  except Exception as e:
     messagebox.showerror("Error",f"An error occurred:{str(e)}")
     

def browse_file():
  file_path =filedialog.askopenfilename(title="Select Image",filetypes=[("Image Files","*.png;*.jpg;*.jpeg;*.bmp")])
  if file_path:
    entry_file_path.delete(0,tk.END)
    entry_file_path.insert(0,file_path)

def encrypt_image():
  input_image_path = entry_file_path.get()
  key=int(entry_key.get())
  output_image_path= filedialog.asksaveasfilename(defaultextension=".png",filetypes=[("PNG files","*.png"),("All files","*.*")])
  if output_image_path:
    xor_encrypt_decrypt_image(input_image_path,output_image_path,key)

def decrypt_image():
   input_image_path=entry_file_path.get()
   key=int(entry_key.get())
   output_image_path= filedialog.asksaveasfilename(defaultextension=".png",filetypes=[("PNG files","*.png"),("All files","*.*")])
   if output_image_path:
     xor_encrypt_decrypt_image(input_image_path,output_image_path,key)

root=tk.Tk()
root.title("Image Encryptor/Decryptor")

label_file_path=tk.Label(root,text="Image file:")
label_file_path.grid(row=0,column=0,padx=10,pady=10)

entry_file_path=tk.Entry(root,width=40)
entry_file_path.grid(row=0,column=1,padx=10,pady=10)

button_browse=tk.Button(root,text="Browse",command=browse_file)
button_browse.grid(row=0,column=2,padx=10,pady=10)

label_key=tk.Label(root,text="Encryption key:")
label_key.grid(row=1,column=0,padx=10,pady=10)

entry_key=tk.Entry(root,width=40)
entry_key.grid(row=1,column=1,padx=10,pady=10)

button_encrypt=tk.Button(root,text="Encrypt",command=encrypt_image)
button_encrypt.grid(row=2,column=0,padx=10,pady=20)

button_decrypt=tk.Button(root,text="Decrypt",command=decrypt_image)
button_decrypt.grid(row=2,column=1,padx=10,pady=20)

root.mainloop()

  
