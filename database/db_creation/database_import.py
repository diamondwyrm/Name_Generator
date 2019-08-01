import pandas as pd
import sqlite3

# establish a connection tot he sqlite database
connection = sqlite3.connect('../name_origins.sqlite')

# read in category.csv
category_df = pd.read_csv('../name-origin-csvs/category.csv')
category_df = category_df.set_index("id")
category_df.to_sql('category', connection, if_exists="replace", index=True, index_label="id")

# read in category_to_name.csv
category_to_name_df = pd.read_csv('../name-origin-csvs/category_to_name.csv')
category_to_name_df = category_to_name_df.set_index("id")
category_to_name_df.to_sql('category_to_name', connection, if_exists="replace", index=True, index_label="id")

# read in name.csv
name_df = pd.read_csv('../name-origin-csvs/name.csv')
name_df = name_df.set_index("id")
name_df.to_sql('name', connection, if_exists="replace", index=True, index_label="id")

# read in origin.csv
origin_df = pd.read_csv('../name-origin-csvs/origin.csv')
origin_df = origin_df.set_index("id")
origin_df.to_sql('origin', connection, if_exists="replace", index=True, index_label="id")


# close connection
connection.close()
