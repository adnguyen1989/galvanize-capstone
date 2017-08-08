## Project Goal

To build a high-fidelity ride-share simulation.

## Learning Goal

1. Understand the ride-share industry.
2. Apply predictive machine learning on actual data.
3. Handle unknown data / cold-start problem.
4. Practice good software engineering principles.

## Project Description

In many cases, A/B testing in live traffic is either impractical, unethical or impossible. A high-fidelity simulation addresses these issues by allowing the evaluation of different algorithms to take inside a simulated environment.

This project's goal is to create a simulation for the ride-share industry with the following characteristics:

|Agent|Action|
|---|---|
|Rider|Sign On|
||Request Ride|
|Driver|Sign On|
||Accept Ride|
||Sign Off|
|Algorithm|Dispatch
|Evaluation|Median Pickup Time|
||Fulfillment Rate
||Dropout Rate

\*  if time permit

## Project Evaluation

### Accuracy

A simulation is only useful as far as it gives similar results to reality. At a minimum, the simulation should give directionally accurate results, i.e. the relative magnitude of the baseline and treatment results should be the same as in production.

Since we do not have actual data, a few contrived dispatch algorithms will be tested to ensure that the simulation results agree with expectations.

### Flexibility

A simulation should allow the users to quickly and easily run experiments. It should accomplish this by abstracting the algorithm layer from the simulation base, allowing the users to specify custom algorithm functions to be used against the base.  

## Data

A lot of data is necessary to make a simulation accurate, among them:
- Rider sign-ons
- Rider information
- Initial ETA given versus actual requests
- Driver sign-ons
- Match given versus actual driver accepts
- Driver sign-offs
- Driver information

Unfortunately, only actual ride pickup data are available, so we need to generate dummy data to use for the simulation.

Practically speaking, this would negate any discussion for the actual accuracy of the simulation. A simulation should ideally be able update itself based on new data or even a completely different set of data, so there is still a lot of meaning to working with dummy data.
