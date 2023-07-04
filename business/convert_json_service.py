import json
from utils.enums import filter_class


class ConvertJson:
    def change_json_key(self, data, old_key, new_key):
        if old_key in data:
            value = data.pop(old_key)
            data[new_key] = value
        return data

    def convert_and_add_json(self, data):
        dic = {
            "title": data.get("name", ""),
            "key": data.get("oid", "")
        }
        return dic

    async def filter_json(self, dataJSON):
        self.new_json = []
        for obj_key, obj_data in dataJSON.items():
            try:
                if obj_data.get("class") in filter_class.class_types or obj_data.get("status") == "deprecated":
                    continue
                converted_data = self.convert_and_add_json(obj_data)
                self.new_json.append(converted_data)
            except KeyError:
                if obj_data.get("oid") is not None:
                    converted_data = self.convert_and_add_json(obj_data)
                    self.new_json.append(converted_data)
        return self.new_json

    def categorize_objects(self, objects):
        categorized = {}

        for obj in objects:
            obj_key = obj["key"]
            obj_title = obj["title"]

            key_parts = obj_key.split(".")
            parent_key = ".".join(key_parts[:-1])

            if obj_key not in categorized:
                categorized[obj_key] = {"title": obj_title, "key": obj_key, "children": []}

            if parent_key:
                if parent_key in categorized:
                    categorized[parent_key]["children"].append(categorized[obj_key])
                else:
                    categorized[parent_key] = {"children": [categorized[obj_key]]}

        top_objects = [categorized[obj_key] for obj_key in categorized if obj_key not in categorized[obj_key].get("key", "")]
        return top_objects

    def remove_empty_children(self, categorized):
        for obj in categorized:
            if obj["children"]:
                self.remove_empty_children(obj["children"])
            else:
                obj.pop("children", None)
        return categorized

    async def upload_json(self, data):
        data_json = await self.filter_json(data)
        objects = json.loads(json.dumps(data_json))
        categorized_objects = self.categorize_objects(objects)
        return self.remove_empty_children(categorized_objects)
