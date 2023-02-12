from tkinter import *
from tkinter import ttk, messagebox
from googletrans import Translator, LANGUAGES
import textblob

main = Tk()
main.title("Copa Translator App")
main.geometry("1080x400")

# Translate function
def translate_btn():
    text_to_translate = text1.get(1.0, END)
    source_language = lang_value[lang1.index(combo1.get())]
    target_language = lang_value[lang1.index(combo2.get())]

    if text_to_translate:
        words = textblob.TextBlob(text_to_translate)
        source_lan = words.detect_language()
        words = words.translate(from_lang=source_lan, to=target_language)
        text2.delete(1.0, END)
        text2.insert(END, words)


# Icon
icon = PhotoImage(file="icon.png")
main.iconphoto(False, icon)

# Translation arrow
arrow = PhotoImage(file="arrow2.png")
arrow_label = Label(main, image=arrow, width=150)
arrow_label.place(x=460, y=50)

# Supported languages
lang = textblob.LANGUAGES
lang1 = list(lang.keys())
lang_value = list(lang.values())

# Source language combobox
combo1 = ttk.Combobox(main, values=lang1, font="Roboto 14", state="readonly")
combo1.place(x=110, y=20)
combo1.set("english")

# Source language label
label1 = Label(
    main,
    text="ENGLISH",
    font="segeo 30 bold",
    bg="white",
    width=18,
    bd=5,
    relief="groove",
)
label1.place(x=10, y=50)

# Source text frame
frame1 = Frame(main, bg="black", bd=5)
frame1.place(x=10, y=118, width=440, height=210)

# Source text widget
text1 = Text(frame1, font="Roboto 20", bg="white", relief="groove", wrap="word")
text1.place(x=0, y=0, width=430, height=200)

# Source text scrollbar
scrollbar1 = Scrollbar(frame1)
scrollbar1.pack(side="right", fill="y")
scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)

# Target language combobox
combo2 = ttk.Combobox(main, values=lang1, font="Roboto 14", state="readonly")
combo2.place(x=730, y=20)
combo2.set("select language")

label2 = Label(
    main,
    text="ENGLISH",
    font="segeo 30 bold",
    bg="white",
    width=18,
    bd=5,
    relief=GROOVE,
)
label2.place(x=620, y=50)


frame2 = Frame(main, bg="black", bd=5)
frame2.place(x=620, y=118, width=440, height=210)

text2 = Text(frame2, font="Roboto 20", bg="white", relief=GROOVE, wrap=WORD)
text2.place(x=0, y=0, width=430, height=200)

scrollbar2 = Scrollbar(frame2)
scrollbar2.pack(side="right", fill="y")
scrollbar2.configure(command=text2.yview)
text2.configure(yscrollcommand=scrollbar2.set)

# Translate Button
translate = Button(
    main,
    text="Translate",
    font="Roboto 15 bold italic",
    activebackground="green",
    cursor="hand2",
    bd=5,
    bg="red",
    fg="white",
    command=translate_btn,
)
translate.place(x=480, y=250)

# label_change()

main.configure(bg="white")
main.mainloop()
