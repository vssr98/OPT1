#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 11:50:57 2023

@author: varunsree
"""

import yfinance as yf
import pandas as pd

def get_option_chain(ticker):
    stock = yf.Ticker(ticker)
    options = stock.option_chain(stock.options[0])
    calls = options.calls
    puts = options.puts
    return calls, puts

def place_order(api, ticker, contract_type, expiry, strike_price, quantity, order_type, time_in_force):
    api.submit_order(
        symbol=ticker,
        qty=quantity,
        side='buy' if contract_type == 'call' else 'sell',
        type=order_type,
        time_in_force=time_in_force,
        order_class='bracket',
        take_profit=dict(
            limit_price=0.9 * strike_price,
        ),
        stop_loss=dict(
            stop_price=1.1 * strike_price,
            limit_price=1.1 * strike_price,
        ),
        trail_price=0.1 * strike_price,
        trail_percent=10.0
    )

def execute_iron_condor_strategy(api, ticker):
    # Get option chain data
    calls, puts = get_option_chain(ticker)
    
    # Define parameters
    expiry = calls.iloc[0]['expiration']
    strike_price_1 = calls.iloc[0]['strike']
    strike_price_2 = calls.iloc[1]['strike']
    strike_price_3 = puts.iloc[0]['strike']
    strike_price_4 = puts.iloc[1]['strike']
    quantity = 1
    order_type = 'limit'
    time_in_force = 'gtc'
    
    # Place orders
    place_order(api, ticker, 'call', expiry, strike_price_1, quantity, order_type, time_in_force)
    place_order(api, ticker, 'call', expiry, strike_price_2, quantity, order_type, time_in_force)
    place_order(api, ticker, 'put', expiry, strike_price_3, quantity, order_type, time_in_force)
    place_order(api, ticker, 'put', expiry, strike_price_4, quantity, order_type, time_in_force)