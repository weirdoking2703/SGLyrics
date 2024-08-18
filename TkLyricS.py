from tkinter import *
from lyrics_extractor import SongLyrics

root = Tk()
root.title("Song Lyrics")
root.geometry("700x400+300+200")
root.configure(bg='#326273')


def get_lyrics():
    extract_lyrics = SongLyrics(
        "AIzaSyAcZ6KgA7pCIa_uf8-bYdWR85vx6-dWqDg", "aa2313d6c88d1bf22"
    )
    temp = extract_lyrics.get_lyrics(str(e.get()))
    res = temp['lyrics']
    song.set(res)


Label(root, text="Enter Song Name", font='arial 10 bold italic', bg="#326273", fg="#fff").grid(row=0, column=1, sticky=W)
Label(root, text="Lyrics", font='arial 10 bold italic', bg="#326273", fg="#fff").grid(row=2, column=1, sticky=W)

song = StringVar()
Label(root, text="", textvariable=song, bg="#326273", font='arial 7').grid(row=3, column=2)

e = Entry(root, width=50, bd=2)
e.grid(row=0, column=2)
b = Button(root, text="Submit", bg="#326273", fg="white", width=10, height=1, bd=2, command=get_lyrics)
b.grid(row=1, column=2, columnspan=2, rowspan=2, padx=5, pady=5)

mainloop()
