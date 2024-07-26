import tkinter as tk

counter = 0
running = False

def counter_label(label):
    def count():
        if running:
            global counter
            if counter == 0:
                display = "Starting..."
            else:
                display = str(counter)
            label['text'] = display
            label.after(1000, count)
            counter += 1
    count()

def start():
    global running
    running = True
    counter_label(label)
    start_button['state'] = 'disabled'
    stop_button['state'] = 'normal'
    reset_button['state'] = 'normal'

def stop():
    global running
    running = False
    start_button['state'] = 'normal'
    stop_button['state'] = 'disabled'
    reset_button['state'] = 'normal'

def reset():
    global counter
    counter = 0
    if not running:
        reset_button['state'] = 'disabled'
        label['text'] = 'Welcome!'
    else:
        label['text'] = 'Starting...'

root = tk.Tk()
root.title('Stopwatch')

label = tk.Label(root, text='Welcome!', fg='black', font='Verdana 30 bold')
label.pack()

start_button = tk.Button(root, text='Start', width=15, command=start)
start_button.pack()

stop_button = tk.Button(root, text='Stop', width=15, state='disabled', command=stop)
stop_button.pack()

reset_button = tk.Button(root, text='Reset', width=15, state='disabled', command=reset)
reset_button.pack()

root.mainloop()
