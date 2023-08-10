# def check_male_and_female(input_list):
#     male_count = 0
#     female_count = 0
#
#     for name in input_list:
#         if name.lower() == 'male':
#             male_count += 1
#         elif name.lower() == 'female':
#             female_count += 1
#
#     return [('male', male_count), ('female', female_count)]


def check_male_and_female(input_list):
    male = sum(1 for name in input_list if name.lower() == 'male')
    female = sum(1 for name in input_list if name.lower() == 'female')

    return [('male', male), ('female', female)]


them = ['male', 'female', 'Female', 'Male', 'male', 'female']
result = check_male_and_female(them)
print(result)
