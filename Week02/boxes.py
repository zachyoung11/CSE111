import math

manufactured_items = int(input("Enter the number of items: "))
items_per_box = int(input("Enter the number of items per box: "))

boxes_needed = math.ceil(manufactured_items/items_per_box)

print(f"For {manufactured_items} items, packing {items_per_box} in each box, you will need {boxes_needed} boxes.")
