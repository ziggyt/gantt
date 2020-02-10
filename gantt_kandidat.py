from datetime import datetime
from datetime import timedelta
import plotly
import numpy
import plotly.figure_factory as ff

df = []
df_temp = []

entries = []


class GanttChartEntry:

    def __init__(self, name, start_datetime_str, finish_datetime_str, completeness) -> None:
        super().__init__()
        self.start_datetime = datetime.strptime(start_datetime_str, '%Y-%m-%d')
        self.finish_datetime = datetime.strptime(finish_datetime_str, '%Y-%m-%d')
        self.name: str = name
        self.completeness: int = completeness

        self.days: int = (self.finish_datetime - self.start_datetime).days
        self.start: str = self.start_datetime.strftime('%Y-%m-%d')
        self.finish: str = self.finish_datetime.strftime('%Y-%m-%d')

    def get_name(self):
        return f"{self.name} [{self.start} - {self.finish} ({self.days} days)] "


def add_gantt_chart_entry(gantt_chart_entry: GanttChartEntry):
    """Converts attributes from a GanttChartEntry to a dict and adds it to a list "df" """

    entry_dict = dict(Task=gantt_chart_entry.get_name(),
                      Start=gantt_chart_entry.start,
                      Finish=gantt_chart_entry.finish,
                      Complete=gantt_chart_entry.completeness)

    df.append(entry_dict)


entries.append(GanttChartEntry("Projektplan", "2020-01-20", "2020-02-14", 5))
entries.append(GanttChartEntry("Inläsning", "2020-01-20", "2020-02-28", 10))
entries.append(GanttChartEntry("Definiera spel och målgrupp", "2020-02-10", "2020-02-28", 12))
entries.append(GanttChartEntry("Definiera epics och första user stories", "2020-02-17", "2020-02-28", 20))
entries.append(GanttChartEntry("Rapport utkast 1", "2020-02-17", "2020-03-15", 35))
entries.append(GanttChartEntry("Första prototyp (papper och påbörjad i Unity)", "2020-02-17", "2020-03-08", 45))
entries.append(GanttChartEntry("Halvtidsredovisning", "2020-02-24", "2020-03-03", 50))
entries.append(GanttChartEntry("Översyn epics och user stories", "2020-03-02", "2020-03-13", 55))
entries.append(GanttChartEntry("Uppdatera pappersprototyp", "2020-03-02", "2020-03-13", 60))
entries.append(GanttChartEntry("Implementera funktionalitet i Unity etapp 1", "2020-03-09", "2020-03-13", 65))
entries.append(GanttChartEntry("Rapport utkast 2", "2020-03-16", "2020-04-17", 75))
entries.append(GanttChartEntry("Implementera funktionalitet i Unity etapp 2", "2020-04-06", "2020-05-03", 85))
entries.append(GanttChartEntry("Fokus debugging", "2020-04-27", "2020-05-10", 90))
entries.append(GanttChartEntry("Utvärdera utkast och färdigställ rapport", "2020-04-15", "2020-05-14", 95))
entries.append(GanttChartEntry("Slutredovisning", "2020-05-14", "2020-05-26", 100))





for entry in entries:
    add_gantt_chart_entry(entry)

fig = ff.create_gantt(df, colors=['#008fff', '#73e000'], index_col='Complete', show_colorbar=True, bar_width=0.4, showgrid_x=True, task_names="Task")
fig.show()
