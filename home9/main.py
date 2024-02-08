import requests
from bs4 import BeautifulSoup
from tkinter import *
from tkinter import ttk

class Exchanger:
    def __init__(self):
        self.bank = 'https://privatbank.ua'

        self.valutes = {
            'euro': {
                'buy': "EUR_buy",
                'sell': "EUR_sell"},

            'usd': {
                'buy': "USD_buy",
                'sell': "USD_sell"},

            'pln': {
                'buy': "PLN_buy",
                'sell': "PLN_sell"}

        }

        self.valutess = ["EURO", "PLN", "USD"]

        def change():
            valu = self.combobox.get()
            uah = self.entry.get()
            self.label["text"] = str(float(uah) / float(self.get_valute_curse(valu.lower())[0]))


        self.root = Tk()
        self.root.title("Обмінник Валют")
        self.root.geometry("500x500")

        self.entry = ttk.Entry()
        self.entry.pack(anchor=NW, padx=6)

        self.label3 = ttk.Label(text="UAH")
        self.label3.pack(anchor=NW, padx=6)

        self.label2 = ttk.Label(text="To")
        self.label2.pack(anchor=NW, padx=6, pady=6)

        self.combobox = ttk.Combobox(values=self.valutess, state="readonly")
        self.combobox.pack(anchor=NW, fill=X, padx=5, pady=5)


        self.btn = ttk.Button(text="Change", command=change)
        self.btn.pack(anchor=NW, padx=6, pady=6)

        self.label = ttk.Label()
        self.label.pack(anchor=NW, padx=6, pady=6)

        self.root.mainloop()

    def get_valute_curse(self, valu):
        req = requests.get(self.bank)
        soup = BeautifulSoup(req.content, "html.parser")

        buy = soup.find("td", {"id": f'{self.valutes[valu]["buy"]}'})
        sell = soup.find("td", {"id": f'{self.valutes[valu]["sell"]}'})

        buy = buy.text.split()
        sell = sell.text.split()

        buy = buy[0]
        sell = sell[0]

        return [buy, sell]


changer = Exchanger()
