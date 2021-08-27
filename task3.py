#This function accepts an object (nested dictionary) and a key
# and returns back the value of the key
# Input: 
# object = {“x”:{“y”:{“z”:”a”}}}
# key = x/y/z
# Output:
# a


def object_key_value(object, key):
  key_cat = ""
  for key_value1 in object:
    if key_value1 == key:
      return object[key_value1]
    for key_value2 in object[key_value1]:
      key_cat = key_value1 + "/" + key_value2
      print(key_cat)
      if key_cat == key:
        return object[key_value1][key_value2]
      for key_value3 in object[key_value1][key_value2]:
        key_cat = key_cat + "/" + key_value3
        print(key_cat)
        if key_cat == key:
          return object[key_value1][key_value2][key_value3]


print(object_key_value({"a": {"b": {"c": "d"}}}, "a"))