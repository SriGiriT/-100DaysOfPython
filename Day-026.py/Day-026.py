import random
import pandas
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# Find squares 
print([i*i for i in numbers])
# Even numbers
print([i for i in numbers if i%2==0])
def file_read(path):
  with open(path) as file:
    content = file.readlines()
    list = [int(i.replace("\n", "")) for i in content]
    return list

file1 = file_read('content/file1.txt')
file2 = file_read('content/file2.txt')
print([i for i in file1 if i in file2])

# Dictionary Comprehension
# new_dict = {new_key:new_value for (key, value) in dict.items() if test}
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
students_scores = {student:random.randint(1, 101) for student in names}
print(students_scores.items()) # (key, value) tuples 
passed_students = {student:mark for (student, mark) in students_scores.items() if mark>50}
print(students_scores)
print(passed_students)

# Find frequency
frequency_words = {word:len(word) for word in list(input().split())}
print(frequency_words)

# dict of Celsius to dict of Fahrenheit
weather_c = {"Monday":12, "Tuesday":14, "Wednesday":15, "Thursday":14, "Friday":21, "Saturday": 22, "Sunday":24}
weather_f = {days:temp*9/5+32 for (days, temp) in weather_c.items()}
print(weather_f)


# DataFrame iterrows()
student_dict = {
  "student": ["Angela", "James", "Lily"],
  "score": [56, 78, 98] 
}
student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)
for (index, row) in student_data_frame.iterrows():
  print(index)
  print(row)
  print(row.student)
  print(row.score)

nato_phonetic = pandas.read_csv('content/nato_phonetic_alphabet.csv')
nato_dict = {row.letter:row.code for (index, row) in nato_phonetic.iterrows()}
word = input("Enter a word: ")
nato_list = [nato_dict[i] for i in word.upper() ]
print(nato_list)