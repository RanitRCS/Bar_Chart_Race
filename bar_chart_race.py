import pandas as pd
import bar_chart_race as bcr
df = pd.read_csv("https://raw.githubusercontent.com/RanitRCS/Bar_Chart_Race/main/sample_csv/urban_pop.csv")
df.head()
df = df.set_index('year')
df.head()
df.columns
bcr.bar_chart_race(df = df, title = "Population Growth",n_bars=10, orientation='h', fixed_order= True, cmap = 'prism')
