# -*- coding: utf-8 -*-
"""
Created on 9/16/2019 Monday
@author: Raymond Jing
"""

from tkinter import *
import numpy as np

class StockCalculator:

    def __init__(self):
        window = Tk()
        window.title("Stock Return Calculator")
        Label(window, text=None).grid(row=1,column=1) # space 
        
        Label(window, text="Stock purchase price ($):",font="Timesnewroman 16").grid(row=2, column=1, sticky=W)
        Label(window, text="Number of shares (/share):", font="Timesnewroman 16").grid(row=3, column=1, sticky=W)
        Label(window, text="Fee and commission income (%):", font="Timesnewroman 16").grid(row=4, column=1, sticky=W)
        Label(window, text="Cash dividends during the holding period ($):", font="Timesnewroman 16").grid(row=5, column=1, sticky=W)
        Label(window, text="Stock dividends during the holding period(/share):", font="Timesnewroman 16").grid(row=6, column=1, sticky=W)
        Label(window, text="Stock selling price ($):", font="Timesnewroman 16").grid(row=7, column=1, sticky=W)
        
        Label(window, text=None).grid(row=8,column=1) # space between inputs and outputs
        

        Label(window, text="Cost of purchase ($):", font="Timesnewroman 16").grid(row=9, column=1, sticky=W)
        Label(window, text="Cost of sales ($):", font="Timesnewroman 16").grid(row=10,column=1, sticky=W)
        Label(window, text="Total profit/loss ($):", font="Timesnewroman 16").grid(row=11,column=1, sticky=W)
        
        # variables to store inputs
        self.purchase_price = StringVar()
        self.number_of_shares = StringVar()
        self.fee = StringVar()
        self.cash_dividends = StringVar()
        self.stock_dividends = StringVar()
        self.selling_price = StringVar()
        

        # varianbles for outputs
        self.cost_of_purchase = StringVar()
        self.cost_of_sales = StringVar() 
        self.total = StringVar() 

        # text boxes to hold inputs
        Entry(window, textvariable = self.purchase_price,
              justify=RIGHT).grid(row=2,column=3, padx=(0,3))
        Entry(window, textvariable = self.number_of_shares, 
              justify=RIGHT).grid(row=3,column=3, padx=(0,5))
        Entry(window, textvariable = self.fee, 
              justify=RIGHT).grid(row=4,column=3, padx=(0,5))
        Entry(window, textvariable = self.cash_dividends, 
              justify=RIGHT).grid(row=5,column=3, padx=(0,5))
        Entry(window, textvariable = self.stock_dividends, 
              justify=RIGHT).grid(row=6,column=3, padx=(0,5))
        Entry(window, textvariable = self.selling_price, 
              justify=RIGHT).grid(row=7,column=3, padx=(0,5))
        
        # text boxes to hold outputs
        Entry(window, textvariable = self.cost_of_purchase, 
              justify=RIGHT).grid(row=9,column=3, padx=(0,5))
        Entry(window, textvariable = self.cost_of_sales, 
              justify=RIGHT).grid(row=10,column=3, padx=(0,5))
        Entry(window, textvariable = self.total, 
              justify=RIGHT).grid(row=11,column=3, padx=(0,5))
        
        # text boxes to hold inputs
        Label(window, text = "(股票购买价格):", font="Timesnewroman 16 bold", 
            justify=RIGHT).grid(row=2,column=2,sticky= W )
        Label(window, text = "(股票购买数量):", font="Timesnewroman 16 bold", 
            justify=RIGHT).grid(row=3,column=2, sticky= W)
        Label(window, text = "(手续费):", font="Timesnewroman 16 bold", 
            justify=RIGHT).grid(row=4,column=2,sticky= W )
        Label(window, text = "(持有期间获得现金股利):", font="Timesnewroman 16 bold", 
            justify=RIGHT).grid(row=5,column=2, sticky= E)
        Label(window, text = "(持有期间获得股票股利):", font="Timesnewroman 16 bold", 
            justify=RIGHT).grid(row=6,column=2,sticky= E )
        Label(window, text = "(股票卖出价格):", font="Timesnewroman 16 bold", 
            justify=RIGHT).grid(row=7,column=2, sticky= W)
        
        # text boxes to hold outputs
        Label(window, textvariable = self.cost_of_purchase, font="Timesnewroman 16 bold", 
            justify=RIGHT).grid(row=9,column=2, sticky= E)
        Label(window, textvariable = self.cost_of_sales, font="Timesnewroman 16 bold", 
            justify=RIGHT).grid(row=10,column=2,sticky= E )
        Label(window, textvariable = self.total, font="Timesnewroman 16 bold", 
            justify=RIGHT).grid(row=11,column=2, sticky= E)
        
        #Calculation button
        Button(window, text="Calculate Total Profit/Loss", 
               command=self.calcPayment).grid(row=8,column=3, padx= (60,5), pady=5)
        
        Label(window, text=None).grid(row=12,column=1) # space  
        
        # render form 
        window.mainloop()
        
        # calculate payment under refi 
    def calcPayment(self):
        purchase_price = float(self.purchase_price.get())
        number_of_shares = float(self.number_of_shares.get())
        fee = float(self.fee.get())
        cash_dividends = float(self.cash_dividends.get())
        stock_dividends = float(self.stock_dividends.get())
        selling_price = float(self.selling_price.get())

        
        if fee*purchase_price*number_of_shares < 5:
            cost_of_purchase = float(purchase_price*(number_of_shares+stock_dividends)+5+cash_dividends)
        else:
            cost_of_purchase = float(purchase_price*(number_of_shares+stock_dividends)+(fee*purchase_price*number_of_shares)/100+cash_dividends)
        
        cost_of_sales = float(selling_price*number_of_shares)
        total = float(cost_of_sales - cost_of_purchase)
        
        
        # display outputs in form
        self.cost_of_purchase.set("$" + format(cost_of_purchase, "5,.2f")+"(购买成本)")
        self.cost_of_sales.set(format(cost_of_sales, "5.2f")+"(卖出成本)")
        self.total.set("$" + format(total, "8,.2f")+"(总收益)")

StockCalculator()

