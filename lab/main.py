from Tkinter import *
app = Tk()
app.title('Lab')
app.geometry('600x400')
app.config(bg='black')
app.resizable(width=False,height=False)
challenge='''
Can you resize this window?
'''
c = Label(app, text=challenge, bg='black', fg='white', font=('sans-serif',10))
c.pack()
app.mainloop()
