import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from mpl_finance import candlestick_ohlc

# Open price plot
f = open("AMZN.csv", "r")
a=[]
for i in f.readlines()[1:]:
    a.append(float(i.split(',')[1]))
f.close()

f = open("GOOG.csv", "r")
b=[]
for i in f.readlines()[1:]:
    b.append(float(i.split(',')[1]))
f.close()

f = open("AAPL.csv", "r")
c=[]
for i in f.readlines()[1:]:
    c.append(float(i.split(',')[1]))
f.close()

x = [t for t in range(1, 25)]
y = [t for t in a]
y1 = [t for t in b]
y2 = [t for t in c]
plt.plot(x, y, color='green', marker='o', linestyle='-', label='AMZN')
plt.plot(x, y1, color='red', marker='o', linestyle='-', label='GOOG')
plt.plot(x, y2, color='blue', marker='o', linestyle='-', label='AAPL')
plt.xlabel('time (daily)')
plt.ylabel('open price ($)')
plt.title('The Dynamics of Open Prices')
plt.legend()
plt.show()

# High price plot
g = open("AMZN.csv", "r")
a=[]
for i in g.readlines()[1:]:
     a.append(float(i.split(',')[2]))
g.close()

g = open("GOOG.csv", "r")
b=[]
for i in g.readlines()[1:]:
     b.append(float(i.split(',')[2]))
g.close()

g = open("AAPL.csv", "r")
c=[]
for i in g.readlines()[1:]:
     c.append(float(i.split(',')[2]))
g.close()

x = [t for t in range(1, 25)]
y3 = [t for t in a]
y4 = [t for t in b]
y5 = [t for t in c]
plt.plot(x, y3, color='green', marker='o', linestyle='-', label='AMZN')
plt.plot(x, y4, color='red', marker='o', linestyle='-', label='GOOG')
plt.plot(x, y5, color='blue', marker='o', linestyle='-', label='AAPL')
plt.xlabel('time (daily)')
plt.ylabel('high price ($)')
plt.title('The Dynamics of High Prices')
plt.legend()
plt.show()

# Low price plot
h = open("AMZN.csv", "r")
a=[]
for i in h.readlines()[1:]:
     a.append(float(i.split(',')[3]))
h.close()

h = open("GOOG.csv", "r")
b=[]
for i in h.readlines()[1:]:
     b.append(float(i.split(',')[3]))
h.close()

h = open("AAPL.csv", "r")
c=[]
for i in h.readlines()[1:]:
     c.append(float(i.split(',')[3]))
h.close()

x = [t for t in range(1, 25)]
y6 = [t for t in a]
y7 = [t for t in b]
y8 = [t for t in c]
plt.plot(x, y6, color='green', marker='o', linestyle='-', label='AMZN')
plt.plot(x, y7, color='red', marker='o', linestyle='-', label='GOOG')
plt.plot(x, y8, color='blue', marker='o', linestyle='-', label='AAPL')
plt.xlabel('time (daily)')
plt.ylabel('low price ($)')
plt.title('The Dynamics of Low Prices')
plt.legend()
plt.show()

# Close price plot
h = open("AMZN.csv", "r")
a=[]
for i in h.readlines()[1:]:
     a.append(float(i.split(',')[3]))
h.close()

h = open("GOOG.csv", "r")
b=[]
for i in h.readlines()[1:]:
     b.append(float(i.split(',')[3]))
h.close()

h = open("AAPL.csv", "r")
c=[]
for i in h.readlines()[1:]:
     c.append(float(i.split(',')[3]))
h.close()

e = open("AMZN.csv", "r")
a=[]
for i in e.readlines()[1:]:
     a.append(float(i.split(',')[4]))
e.close()

e = open("GOOG.csv", "r")
b=[]
for i in e.readlines()[1:]:
     b.append(float(i.split(',')[4]))
e.close()

e = open("AAPL.csv", "r")
c=[]
for i in e.readlines()[1:]:
     c.append(float(i.split(',')[4]))
e.close()

x = [t for t in range(1, 25)]
y9 = [t for t in a]
y10 = [t for t in b]
y11 = [t for t in c]
plt.plot(x, y9, color='green', marker='o', linestyle='-', label='AMZN')
plt.plot(x, y10, color='red', marker='o', linestyle='-', label='GOOG')
plt.plot(x, y11, color='blue', marker='o', linestyle='-', label='AAPL')
plt.xlabel('time (daily)')
plt.ylabel('close price ($)')
plt.title('The Dynamics of Close Prices')
plt.legend()
plt.show()


# Candlestick for Amazon
data = []

c = open("AMZN.csv", "r")
a = c.readlines()[1:]
for x in range(len(a)):
	line = a[x].split(',')
	data.append([x, float(line[1]), float(line[2]), float(line[3]), float(line[4])])
c.close()

fig, ax1 = plt.subplots()
candlestick_ohlc(ax1, data, width = 0.5, colorup = 'green', colordown = 'red')

plt.grid()
plt.xlabel('Days of Octօber')
plt.ylabel('Price ($)')
plt.title('Candlestick for Amazon')
plt.tight_layout()
plt.show()

# Candlestick for Google
data = []

c = open("GOOG.csv", "r")
a=c.readlines()[1:]
for x in range(len(a)):
	line=a[x].split(',')
	data.append([x, float(line[1]), float(line[2]), float(line[3]), float(line[4])])
c.close()

fig, ax1 = plt.subplots()
candlestick_ohlc(ax1, data, width = 0.5, colorup = 'green', colordown = 'red')

plt.grid()
plt.xlabel('Days of October')
plt.ylabel('Price ($)')
plt.title('Candlestick for Google')
plt.tight_layout()
plt.show()

# Candlestick for Google
data = []

c = open("AAPL.csv", "r")
a=c.readlines()[1:]
for x in range(len(a)):
	line=a[x].split(',')
	data.append([x, float(line[1]), float(line[2]), float(line[3]), float(line[4])])
c.close()

fig, ax1 = plt.subplots()
candlestick_ohlc(ax1, data, width = 0.5, colorup = 'green', colordown = 'red')

plt.grid()
plt.xlabel('Days of Octօber')
plt.ylabel('Price ($)')
plt.title('Candlestick for Apple')
plt.tight_layout()
plt.show()
