from bokeh.io import show, output_file
from bokeh.plotting import figure

import seaborn as sns
tips = sns.load_dataset("tips")

agg = tips.groupby(['day'])['total_bill'].mean().reset_index(name ='total_bill')

print(agg['day'])
print(agg['total_bill'])


tips.to_csv('tips.csv')

output_file("bokeh_test.html")

fruits = ['Thur', 'Fri', 'Sat', 'Sun']
counts = [5, 3, 4, 2, 4, 6]

p = figure(y_range=agg['day'].tolist(), plot_height=250)

p.hbar(y=agg['day'], height=0.5, right=agg['total_bill'])

p.xgrid.grid_line_color = None
p.xaxis.axis_label = "day"
p.yaxis.axis_label = "total_bill"

show(p)