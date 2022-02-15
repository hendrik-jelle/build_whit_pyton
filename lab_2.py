#%%
from calendar import firstweekday


first_name = "Erling"
last_name  = "Haaland"

full_name  = first_name + last_name
print(full_name)
#%%
first_name = "Erling"
last_name = "Haagland" 

full_name = "{} {}".format(first_name, last_name)
print(full_name)
# %%
first_name = "Erling"
last_name = "Haagland"
called_name = "jr."

full_name= "{} {} {}".format(first_name, last_name, called_name)

print(full_name)

# %%
first_name = "Erling"
last_name = "Haagland"
called_name = "jr."

full_name= "{[0]}{} {} {}".format(first_name,".", last_name, called_name)

print(full_name)
# %%
flower_list_1 = ['rose', 'tulip', 'lily']
flower_list_2 = ['dandelion', 'gerbera']

combined_flower_list = flower_list_1 + flower_list_2
print(combined_flower_list)
# %%

flower_list_1 = ['rose', 'tulip', 'lily']
flower_list_2 = ['dandelion', 'gerbera']

combined_flower_list = flower_list_1 + flower_list_2
print(combined_flower_list)