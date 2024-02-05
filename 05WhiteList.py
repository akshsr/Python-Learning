black_list = ['susan', 'john', 'richael', 'robert']

num_student = int(input("Enter number of students: "))

student_list = []
white_list = []

for student in range (num_student):
    prompt = input("Input a name: ").lower()
    while prompt == "": # if input is black 
        prompt = input("Input non-empty name: ")
    student_list.append(prompt)

for student in student_list:
    if student not in black_list: 
        white_list.append(student)

print('These', len(white_list), "students are allowed to graduate.")
print(*sorted(white_list), sep="\n")