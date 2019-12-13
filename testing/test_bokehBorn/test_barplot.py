import seaborn as sns
from bokehBorn.categorical import barplot

tips = sns.load_dataset("tips")
print(tips.head())

barplot(x="day", y="total_bill", data=tips)


