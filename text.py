import pandas as pd 

url = "https://info.usd-cny.com/wti/lishi.htm"

table = pd.read_html(url)

print(table)