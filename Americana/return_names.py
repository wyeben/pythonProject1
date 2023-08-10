def return_names_that_start_with_s(input):
    s = {name: input.count(name) for name in input if name.lower().startswith("s")}
    return s


them = ['Show', 'Shoe', 'School', 'hot', 'Shoe', 'book', 'show', 'shoe', 'school']
result = return_names_that_start_with_s(them)
print(result)
