import seaborn as sns
import matplotlib.pyplot as plt


tips = sns.load_dataset("tips")

ax = sns.barplot(x="tip", y="day", data=tips)
plt.show()