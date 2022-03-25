import os
global mode
mode=None
html_text='''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
<center>
<h1>Hello World!</h1>
<h2>Created By YeaeThawe</h2>
</center>
</body>
<script src="script.js"></script>
</html>
'''
yt_css_text='''
body{
    background-color:black;
    color:white;
}
'''
yt_js_text='''
// JavaScript
'''
def create():
    os.system('type nul > index.html')
    os.system('type nul > style.css')
    os.system('type nul > script.js')
def print_self():
    with open('setup.py', 'r') as f:
        f_contents = f.read()
        print(f_contents)
def write(m):
    if m is 'yt':
        with open('index.html', 'w') as f:
            f.write(html_text)
        with open('style.css', 'w') as f:
            f.write(yt_css_text)
        with open('script.js', 'w') as f:
            f.write(yt_js_text)
    elif m is 'blank':
        create()
        pass
    elif m is 'linked':
        create()
        with open('index.html', 'w') as f:
            f.write(html_text)
    else:
        print('Your mode '+m+' is not exist.')
def start():
    print('HTML Setup\nVersion 0.1.0\nCreated by YeaeThawe at 10:38 AM 3/25/2022\nContent\nyeaethawe@gmail.com\nyeaethawe@outlook.com\n')
    print('Select a mode or press Enter to choose default mode\nModes\n<1> blank (only create blank HTML,CSS and JavaScript files)\n<2> linked (create linked HTML,CSS and JavaScript files)\n<3> yt (default mode)\n<4> print_self to print the source code of setup.py\n')
    q=input()
    if q == "": 
        global mode
        mode = 'yt'
        write(mode)
    elif q is 'print_self':
        print_self()
        input('press any keys to continue :')
        start()
    else:
        mode = q
        write(q)
start()
input('press any keys to close :')
