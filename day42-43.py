#Day 42-43 of 100
#Python Project: Email Slicer, spearates domain name and server name of an email

import tkinter as tk

window = tk.Tk()
window.geometry("480x440")
window.config(bg="blue")
window.resizable(width=False, height=False)
window.title('Python Project')


def result():
    try:
        email = entry.get()
        inp_email = email.strip()
        username = inp_email[0:inp_email.index('@')]
        domain = inp_email[inp_email.index('@') + 1:]
        text_box.delete('1.0', tk.END)
        msg = 'Email entered was: {}\n username: {}\nAnd domain server: {}'
        msg_formatted = msg.format(email, username, domain)
        text_box.insert(tk.END, msg_formatted)
        entry.delete(0, 'end')
    except:
        text_box.delete('1.0', tk.END)
        text_box.insert(tk.END, "ERROR!")


def reset_all():
    text_box.delete('1.0', tk.END)
    entry.delete(0, 'end')


# Labels in program
greeting = tk.Label(text="Day 42-43 of 100: Email Slicer!", font=(12), foreground="white", background="grey")
Info = tk.Label(foreground="white", background="grey", font=(10),
                text="Enter email id !\n The application will extract your username and domain name.")
entry_label = tk.Label(foreground="white", font=(10), background="black", text="Enter Email Id: ")
result_label = tk.Label(font=(10), foreground="white", background="black", text="There:")
empty_label0 = tk.Label(background="blue")
empty_label1 = tk.Label(background="blue")
empty_label2 = tk.Label(background="blue")
empty_label3 = tk.Label(background="blue")
empty_label4 = tk.Label(background="blue")
empty_label5 = tk.Label(background="blue")

#enter the email..
e1 = tk.StringVar()
entry = tk.Entry(font=(11), width=50, justify='center', textvariable=e1)

# Buttons
button = tk.Button(text="Done!", command=result, font=(11))
reset = tk.Button(text="Reset!", command=reset_all, font=(11))

# Result
text_box = tk.Text(height=5, width=50)

# Packing Everything Together
empty_label0.pack()
greeting.pack()
Info.pack()
empty_label1.pack()
entry_label.pack()
empty_label4.pack()
entry.pack()
empty_label2.pack()
button.pack()
empty_label5.pack()
reset.pack()
empty_label3.pack()
result_label.pack()
text_box.pack()

window.mainloop()
