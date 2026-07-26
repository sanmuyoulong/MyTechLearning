file = open('filename.txt', 'w')
lines = ['This is a line.\n', 'This is the next line.\n']

file.writelines(lines)
file.close()

file = open('filename.txt', 'r')
lines = file.readlines()
for line in lines:
  print(line, end='')
file.close()

file = open('filename.txt', 'r')
content = file.read()
print('Using read():')
print(content)
file.close()

# Instructions
# ✨ Here at Codédex, we are 🤩 big fans of music 🎹. The only thing better than a perfect playlist is a playlist with all your favorite songs. Let's create a Python script that organizes the songs into a .txt file. Let's make a playlist!

# First, let's define a dictionary to store liked songs:

# liked_songs = {
#   'title': 'artist'
# }

# Next, create a function to display and write liked songs to a file:

# def write_liked_songs_to_file(liked_songs, file_name):

# Open the file in write mode.
# Write each song and artist by iterating through the liked_songs dictionary.
# Your liked_songs.txt file should look something like this:

# Liked Songs:
# Bad Habits by Ed Sheeran
# I'm Just Ken by Ryan Gosling
# Mastermind by Taylor Swift
# Uptown Funk by Mark Ronson ft. Bruno Mars
# Ghost by Justin Bieber

liked_songs = {
    'Bad Habits': 'Ed Sheeran',
    "I'm Just Ken": 'Ryan Gosling',
    'Mastermind': 'Taylor Swift',
    'Uptown Funk': 'Mark Ronson ft. Bruno Mars',
    'Ghost': 'Justin Bieber'
}

def write_liked_songs_to_file(liked_songs, file_name):
    file = open(file_name, 'w', encoding='utf-8')
    file.write('Liked Songs:\n')
    for title, artist in liked_songs.items():
        file.write(f'{title} by {artist}\n')
    file.close()

write_liked_songs_to_file(liked_songs, 'liked_songs.txt')
file = open('liked_songs.txt', 'r', encoding='utf-8')
content = file.read()
print('Liked Songs Playlist:')
print(content)
file.close()
