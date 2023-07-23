def check_duplicates(name):
    return next((n for n in name if name.count(n) > 1), "No duplicate")


strings_list = ["orange", "banana", "banana", "apple"]
result = check_duplicates(strings_list)
print("Duplicate:", result)

strings_list = ["apple", "orange", "banana", "grape"]
result = check_duplicates(strings_list)
print("Duplicate:", result)


