#!/usr/bin/python3

import pandas as pd
import csv
import sys
import matplotlib.pyplot as plt

def main():
  d = pd.read_csv(sys.argv[1])

  # convert cell voltage columns to numeric
  cols = [col for col in d.columns if 'Cell Voltage #' in col]
  for col in cols:
    d[col] = pd.to_numeric(d[col], errors='coerce')

  valid_d = d.dropna()

  if valid_d.empty:
    print('could not find any valid rows, exiting...')
    return

  voltages = valid_d[cols].to_numpy()

  # sum of all cell voltages at each time
  v_batt = voltages.sum(axis=1)

  # max - min voltage between cells at each point in time
  v_batt_range = voltages.max(axis=1) - voltages.min(axis=1)

  nbins = 100

  plt.figure(1)
  plt.hist(voltages[0,:], nbins)
  plt.title('Cell voltage histogram from first time point')

  plt.figure(2)
  plt.hist(voltages[-1,:], nbins)
  plt.title('Cell voltage histogram from last time point')

  plt.figure(3)
  plt.plot(v_batt)
  plt.title('total battery voltage over time')

  plt.figure(4)
  plt.plot(voltages)
  plt.title('individual battery voltages over time')

  plt.show()
#  for col in cols:
#    plt.plot(d[col])
#  plt.show()  
  '''
  print("range=[%f, %f]" % (the_min, the_max))
  '''
if __name__ == '__main__':
  main()
