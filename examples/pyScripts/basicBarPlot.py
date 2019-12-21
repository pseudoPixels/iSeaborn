import bokehBorn as bb
from bokeh.plotting import figure, output_file, save

tips = bb.load_dataset("tips")

fig = bb.barplot(x="day", y="total_bill", data=tips)

output_file("basicBarPlot.html")
save(fig)
