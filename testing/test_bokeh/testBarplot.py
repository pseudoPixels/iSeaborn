from bokeh.io import show, output_file
from bokeh.plotting import figure, ColumnDataSource
from bokeh.models import HoverTool
import seaborn as sns
tips = sns.load_dataset("tips")
import pandas as pd
output_file("bokeh_test.html")


df = pd.read_csv("../dataset/car.csv")
source = ColumnDataSource(df)
car_list = source.data['Car'].tolist()
agg = tips.groupby(['day'])['total_bill'].mean().reset_index(name ='total_bill')

print(agg.head())

source = ColumnDataSource(agg)

p = figure(x_range=agg['day'].tolist(), plot_width=800,
  plot_height=600,
  tools="pan,box_select,zoom_in,zoom_out,save,reset")

p.vbar(x='day', top='total_bill',  width=0.7, color='orange',
    fill_alpha=0.5,
    source=source)

#
# p = figure(
#   y_range=agg['day'].tolist(),
#   title = 'Cars With Top Horsepower',
#   x_axis_label ='Horsepower',
#   plot_width=800,
#   plot_height=600,
#   tools="pan,box_select,zoom_in,zoom_out,save,reset"
# )
# p.hbar(
#     y='day',
#     right='total_bill',
#     left=0,
#     height=0.4,
#     color='orange',
#     fill_alpha=0.5,
#     source=source
# )

hover = HoverTool()
hover.tooltips = """
    <div>
        <h3>@day</h3>
        <div><strong>Total Bill: </strong>@total_bill</div>    
    </div>
"""


p.xgrid.grid_line_color = None
p.xaxis.axis_label = "day"
p.yaxis.axis_label = "total_bill"
p.add_tools(hover)

show(p)