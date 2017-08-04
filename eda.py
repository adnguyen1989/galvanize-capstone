import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('data/uber.csv')
uber_weekdays = df.pivot_table(index=['DOW'],
                                  values='DateTime',
                                  aggfunc='count')

uber_weekdays.plot(kind='bar', figsize=(8,6))


plt.show()
