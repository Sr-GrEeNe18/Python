


# file_handler = open ('preamble.txt', 'r')

# contents = file_handler.read()

# file_handler.close()

# print(contents)
# file_handler = open ('preamble.txt', 'wb')

# contents = file_handler.write('\n\n here is some new test on a new line heyy')

# file_handler.close()

# with open('riolove.txt', 'w') as file_handler:
#     contents = file_handler.write ('rio you got this sis, stay steady')

import pickle
students = {
    'Giselle': 'Las Vegas',
    'Layne': 'Atlanta',
    'Victoria': 'Humble'
}

with open('data.pickle', 'wb') as fh:
    students = pickle.dump(students, fh) 
    
with open('data.pickle', 'rb') as fh:
    students = pickle.load(fh)
print(students)
    




