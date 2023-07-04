import json
def change_json_key(data, old_key, new_key):
    # Parse the JSON string into a Python dictionary
    # Check if the old key exists in the dictionary
    if old_key in data:
        # Get the value of the old key
        value = data[old_key]

        # Remove the old key-value pair
        del data[old_key]

        # Add a new key-value pair with the new key name
        data[new_key] = value

    # Convert the modified dictionary back to JSON string
    return data


with open('input.json', 'rb') as file:
    dat = json.loads(file.read())
# print(dat)
new_json = []


def convert_json(data):
    dic = dict(title='', key='')
    value = change_json_key(data, "oid", "key")
    value = change_json_key(data, "name", "title")
    dic["title"] = value['title']
    dic["key"] = value['key']
    new_json.append(dic)


for cls in dat:
    dataaaa = dat[f'{cls}']
    try:
        className = dat[f'{cls}']['class']
        if className in filter_class.class_types:
            del dataaaa
        elif dataaaa['status'] == 'deprecated':
            del dataaaa
        else:
            convert_json(dataaaa)
            # print(dataaaa)
    except KeyError:
        try:
            if dataaaa['oid'] is not None:
                convert_json(dataaaa)
        except KeyError:
            pass
        pass


def categorize_objects(objects):
    categorized = {}

    for obj in objects:
        obj_key = obj["key"]
        obj_title = obj["title"]

        # Split the key by dot separator
        key_parts = obj_key.split(".")
        parent_key = ".".join(key_parts[:-1])
        obj_id = key_parts[-1]

        # Create a new object entry if it doesn't exist
        if obj_key not in categorized:
            categorized[obj_key] = {"title": obj_title, "key": obj_key, "children": []}

        # Add the object as a child to its parent (if exists)
        if parent_key:
            if parent_key in categorized:
                categorized[parent_key]["children"].append(categorized[obj_key])
            else:
                categorized[parent_key] = {"children": [categorized[obj_key]]}

    top_objects = []
    for obj_key in categorized:
        if obj_key not in categorized[obj_key].get("key", ""):
            top_objects.append(categorized[obj_key])

    return top_objects


def remove_empty_children(categorized):
    for obj in categorized:
        if obj["children"]:
            remove_empty_children(obj["children"])
        else:
            obj.pop("children", None)


obj = json.dumps(new_json)
objects = json.loads(obj)

# Categorize objects
categorized_objects = categorize_objects(objects)
remove_empty_children(categorized_objects)
with open("categorized.json", "w") as file:
    json.dump(categorized_objects, file, indent=3)

# Read and print the generated JSON file
with open("categorized.json", "r") as file:
    categorized_json = json.load(file)
    print(json.dumps(categorized_json, indent=3))
