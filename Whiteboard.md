Read in data
  API to trading service
  create class to store data in (df?)

Create strategy (1 Day Iron Condor)
  read in inputs: ticker, exp date
  look at historical volatility (volatility over course of the day)
  Depending on above, determine optimal strategy, ie. bull vs bear spread, size of condor
  Determine size based on risk tolerance, account size

Send trade signals
  API to trading service

Tracker for open trades
