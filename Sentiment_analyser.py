from tkinter import *
import tkinter.messagebox
import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Main function in program
def center(toplevel):
    toplevel.update_idletasks()
    w = toplevel.winfo_screenwidth()
    h = toplevel.winfo_screenheight()
    size = tuple(int(_) for _ in toplevel.geometry().split('+')[0].split('x'))
    x = w/2 - size[0]/2
    y = h/2 - size[1]/2
    toplevel.geometry("%dx%d+%d+%d" % (size + (x, y)))

def callback():
    if tkinter.messagebox.askokcancel("Quit", "Do you really wish to quit?"):
        main.destroy()

def setResult(type, res):
    if (type == "neg"):
        negativeLabel.configure(text = "Negatively : " + '%.2f' % res + "  \n")
    if (type == "neu"):
        neutralLabel.configure( text = "Neutral  : " + '%.2f' % res + "  \n")
    if (type == "pos"):
        positiveLabel.configure(text = "Positively : " + '%.2f' % res + "  \n")

def runAnalysis():
    sentences = []
    sentences.append(line.get())
    sid = SentimentIntensityAnalyzer()
    for sentence in sentences:
        # print(sentence)
        ss = sid.polarity_scores(sentence)
        for k in sorted(ss):
            setResult(k, ss[k])

# def editedText(event):
    # print(event.char)
    # typedText.configure(text = line.get() + event.char)

def runByEnter(event):
    typedText.configure(text = line.get())
    runAnalysis()

# Create main window
main = Tk()
main.title("Sentiment analysis")
main.geometry("840x520")
main.resizable(width=FALSE, height=FALSE)
main.protocol("WM_DELETE_WINDOW", callback)
main.focus()
center(main)

# addition item on window
label1 = Label(text = "Text you want to analyse:")
label1.pack()


line = Entry(main, width=70)
# line.bind("<Key>",editedText)
line.bind("<Return>",runByEnter)
line.pack()

textLabel = Label(text = "\nText you entered:", font=("Helvetica", 15))
textLabel.pack()
typedText = Label(text = "", fg = "red", font=("Helvetica", 20))
typedText.pack()

result = Label(text = "\nResults", font=("Helvetica", 15))
result.pack()
negativeLabel = Label(text = "", fg = "orange", font=("Helvetica", 20))
negativeLabel.pack()
neutralLabel  = Label(text = "", font=("Helvetica", 20))
neutralLabel.pack()
positiveLabel = Label(text = "", fg = "dark green", font=("Helvetica", 20))
positiveLabel.pack()
# Run program
mainloop()