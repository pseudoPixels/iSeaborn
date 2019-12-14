from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import HoverTool
import seaborn as sns
tips = sns.load_dataset("tips")

from bokeh.colors.rgb import RGB

agg = tips.groupby(['day'])['total_bill'].mean().reset_index(name ='total_bill')

print(agg['day'])
print(agg['total_bill'])


tips.to_csv('tips.csv')

output_file("bokeh_test.html")

fruits = ['Thur', 'Fri', 'Sat', 'Sun']
counts = [5, 3, 4, 2, 4, 6]

p = figure(y_range=agg['day'].tolist(), plot_height=250)

conv = []
conv.append(RGB(59, 83, 100))
conv.append(RGB(67, 115, 150))
conv.append(RGB(93, 146, 184))
conv.append(RGB(136, 176, 203))

r = agg['total_bill']
p.hbar(y=agg['day'], height=0.5, right=r, fill_color=conv
)

p.xgrid.grid_line_color = None
p.xaxis.axis_label = "day"
p.yaxis.axis_label = "total_bill"
p.add_tools(HoverTool(tooltips=[("Avg MPG", "@r")]))

show(p)