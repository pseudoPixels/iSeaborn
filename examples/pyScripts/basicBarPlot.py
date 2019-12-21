import iSeaborn as isn
from bokeh.plotting import output_file, save

tips = isn.load_dataset("tips")
fig = isn.barplot(x="day", y="total_bill", data=tips)

output_file("basicBarPlot.html")
save(fig)
