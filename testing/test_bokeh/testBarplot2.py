from bokeh.io import show, output_file
from bokeh.plotting import figure

import seaborn as sns
tips = sns.load_dataset("tips")

agg = tips.groupby(['day'])['total_bill'].mean().reset_index(name ='total_bill')

print(agg['day'])
print(agg['total_bill'])


tips.to_csv('tips.csv')

output_file("bokeh_test.html")

fruits = ['1', '2', '3']
counts = [5, 3, 4]

p = figure(x_range=fruits, plot_height=250, title="Title Fig")

p.vbar(x=[0, 1.5, 2, 3, 4, 5], top=[1, 2, 3, 4, 5, 6], width=.9)

p.xgrid.grid_line_color = None
p.xaxis.axis_label = "day"
p.yaxis.axis_label = "total_bill"
#
show(p)