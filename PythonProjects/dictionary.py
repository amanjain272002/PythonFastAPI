# user_dictionary = {
#     'username':'codingwithroby',
#     'name':'Eric',
#     'age':32
# }

# # print(user_dictionary)
# # print(user_dictionary.get("username"))

# user_dictionary["married"]=True
# print(len(user_dictionary))

# # user_dictionary.pop("age")
# # print(user_dictionary)
# # user_dictionary.clear()
# # print(user_dictionary)
# # del user_dictionary
# # print(user_dictionary)

# # for i,j in user_dictionary.items():
# #     print(i, j)

# user_dictionary2 = user_dictionary
# # user_dictionary2.pop("age")
# # print(user_dictionary)  age also got popped from user_dictionary 1

# # instead use .copy()

# user_dictionary3=user_dictionary.copy()
# user_dictionary3.pop("age")
# print(user_dictionary)


#  assignment

my_vechile = {
    "model":"Ford",
    "make":"Explorer",
    "year":2018,
    "mileage": 40000
}

for x, y in my_vechile.items():
    print(x,y)

vehicle2=my_vechile.copy()
vehicle2["number_of_tires"]=4
vehicle2.pop("mileage")
for i in vehicle2:
    print(i)