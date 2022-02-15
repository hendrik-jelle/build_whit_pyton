#%%

import requests
brand = "BMW"
endpoint = f"https://opendata.rdw.nl/resource/m9d7-ebf2.json?merk={brand}"

response = requests.get(endpoint)
# %%
response.json()
# %%
