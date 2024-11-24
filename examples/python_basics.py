a = 10
b = 20

c = a + b
print(c)

# List
l = [1, 2, 3, 4]
print(l)

# ถ้าเราต้องการที่จะดูค่าใน List ตัวแรก เราจะอ้างอิงโดยเริ่มจาก Index ที่ 0
print(l[0])

# Tuple
my_tuple = (1, "hello", 3.14)
print(my_tuple)
print(my_tuple[1])

# Dict
d = {
    "a": 1,
    "b": 2,
}
print(d)

# คำสั่งในการดึงค่าของแต่ละ Key ทำได้ 2 แบบ
print(d["a"])
print(d.get("a"))

# Set
my_set = set()
my_set.add(10)
my_set.add(10)

# Loop
for i in range(11):
    print(i)
    
    
l = [1, 2, 3, 4]
for item in l:
    print(item)


d = {
    "a": 1,
    "b": 2
}
for k, v in d.items():
    print(f"Key: {k}, Value: {v}")

# Function
def greater_then_three(input_list):
    results = []
    for item in input_list:
        if item > 3:
            results.append(item)

    return results


list_1 = [1, 2, 3, 4, 5, 6]
print(greater_then_three(list_1))

# Classes and Objects
class DataExtractor:

    def __init__(self, value):
        self.value = value

    def get(self):
        return self.value


data_extractor_object = DataExtractor(9)
print(data_extractor_object.get())

# Libraries
from datetime import datetime


now = datetime.now().strftime("%Y %m %d")
print(now)
