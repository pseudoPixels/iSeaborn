import bokehBorn as bb


tips = bb.load_dataset("tips")

bb.barplot(x="day", y="total_bill", data=tips, palette="Blues_d", alpha=1.0)

