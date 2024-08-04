import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

normal_scores = np.random.normal(75,10,100)

abnormal_scores = [10,150,-5,200]

index = np.random.choice(range(100),size=4,replace=False)

for i,idx in enumerate(index):
    normal_scores[idx]=abnormal_scores[i]

data = {
    "StudenID":range(1,101),
    "Scores":normal_scores
}

df = pd.DataFrame(data)

df_cleaned = df[(df['Scores'] >= 0) & (df['Scores'] <= 100)]


plt.figure(figsize=(12, 6))


plt.subplot(1, 2, 1)
plt.boxplot(df["Scores"], positions=[1], widths=0.5, patch_artist=True, boxprops=dict(facecolor='steelblue', alpha=0.5))
plt.title("Boxplot of Original Scores")
plt.ylabel("Scores")


plt.boxplot(df_cleaned["Scores"], positions=[1.5], widths=0.5, patch_artist=True, boxprops=dict(facecolor='orange', alpha=0.5))
plt.title("Boxplot of Scores (Original vs Cleaned)")
plt.xticks([1, 1.5], ['Original', 'Cleaned'])


plt.subplot(1, 2, 2)
plt.hist(df["Scores"], bins=20, color="steelblue", edgecolor="green", alpha=0.5, label="Original Scores")
plt.hist(df_cleaned["Scores"], bins=20, color="orange", edgecolor="red", alpha=0.7, label="Cleaned Scores")
plt.title("Histogram of Scores (Original vs Cleaned)")
plt.xlabel("Scores")
plt.ylabel("Frequency")
plt.legend()

plt.tight_layout()  
plt.show()