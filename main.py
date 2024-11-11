import json

def royxat(a):
    with open('data.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    for item in data:
        if item['group_name'] == a:
            return item
    return "Topilmadi"

b = input("group_name ni kiriting: ")
natija = royxat(b)
print(natija)
