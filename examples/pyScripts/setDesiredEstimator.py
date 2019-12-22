import iSeaborn as isn
from bokeh.plotting import output_file, save
from numpy import median

tips = isn.load_dataset("tips")
fig = isn.barplot(x="day", y="tip", data=tips, estimator=median)

output_file("setDesiredEstimator.html")
save(fig)
