data={
"name":"jacob",
"age":19,
"city":"erode"
}
def check_key_or_value(dictionary, key=None, value=None):
    if key is not None:
        return f"{key} is in dictionary" if key in dictionary else f"{key} is not in dictionary"
    if value is not None:
        return f"{value} is in dictionary" if value in dictionary.values() else f"{value} is not in dictionary"

print(check_key_or_value(data, key="name"))
print(check_key_or_value(data, value=19))
print(check_key_or_value(data, key="names"))
print(check_key_or_value(data, value="erode"))