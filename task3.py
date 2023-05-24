import pandas as pd
import lxml

"""Select a page on any site with tabular data. Import tables into pandas DataFrame."""

df = pd.read_html('https://pythonworld.ru/tipy-dannyx-v-python/stroki-funkcii-i-metody-strok.html')[0]

print(df.head())
