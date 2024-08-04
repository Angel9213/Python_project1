import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
scores = np.concatenate([np.random.normal(75,10,100),np.array([10,150,-5,200])])

cleaned_scores = scores[(scores>=0) & (scores <= 100)]

plt.figure(figsize=(12,6))

plt.hist(scores, bins=20, color="steelblue",edgecolor='green',alpha=0.7,label="Original Scores" )

plt.hist(cleaned_scores,bins=20,color="orange",edgecolor='red',alpha=0.7,label="Cleaned Scores")

plt.title("Comparison of Original and Cleaned Scores")

plt.xlabel("Scores")

plt.ylabel("Frequency")

plt.legend()

plt.show()