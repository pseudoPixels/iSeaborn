import iSeaborn as isn
from bokeh.plotting import output_file, save

tips = isn.load_dataset("tips")
fig = isn.barplot(x="tip", y="day", data=tips)

output_file("horizontalBar.html")
save(fig)
