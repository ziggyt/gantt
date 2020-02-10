import plotly
import numpy
import plotly.figure_factory as ff

df = []


def add_gantt_chart_entry(name, start, finish, completeness):
    """ Takes date YYYY-MM-DD"""
    df.append(dict(Task=name, Start=start, Finish=finish, Complete=completeness))


add_gantt_chart_entry("Projektplanering", "2020-01-20", "2020-02-14", 5)
add_gantt_chart_entry("Research", "2020-01-20", "2020-02-28", 8)
add_gantt_chart_entry("Utforska dagens utbud av spel", "2020-02-10", "2020-02-21", 12)
add_gantt_chart_entry("Brainstorming av spelidéer", "2020-02-10", "2020-02-21", 14)
add_gantt_chart_entry("Val av målgrupp", "2020-02-10", "2020-02-21", 16)
add_gantt_chart_entry("Val av spel", "2020-02-10", "2020-02-21", 18)
add_gantt_chart_entry("Skapande av epics och requirements", "2020-02-17", "2020-03-01", 25)
add_gantt_chart_entry("Skapande av user stories", "2020-02-17", "2020-03-01", 99)
add_gantt_chart_entry("Skapande av user stories", "2020-02-17", "2020-03-01", 99)

fig = ff.create_gantt(df, colors='Viridis', index_col='Complete', show_colorbar=True)
fig.show()
