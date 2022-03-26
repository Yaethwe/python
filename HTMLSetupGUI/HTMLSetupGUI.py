from Tkinter import *
import os
import sys
import zipfile
import webbrowser as wb

app = Tk()
app.title('HTML Setup GUI')
app.geometry('600x700')
app.resizable(width=False,height=True)
HTML_default='''
<!DOCTYPE html>
<html>
    <head>
        <link rel='stylesheet' href='style.css'>
        <meta charset='utf-8'>
        <title>Document</title>
    </head>
    <body>
        <h1>HelloWorld!</h1>
        <label>HTML Project Setup GUI</label><br>
        <label>Created By YeaeThawe</label><br>
        <label>yeaethawe@gmail.com</label><br>
    </body>
    <script src='script.js'></script>
</html>
'''
CSS_default='''
body{
  background-color:gray;
  color:white;
}
h1{
  font-family:sans-serif;
  color:white;
}
label{
  font-family:sans-serif;
  color:white;
}
'''
JS_default='''
const body = document.querySelector('body');
'''
def webso():
    wb.open('https://gardennet.netlify.app/explorer?gid=2&gname=HTMLsetupGUI')
def unzip(h,t):
    with zipfile.ZipFile(h, 'r') as zip_ref:
        zip_ref.extractall(t)
def close():
    sys.exit()
def create(f, value):
    with open(f,'w') as fi:
        fi.write(value);
def setup():
    create('index.html',html_t.get(1.0,END))
    create('style.css',css_t.get(1.0,END))
    create('script.js',js_t.get(1.0,END))
    setupSuccessful()
def newpage():
    html_t.delete(1.0, END)
    css_t.delete(1.0, END)
    js_t.delete(1.0, END)
def default():
    newpage()
    html_t.insert(1.0, HTML_default)
    css_t.insert(1.0, CSS_default)
    js_t.insert(1.0, JS_default)
def setupSuccessful():
    ss = Tk()
    ss.title('Setup Successful')
    ss.geometry('400x200')
    ssl = Label(ss,text="Setup Successful",fg='orange',font=('sans-serif',20))
    btn = Button(ss,text='OK',bg='blue',fg='white',command=ss.destroy)
    ssl.pack()
    btn.pack()
    ss.mainloop()
def fileCreatorGUI():
    fc = Tk()
    l=Label(fc,text='File Creator',fg='blue',font=('sans-serif',20))
    f=Frame(fc)
    def createin():
        e=ent1.get()
        create(e,'')
        slab.config(text='"'+e+'" was created successfully.',fg='blue')
    fc.title('File Creator')
    fc.geometry('400x200')
    ent1 = Entry(f,width=25)
    btn1 = Button(f,text='create',command=createin)
    slab = Label(f,text='')
    ent1.grid(column=0,row=0)
    btn1.grid(column=1,row=0)
    slab.grid(column=0,row=1 )
    l.pack()
    f.pack()
    fc.mainloop()
def unzipGUI():
    fc = Tk()
    l=Label(fc,text='Unzipper',fg='blue',font=('sans-serif',20))
    f=Frame(fc)
    def unzipin():
        e=ent1.get()
        unzip(e,'./')
        slab.config(text='"'+e+'" was unzipped successfully.',fg='blue')
    fc.title('Unzipper')
    fc.geometry('400x200')
    ent1 = Entry(f,width=25)
    btn1 = Button(f,text='unzip',command=unzipin)
    slab = Label(f,text='')
    ent1.grid(column=0,row=0)
    btn1.grid(column=1,row=0)
    slab.grid(column=0,row=1 )
    l.pack()
    f.pack()
    fc.mainloop()
menubar = Menu(app)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New Page", command=newpage)
filemenu.add_command(label="Restore Default", command=default)
filemenu.add_command(label="Setup", command=setup)
filemenu.add_command(label="File Creator", command=fileCreatorGUI)
filemenu.add_command(label="Unzipper", command=unzipGUI)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=close)
menubar.add_cascade(label="File", menu=filemenu)
infomenu = Menu(menubar, tearoff=0)
infomenu.add_command(label="Website", command=webso)
menubar.add_cascade(label="Info", menu=infomenu)
app.config(menu=menubar)
html_l = Label(app, text="HTML")
html_t = Text(app, width=60, height=10)
css_l = Label(app, text="CSS")
css_t = Text(app, width=60, height=10)
js_l = Label(app, text="JS")
js_t = Text(app, width=60, height=10)
setupBtn = Button(app,text='setup',bg='gray',fg='white',activebackground='pink',activeforeground='orange',font=('sans-serif',20),padx=0,pady=5,command=setup)

html_l.pack()
html_t.pack()
css_l.pack()
css_t.pack()
js_l.pack()
js_t.pack()
setupBtn.pack()
#create('')
default()
app.mainloop()

