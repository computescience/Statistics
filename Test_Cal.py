import matplotlib.pyplot as plt
import statistics_practice
import numpy as np
import pandas as pd

resume = []
interview = []
offer = []
df = pd.DataFrame()

for i in range(10,1010, 10):
    resume.append(i)
for i in np.arange(0.1,1.1, 0.1):
    interview.append(i)
for i in np.arange(0.1,1.1, 0.1):
    offer.append(i)
#calculate with different successful rate of offer, how many resumes submissions.
df['Interview'] = interview
prob = []

for j in offer:
    for k in interview:
        p = statistics_practice.stats.conditionProb(k,j)
        prob.append(p)
    df['OfferProb'+str(round(j,1))] = prob
    prob = []


c = df.columns


for c in c:

    plt.plot(df['Interview'],df[c], label = c)
plt.legend(loc='lower right')
plt.xlabel('Interview Probability')
plt.ylabel('Offer Probability')
plt.title("Bayes Theorem on offer probability")
plt.show()
