"""
ticker.py
Provides stock ticker symbols for some of the top companies on the S&P 500.
"""

import sys
import tkinter


companies = [
    None,
    "Apple Inc.",
    "Microsoft Corp.",
    "Amazon.com Inc.",
    "Facebook Inc.",
    "Berkshire Hathaway Inc.",
    "Google (aka Alphabet Inc.)"
]


tickers = [
    None,
    "AAPL",
    "MSFT",
    "AMZN",
    "FB",
    "BRK",
    "GOOG"
]
    
root = tkinter.Tk()
root.title("Stock ticker symbols")

#labels

compLabel = tkinter.Label(text = "Choose company name:", anchor = "w",padx = 20)
compLabel.grid(row = 0, column = 0)

mytikLabel = tkinter.Label(text = "Ticker:", anchor = "e",padx = 5)
mytikLabel.grid(row = 2, column = 0)

tikLabel = tkinter.Label(anchor = "e", pady = 10, padx = 40, bg = "white", fg = "green", font = 20)
tikLabel.grid(row = 2, column = 1, sticky = "e")



#Variables:

com = tkinter.StringVar(root)
com.set(companies[1])   #default value

#menu

def erase(companies):
    tikLabel["text"] = ""
    
compMenu = tkinter.OptionMenu(root, com, *companies[1:], command = erase)
compMenu.grid(row = 0, column = 1, sticky = "ew")

#button
def fetchticker():
    select = com.get()
    for ticker in tickers:
        if select == companies[1]:
            tik = tickers[1]
        elif select == companies[2]:
            tik = tickers[2]
        elif select == companies[3]:
            tik = tickers[3]
        elif select == companies[3]:
            tik = tickers[3]
        elif select == companies[4]:
            tik = tickers[4]
        elif select == companies[5]:
            tik = tickers[5]
        elif select == companies[6]:
            tik = tickers[6]

        tikLabel["text"] = tik

button = tkinter.Button(root, text = "Fetch ticker symbol",
    anchor = "e", padx = 20, pady = 5, command = fetchticker, bg = "red", fg="white")
button.grid(row = 1, column = 1, sticky = "e")

tkinter.mainloop()
