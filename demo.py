#!/usr/bin/env python
# coding: utf-8

# ### Imports and Database Connection

# In[1]:


# import dependencies
import pandas as pd
from sqlalchemy import create_engine
from pomegranate import *

# get the path for the database
database_path = "database/name_origins.sqlite"

# ### Read the Database into a CSV

# In[2]:


# start up a connection to the database
engine = create_engine(f"sqlite:///{database_path}")
connection = engine.connect()

# In[3]:


# read the needed data from the database into dataframes
name_df = pd.read_sql("SELECT * FROM name", connection)

# close the connection, because who needs to use SQLalchemy
connection.close()

# In[4]:


name_df.head()

# ### Clean the Data

# In[5]:


# remove all of the fluff text from the used_in column
name_usage_split_df = name_df
name_usage_split_df['used_in'] = name_usage_split_df['used_in'].str.replace(' speaking countries', '')
name_usage_split_df['used_in'] = name_usage_split_df['used_in'].str.replace(' and', '')
name_usage_split_df['used_in'] = name_usage_split_df['used_in'].str.replace(',', '')

# chekcout the colums to make sure things work right
# pd.DataFrame(name_origin_split_df.groupby(by="used_in").count()).reset_index()["used_in"].tolist()


# In[6]:


# create a dictionary to hold the names, organized by usage
names_by_usage = {}

# iterate through each row of the DF
for i, row in name_usage_split_df.iterrows():
    # pull out all of the origins from the DF row and put them into a list
    usages = name_usage_split_df.loc[i, "used_in"].split(' ')

    # loop through all the list of origins to find matching keys (langueages that use the name)
    for usage in usages:
        # if it no keys match the existing keys add in a new one
        if not (usage in names_by_usage.keys()):
            names_by_usage[usage] = []
        # then add the names to the apropreate usage keys
        names_by_usage[usage].append(name_usage_split_df.loc[i, "title"])

# In[7]:


# checkout those keys
names_by_usage.keys()

# In[8]:


# delete all usage categories that have less than 40 names,
# otherwise usage categories will have improper sets
for key in list(names_by_usage.keys()):
    if len(names_by_usage[key]) < 40:
        del names_by_usage[key]

# check out the new list of languages that have more than 40 names (from the currrent data set at least)
names_by_usage.keys()

# In[9]:


# change all names to lowercase
for key, names in names_by_usage.items():
    for i, name in enumerate(names):
        names_by_usage[key][i] = name.lower()

# In[10]:


# Check the names
# print(names_by_usage["Arabic"])


# ### Create and Save Models

# In[11]:


# # loop through all fo the lists of names
# for key in names_by_usage.keys():
#     # for each list generate and fit a model
#     model = MarkovChain.from_samples(names_by_usage[key], k=2)
#     model.fit(names_by_usage[key])

#     # convert the model to a json
#     model_data = model.to_json()

#     # save the json to a file
#     with open(f"models/{key}.json", 'w') as outfile:
#         json.dump(model_data, outfile)


# ### Test Model

# In[12]:


# # Open json containing the model
# with open("models/Arabic.json", 'r') as infile:
#     same_data = json.load(infile)

# # Load the json into a model
# new_model = MarkovChain.from_json(same_data)

# # Get a sample of the model for texting
# new_model.sample(6)


# In[13]:


# def get_markov_chain(name_list):
#     letter_occurance = {}
#     markov_chain = {}

#     for name in name_list:
#         for i, char in enumerate(name):
#             if i >= 1:
#                 element = f"{name[i-1]}{name[i]}"
#                 if element in letter_occurance:
#                     letter_occurance[element] += 1
#                 else:
#                     letter_occurance[element] = 1

#     total_cases = 0

#     for element in letter_occurance.values():
#         total_cases += element

#     for key, value in letter_occurance.items():
#         markov_chain[key] = round(value/total_cases*100, 2)

#     return markov_chain


# In[14]:


# test_sample = get_markov_chain(names_by_usage['Arabic'])


# In[15]:


# test = 0
# for sample in test_sample.values():
#     test += sample

# print(test)


# In[16]:


def test_model(name_list):
    model = MarkovChain.from_samples(name_list, k=2)
    model.fit(name_list)
    return model.sample(6)


message = "Languages to pick from: \n"

for languages in names_by_usage.keys():
    message += (languages + ", ")

# In[18]:
x = True
while x:

# In[17]:
    print("\n           ***** Comparable Name Generator: By Kent Hazen *****\n")
    print("This project generates random names that sound like they originate from the input language.\n")
    print(message + "\n\n")
    language = input("which language do you want to get a name for? ")
    demo = test_model(names_by_usage[str.capitalize(str.lower(language))])
    name = ""
    for char in demo:
        name += char
    print("\n---------------")
    print(f"{name}")
    print("---------------\n\n\n")

    input("Press enter to continue: ")


