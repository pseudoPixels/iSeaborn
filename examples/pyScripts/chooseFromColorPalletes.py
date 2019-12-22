import iSeaborn as isn
from bokeh.plotting import output_file, save

tips = isn.load_dataset("tips")
fig = isn.barplot(x= "day", y="total_bill", data=tips, palette="Blues_d")

output_file("chooseFromColorPalletes.html")
save(fig)
