import pandas as pd
import numpy as np

class RideDistribution(object):
    def __init__(self, df):
        self.df = df

    def sample(self, weekend, TOD, num=1):
        df = self.df
        # import ipdb; ipdb.set_trace()
        samples = df[(df.Weekend == weekend) & (df.TOD == TOD)].reset_index()
        total_ride_count = float(samples['Count'].sum())
        x = samples.shape[0]
        y = samples['Count'] / total_ride_count
        rand_sample = np.random.choice(x, num, p=y)
        return samples.iloc[rand_sample]

df = pd.read_csv('processed/ride_distribution.csv')
rd = RideDistribution(df)
print rd.sample(0, 8, num=30)
