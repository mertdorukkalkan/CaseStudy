from models.dictionary import ex_dictionary


def translate_data(data_json: dict):
    if isinstance(data_json, dict):
        translated_data = {}
        for key, value in data_json.items():
            translated_key = ex_dictionary.get(key,key)
            translated_value = translate_data(value)
            translated_data[translated_key] = translated_value
        return translated_data
    elif isinstance(data_json, list):
        translated_list = []
        for item in data_json:
            translated_item = translate_data(item)
            translated_list.append(translated_item)
        return translated_list
    else:
        translated_value = ex_dictionary.get(data_json, data_json)
        return translated_value

