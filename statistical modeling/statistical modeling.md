> i found this paper through this video: https://www.youtube.com/watch?v=ObbTLep4Hxo

> the paper is trying to argue that: “an algorithmic model can produce more and more reliable information about the structure of the relationship between inputs and outputs than data models”.

> note: around 2001 when this paper was published, very few people did machine learning so it was a hot take. but there are many other counter examples of what has been said here: [“A systematic review shows no performance benefit of machine learning over logistic regression for clinical prediction models”](https://pubmed.ncbi.nlm.nih.gov/30763612/)

## the cultures

the goal is to get information from data, then maybe use that information to make predictions.

we have two opposing cultures with different assumptions.

_culture 1: statistical community / data modeling culture_

- assumption: data are generated by a stochastic data model.
- we try to find a matching stochastic data model (ie. linear regression, logistic regression, cox model) that returns the right response variables based on the given predictor variables, random noice, parameters.
	- the conclusions are based on the model’s outputs, not on that of the nature (original black box we are trying to model).
- model validation: goodness-of-fit tests.

_culture 2: machine learning community / algorithmic modeling culture_

- asssumption: data mechanism is unknown.
- we try to find a function, which is an algorithm that operates on the input data with neural nets / decision trees and tries to predict the response.
- model validation: measured by predictive accuracy.

## the problem

here’s what people from culture-1 get wrong about people from culture-2.

occam’s razor often gets interpreted as simpler is better. but prediction, accuracy and simplicity (interpretability) are conflicting goals. 

they argue that machine learning models lack accuracy and interpretability because they are so complex. but in reality:

- the goal is not interpretability, but accurate information.
- we have to focus on the problem and on the data.