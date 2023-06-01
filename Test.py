from bokeh.plotting import ColumnDataSource, figure, output_file, show
import pandas as pd
import numpy as np
from bokeh.palettes import Spectral11

source = ColumnDataSource(data=dict(
    x=[1, 2, 3, 4, 5],
    y=[2, 5, 8, 2, 7],
    desc=['A', 'b', 'C', 'd', 'E'],
))

print(source)

TOOLTIPS = [
    ("index", "$index"),
    ("(x,y)", "($x, $y)"),
    ("desc", "@desc"),
]

p = figure(width=400, height=400, tooltips=TOOLTIPS,
           title="Mouse over the dots")

p.line(source = source)

#show(p)




#ts_list_of_list = []
#for i in range(0,len(SP500.columns)):
#    ts_list_of_list.append(SP500.index.T)#

#vals_list_of_list = SP500.values.T.tolist()





#hover = p.select(dict(type=HoverTool))
#hover.tooltips = [
#    ("index", @a),
#    ("Date", @b),
#    ("Value", @c),
#]

#TOOLTIPS = [
#        ("index", "@a"),
#        ('Date', '@b{%Y-%m-%d}'),
#        ("Value", "@c")
#    ],

#hover = p.select(dict(type=HoverTool)



#source = ColumnDataSource(data=dict(x=b, y=c))

#c = figure(source = source, tools='hover')
#hover = p.select(dict(type=HoverTool))
#hover.tooltips = [
#        ("Date", "@b"),
#        ("Value", "@c"),
#        ]

#print(SP500)

#output_file("S&P500_random.html")

toy_df = pd.DataFrame(data=np.random.rand(4,3), columns = ('a', 'b' ,'c'), index = pd.to_datetime(['01-06-2018 23:15:00','02-09-2019 01:48:00','08-06-2020 13:20:00','07-03-2021 14:50:00']))

print(toy_df)

numlines=len(toy_df.columns)
mypalette=Spectral11[0:numlines]

p = figure(width=500, height=300, x_axis_type="datetime", tools='hover')
p.multi_line(xs=[toy_df.index.values]*numlines,
                ys=[toy_df[name].values for name in toy_df],
                line_color=mypalette,
                line_width=5)
show(p)




numlines=len(SP500.columns)
mypalette=Spectral11[0:numlines]
z = figure(width=500, height=300, x_axis_type="datetime")
z.multi_line(xs=[SP500.index.values]*numlines,
                ys=[SP500.iloc[:,1].values for nam in SP500],
                line_color=mypalette,
                line_width=5)
show(z)