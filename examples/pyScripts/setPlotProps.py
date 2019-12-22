import iSeaborn as isn
from bokeh.plotting import output_file, save

tips = isn.load_dataset("tips")
fig = isn.barplot(x="day", y="total_bill", data=tips, plot_width=600, plot_height=200, plot_title="Awesome Plot Title")

output_file("setPlotProps.html")
save(fig)
