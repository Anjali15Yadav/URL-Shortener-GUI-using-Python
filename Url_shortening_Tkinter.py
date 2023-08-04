# Importing tkinter and pyshorteners.
import tkinter as tk
import pyshorteners

# Creating root window
root=tk.Tk()
# Giving window a name/title
root.title("URL Shortener")
# Defining window size
root.geometry("600x600")

# Creating an input String variable
url_var  = tk.StringVar()

# Defining the URL shortener function which uses "pyshorteners" library.
def shorten_url(url):
    s=pyshorteners.Shortener()
    short_url =s.tinyurl.short(url)
    return short_url

# Defining submit button function
def submit():
    global sh,output_url
    url = url_var.get()
    sh=shorten_url(url)
    
    # Output the shortened URL by using an Entry widget in such a way,so we can copy it.
    output_var = tk.StringVar()
    output_var.set(sh)
    output_url.config(textvariable = output_var)

    url_var.set("")

# Creating Labels,Buttons, and Entry widgets.
url_label = tk.Label(root,text = "Enter URL to be shortened:")
url_entry = tk.Entry(root,text = url_var,font = ('calibre',10,'normal'))
sub_button = tk.Button(root,text = "Submit",command = submit)
output_label = tk.Label(root,text = "Shortened URL:")

# Griding all the widgets on the root window.
url_label.grid(row = 0, column = 0)
url_entry.grid(row = 0, column =1)
sub_button.grid(row = 0, column = 2)
output_label.grid(row = 1, column = 0)

# The method to output the resultant URL.
output_url = tk.Entry(root, font =("Helvetica",10),bd = 0)
output_url.config(state = "readonly")       #Key point- Keep the Entry widget in "Readonly" mode.
output_url.grid(row = 1, column = 1)

# Run the application until the user stops it by closing it or interrupting using keyboard.
root.mainloop()
