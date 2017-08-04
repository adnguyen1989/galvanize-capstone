import pandas as pd
import os
import holidays

US_HOLIDAYS = holidays.UnitedStates()

class DataPrep(object):

    def __init__(self, dir):
        self.dir = dir

    def fit_one(self, fn):
        print "processing: " + fn
        df = pd.read_csv(fn)
        df = df.rename(index=str, columns={"Date/Time": "DateTime"})
        df['DateTime'] = pd.to_datetime(df['DateTime'], format='%m/%d/%Y %H:%M:%S')
        df['Date'] = pd.to_datetime(df['DateTime'].dt.date, infer_datetime_format=True)
        df['Month'] = df['DateTime'].dt.month
        # Monday=0, Sunday=6
        df['DOW'] = df['DateTime'].dt.dayofweek
        # weekday = 0, weekend = 1
        df['Weekend'] = (df['DOW'] > 4).astype(int)
        df['Holiday'] = (df['DateTime'].isin(US_HOLIDAYS)).astype(int)
        df['TOD'] = df['DateTime'].dt.hour
        return df.drop(['Base'],axis=1)

    def fit(self):
        fns = [self.dir + '/' + f for f in os.listdir(self.dir) if f.endswith("14.csv")]
        self.df = pd.concat(map(lambda x: self.fit_one(x), fns))
        return self

    def joint_csv(self, out):
        print "writing: " + out
        self.df.to_csv(out, index=False)

    def ride_distribution_csv(self, out, loc):
        df = self.df[loc]
        locdf = df.groupby(loc).size().to_frame('Count').sort_values('Count',ascending=False).reset_index()
        print "writing: " + out
        locdf.to_csv(out, index=False)

directory = 'data'
joint_out = 'data/uber.csv'
ride_distribution_out = 'processed/ride_distribution.csv'
loc = ['Lat', 'Lon','DOW','TOD']

dp = DataPrep(directory)
dp.fit()
dp.joint_csv(joint_out)
dp.ride_distribution_csv(ride_distribution_out, loc)
