from tkinter import *
import tkinter.ttk as ttk
from texts import small_rus, medium_rus, large_rus, small_eng, medium_eng, large_eng

ws = Tk()
ws.title('Typing Test')
ws.geometry('700x400')
ws['bg'] = 'gray22'

language = ''
choose_text = ''


def ch_language(selection):
    global language
    if selection == 'Russian':
        language = 'rus'
    elif selection == 'English':
        language = 'eng'


def finish_typing(entry):
    result.grid_forget()
    text_output = entry.get(1.0, END)
    entry.grid_forget()
    mistakes = 0
    choose_text_split = []
    for i in choose_text:
        choose_text_split.append(i)
    text_split_symbols = []
    for i in text_output:
        text_split_symbols.append(i)
    text_split_words = text_output.replace(', ', ' ').replace('. ', ' ').replace(' - ', ' ').replace('(', '').replace(
        ')', '').replace('-', ' ').split(' ')
    if text_split_symbols[0] == '\n':
        symbols_in_min = 0
        words_in_min = 0
        mistakes = len(choose_text_split)
    else:
        words_in_min = len(text_split_words) // int(clicked1.get())
        text_split_symbols.remove('\n')
        symbols_in_min = len(text_split_symbols) // int(clicked1.get())
        for i in range(len(choose_text_split)):
            try:
                if choose_text_split[i] != text_split_symbols[i]:
                    mistakes += 1
            except IndexError:
                mistakes += 1
    result.configure(text=f'Symbols per minute: {symbols_in_min}, Words per minute: {words_in_min}, Mistakes: {mistakes}')
    result.grid(row=5, column=3, pady=20, sticky=N)


def start_typing():
    if clicked1.get() != '' and clicked.get() != '' and clicked2.get() != '':
        entry = Text(ws, height=30, width=50)
        entry.grid(row=5, column=3, pady=20, sticky=N)
        ws.after(60000 * int(clicked1.get()), lambda: finish_typing(entry))


def texts_size(selection):
    global text, choose_text
    if language == 'rus':
        if selection == 'Small':
            text.config(text=small_rus)
            choose_text = small_rus
        elif selection == 'Medium':
            text.config(text=medium_rus)
            choose_text = medium_rus
        elif selection == 'Large':
            text.config(text=large_rus)
            choose_text = large_rus
    elif language == 'eng':
        if selection == 'Small':
            text.config(text=small_eng)
            choose_text = small_eng
        elif selection == 'Medium':
            text.config(text=medium_eng)
            choose_text = medium_eng
        elif selection == 'Large':
            text.config(text=large_eng)
            choose_text = large_eng

    text.grid(row=5, column=1, pady=20)


result = ttk.Label(ws, text='', style='BW.TLabel', wraplength=300)

text = ttk.Label(ws, text='', style='BW.TLabel', wraplength=900, justify=LEFT)

style_bold = ttk.Style()
style_bold.configure('Bold.TLabel', background='gray22', foreground='white', font=('Sans', '30', 'bold'))
style_normal = ttk.Style()
style_normal.configure('BW.TLabel', background='gray22', foreground='white', font=('Sans', '12', 'normal'))
style_button = ttk.Style()
style_button.configure('Bold.TButton', font=('Sans', '12', 'normal'))

title = ttk.Label(ws, text='Typing Speed Test', style='Bold.TLabel').grid(row=0, column=1)
language_label = ttk.Label(ws, text='Choose language:', style='BW.TLabel').grid(row=1, column=0, pady=20, sticky=W)
options = ['', 'English', 'Russian']
clicked = StringVar()
clicked.set(options[0])
select_language = ttk.OptionMenu(ws, clicked, *options, command=ch_language).grid(row=1, column=2)

time_label = ttk.Label(ws, text='Choose time in minutes: ', style='BW.TLabel').grid(row=2, column=0, pady=20, sticky=W)
options1 = ['', '1', '2', '3', '4', '5']
clicked1 = StringVar()
clicked1.set(options1[0])
select_time = ttk.OptionMenu(ws, clicked1, *options1).grid(row=2, column=2)

text_size = ttk.Label(ws, text='Text size: ', style='BW.TLabel').grid(row=3, column=0, pady=20, sticky=W)
options2 = ['', 'Small', 'Medium', 'Large']
clicked2 = StringVar()
clicked2.set(options2[0])
select_size = ttk.OptionMenu(ws, clicked2, *options2, command=texts_size).grid(row=3, column=2)

start = ttk.Button(ws, text='Start', width=15, style='Bold.TButton', command=start_typing).grid(row=4, column=1)

ws.mainloop()
