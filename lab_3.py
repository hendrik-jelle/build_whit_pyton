#%%
import datetime
# %%
import math

from pkg_resources import run_script
# %%
my_birthday = datetime.date(2022,3,23)
today = datetime.date.today()

daysto = my_birthday - today

print(daysto)
# %%
surface= math.pi * 5
print(surface)
# %%
import os
# %%
dirlist = os.listdir(os.getcwd())
print(dirlist)
# %%
newdir = os.mkdir("our_functions")
# %%
os.rmdir("test")
# %%

# %%
