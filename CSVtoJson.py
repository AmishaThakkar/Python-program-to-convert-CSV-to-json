import pandas as pd
import json

output_lst = []

##specify the first row as header
df = pd.read_csv('my_csv.csv', header=0)
##iterate through all the rows
for index, row in df.iterrows():
    dict = {}
    items_lst = []
    ## column_list is a list of column headers
    column_list = df.columns.values


    for i, col_name in enumerate(column_list):
        ## for the first 2 columns simply copy the value into the dictionary
        if i<0:
            element = row[col_name]
            if isinstance(element, str):
            ## strip if it is a string type value
                element = element.strip()
            dict[col_name] = element

        elif "_id" in col_name:
            ## i+1 is used assuming that the item_quantity comes right after  the corresponding item_id for each item
            item_dict  = {"name":row[col_name], "value":row[column_list[i+1]]}
            items_lst.append(item_dict)


        j=0
        dict[row[column_list[j]]] = items_lst
        j=j+1

    output_lst.append(dict)

print(json.dumps(output_lst))