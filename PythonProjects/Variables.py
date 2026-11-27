# cost = 10
# tax_percent=.25
# tax=cost*tax_percent
# price=cost+tax
# print(price)

# username="John"
# first_name="Eric"

# print(username +" "+first_name)

# use in the imports file
def calculate_homework(homework_assigment_arg):
    sum_of_grades=0
    for homework in homework_assigment_arg.values():
        sum_of_grades+=homework
    final_grade=round(sum_of_grades/len(homework_assigment_arg),2)
    print(final_grade)