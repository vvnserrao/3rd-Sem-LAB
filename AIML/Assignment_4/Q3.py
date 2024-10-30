import matplotlib.pyplot as plt

date = ['10-03-16','10-04-16','10-05-16','10-06-16','10-07-16']
open = [774.25, 776.030029, 779.309998, 779, 779.659973]
high = [776.065002, 778.710022, 782.070007, 780.47998, 779.659973]
low = [769.5, 772.890015, 775.650024, 775.539978, 770.75]
close= [772.559998, 776.429993, 776.469971, 776.859985, 775.080017]

plt.plot(date, open, marker='o', label='Open')
plt.plot(date, high, marker='o', label='High')
plt.plot(date, low, marker='o', label='Low')
plt.plot(date, close, marker='o', label='Close')

plt.xlabel('Date')
plt.ylabel('Price')
plt.title('Alphabet Inc. Financial Data (Oct 3, 2016 - Oct 7, 2016)')
plt.legend()
plt.grid(True)


