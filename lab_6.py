#%%

vowels = 'aeiou'
names_list = ['Jim', 'John', 'uarc', 'Danny', 'Peter', "p"]
new_names_list = []

for name in names_list:
    print(name)
    for letter in name:
        if letter.lower()in vowels:
            name=name.replace(letter, " ")

new_names_list.append(name)

print(new_names_list)

#%%
import datetime
from time import strftime

current_date = datetime.date.today()
day_range = range(10)

for num_days in day_range:
    new_date = current_date + datetime.timedelta(days=num_days + 1)
    print(new_date.strftime("%A"))
# %%
