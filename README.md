# Python-program-to-convert-CSV-to-json
Example

my.csv

customer_name, item_1_id, item_1_quantity, Item_2_id, Item_2_quantity, Item_3_id, Item_3_quantity
topic1, John,4,John1, 24, John4, 16
topic2, 	Paul, 8,John2,41,John5, 33
topic3, Andrew, 1,John3, 34, John6,8

Json

[
{"topic1": [{"name": " John", "value": 4}, {"name": "John1", "value": 24}, {"name": " John4", "value": 16}]}, 
{"topic2": [{"name": " Paul", "value": 8}, {"name": "John2", "value": 41}, {"name": "John5", "value": 33}]},
{"topic3": [{"name": " Andrew", "value": 1}, {"name": "John3", "value": 34}, {"name": " John6", "value": 8}]}
]
