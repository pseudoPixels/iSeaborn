import iSeaborn as isn
from bokeh.plotting import output_file, save

tips = isn.load_dataset("tips")
fig = isn.barplot(x="day", y="total_bill", data=tips, tools="pan, save")

output_file("chooseInteractiveTools.html")
save(fig)