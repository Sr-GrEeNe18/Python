# 1. Create a dictionary called zodiac with the following inforation.
# Each key is the name of the zodiac
# Aries - The Warrior
# Taurus - The Builder
# Gemini - The Messenger
# Cancer - The Mother
# Leo - The King
# Virgo -The Analyst
# Libra - The Judge
# Scorpio - The Magician
# Sagittarius - the Gypsy
# Capricorn - the Father
# Aquarius - The Thinker
# Pisces - TheMystic
# 1a. Retrieve information about your zodiac from the zodiac dictionary
# 2. Given the following dictionary

# Zodiac = {"Rio": "Capricorn the mother"}
# print(Zodiac)



# phonebook_dict = {
#     'Alice': '703-493-1834',
#     'Bob': '857-384-1234',
#     'Elizabeth': '484-584-2923'
# }
# phonebook_num = phonebook_dict.values
# print(phonebook_dict)
# phonebook_dict = {
#     'Alice': '703-493-1834',
#     'Bob': '857-384-1234',
#     'Elizabeth': '484-584-2923'
# }
# print(f'Kareem = int(938-489-1234)

# phonebook_dict["Kareem"] = "938-489-1234"
# # 2a. Print Elizabeth's phone number
# print(phonebook_dict['Elizabeth'])

# # 2b. Add a entry to the dictionary: Kareem's number is 938-489-1234.
# print(f"Kareem's number is 938-489-1234{phonebook_dict}")

# # 2c. Delete Alice's phone entry.
# del phonebook_dict['Alice']
# print(phonebook_dict)
# # 2d. Change Bob's phone number to '968-345-2345'.
# print(f"Bob's 968-489-1234{phonebook_dict}")

# # 2e. Print all the phone entries.
# print(phonebook_dict) 
# # 3. Nested dictionaries
ramit = {
    'name': 'Ramit',
    'email': 'ramit@gmail.com',
    'interests': ['movies', 'tennis'],
    'friends': [
        {
            'name': 'Jasmine',
            'email': 'jasmine@yahoo.com',
            'interests': ['photography', 'tennis']
        },
        {
            'name': 'Jan',
            'email': 'jan@hotmail.com',
            'interests': ['movies', 'tv']
        }
    ]
}
# 3a. Write a python expression that gets the email address of Ramit.
print(ramit['email'])
# 3b. Write a python expression that gets the first of Ramit's interests.
print(ramit['interest'[0]])
# 3c. Write a python expression that gets the email address of Jasmine.
print(ramit[])
# 3d. Write a python expression that gets the second of Jan's two interests.
# 4. Letter Summary
# Write a letter_histogram function that takes a word as its input,
# and returns a dictionary containing the tally of how many times
# each letter in the alphabet was used in the word. For example:
# # >>>letter_histogram('banana')
# # {'a': 3, 'b': 1, 'n': 2}
# # Word Summary
# # Write a word_histogram function that takes a paragraph of text as its input, and returns a dictionary containing the tally of how many times each word in the alphabet was used in the text. For example:
# # >>> word_histogram('To be or not to

# contact = [
#     {
#         'first_name': 'Phillip',
#         'last_name': 'Guo',
#         'email': 'phillip.guo@gmail.com',
#         'phone':{
#             'work':'837-494-3948',
#             'cell': '234-897-4933'
#         }
#     },
#     {
#         'first_name': 'Mark',
#         'last_name': 'Guzdial',
#         'email': 'mark.guzdial@gatech.edu',
#         'phone':{
#             'work':'484-569-3466',
#             'cell': '493-485-9845'
#         }
#     }
#     print(contat[0]['phone']['work'])