# galvanize-capstone

## Step 1:

Concatenate raw data

## Step 2:

Generate historical demand. This is consistent with what Uber seems to suggest [here](https://newsroom.uber.com/semi-automated-science-using-an-ai-simulation-framework/):

>More sophisticated simulations don’t assume spatial or temporal distributions of passengers, drivers, or their destinations. Instead they randomly pull from the empirical distributions based on historical demand patterns.

--

`run ride_distribution.py`

`df` is a data-frame containing trip count for each combination of:

- lat: latitude
- lon: longitude
- weekend: 0 for weekday, 1 for weekend
- TOD: time of day

|index|      Lat|      Lon|  Weekend|  TOD | Count |
|---|---|---|---|---|---|
|     230839|  40.7635| -73.9805|        0|    8|      3|
|...|

RideDistribution is a class that take random samples with replacement from `df`, given weekend and TOD

So for example `rd.sample(0, 8, num=30)` would return 30 samples for 8am on a weekday.


## Next step:

Now that we know how to take individual samples using historical demand pattern, how do we actually simulate the random process of rides being requested?

I assume that the simulation elapses over time, so there should be some sort of trigger for when a new request is to be sampled. How do we model this trigger? Use linear regression to predict the number of rides in the next hour and then Poisson?
