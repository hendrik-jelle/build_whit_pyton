#%%
import sqlite3
from tkinter import INSERT

#%%
con= sqlite3.connect("database.db")
# %%
cursor = con.cursor()
# %%
qry_define_table = '''
CREATE TABLE training
(
    name text,
    participents real
)

'''
# %%
qry_insert_values = '''
INSERT INTO training ('python', 10)
'''
# %%
