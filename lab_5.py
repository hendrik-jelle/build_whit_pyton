# %%



name= 'Hendrik'
if "H" in name:
    print("jazeker")
# %%
name="arie"
klinkers_list= ['a', 'e', 'i']

if name[0] in klinkers_list:
    print("ja")
else:
    print("nee")
# %%
name="arie"
klinkers_list= ['a', 'E', 'O']

if name[0] in klinkers_list:
    name= name.replace (name[0], "B")
    print(name)
else:
    print("nee")
    print(name)