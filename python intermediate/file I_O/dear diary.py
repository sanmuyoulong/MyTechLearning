# This opens example file for writing
file = open('example.txt', 'w', encoding='utf-8')
file.write('Hello, World! 🌎')
file.close()

# Instructions
# Diaries can contain anything and everything. Some have even won awards. 🤫 Regardless of what your writing aspirations may be, let’s make a diary. Your secret is safe with us (your local storage 🔐).

# Let’s start writing!

# Use the open() method to create a new diaries.txt file.
# Fill your new diary with entries or secrets. 🤐
# Each entry should be separated by a new line.

open('diaries.txt', 'w', encoding='utf-8').write(
    "Dear Diary,\n"
    "I'm so excited to write in my diary today!\n"
    "It's a great way to express my thoughts and feelings.\n"
)
