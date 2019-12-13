import seaborn as sns
from bokehBorn.categorical import barplot

tips = sns.load_dataset("tips")

barplot(x="day", y="total_bill", data=tips, orient="h")


