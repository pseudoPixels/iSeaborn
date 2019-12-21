import iSeaborn as isn


tips = isn.load_dataset("tips")

isn.barplot(x="day", y="total_bill", data=tips, palette="Blues_d", alpha=1.0)

