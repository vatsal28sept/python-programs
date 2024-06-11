# List Uniqueness Checker
# Check If All Elements In List Are Unique ,If A Duplicate Is Found Exit The Loop And Print The Duplicate
# list = ["Apple","Banana","Orange","Apple","Mango"]
items = ["Apple","Banana","Orange","Apple","Mango"]
unique_item = set()
for item in items:
  if item in unique_item:
    print("Duplicate: ",item)
    break
  unique_item.add(item)