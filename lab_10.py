#%%
from ntpath import join


with open("my_story.txt", "w") as file:
    file.write("And he wrote beautiful Python code.\nIt took some time.")
# %%
with open("my_story.txt", "r") as file:
    content = file.readlines()
    print(content)
# %%
with open("my_story.txt", "r") as file:
    content = file.readlines()
    print(content)

    new_content= "".join(content).upper()
    

# %%
