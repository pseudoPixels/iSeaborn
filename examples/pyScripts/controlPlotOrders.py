import iSeaborn as isn
from bokeh.plotting import output_file, save

tips = isn.load_dataset("tips")
fig = isn.barplot(x="time", y="tip", data=tips,order=["Lunch", "Dinner"])

output_file("controlPlotOrders.html")
save(fig)
