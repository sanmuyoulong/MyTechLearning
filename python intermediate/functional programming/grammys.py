# Instructions
# For many, music is so personal. We have created a playlist of songs that have won the “Song of the Year” 🏆 Grammy award in the past 5 years.

# Let's play around with the data!

# # List of songs with their durations (in minutes)
# playlist = [('What Was I Made For?', 3.42), ('Just Like That', 5.05), ('Song 3', 6.55), ('Leave The Door Open', 4.02), ('I Can\'t Breath', 4.47), ('Bad Guy', 3.14)] 

# First, use the filter() function to pick out the songs that are longer than 5 minutes (i.e., 5.00).

# Next, use map() to convert all the durations of the songs in your playlist from minutes to seconds.

# Lastly, add up the total playtime of the playlist with reduce().

# Since map(), filter(), and reduce() all use function parameters, it may be helpful to define separate named functions for them:

# A longer_than_five_minutes() function for filter().
# A minutes_to_seconds() function for map().
# An add_durations() function for reduce().

# List of songs with their durations (in minutes)
playlist = [('What Was I Made For?', 3.42), ('Just Like That', 5.05), ('Song 3', 6.55), ('Leave The Door Open', 4.02), ('I Can\'t Breath', 4.47), ('Bad Guy', 3.14)]

def song_pick(song):
    return song[1] > 5.00

after_pick = filter(song_pick, playlist)

def minutes_to_seconds(song):
    return (song[0], song[1] * 60)

after_conversion = map(minutes_to_seconds, after_pick)

def add_durations(total, song):
    return total + song[1]

from functools import reduce

total_playtime = reduce(add_durations, after_conversion, 0)
print(f'Total playtime of the playlist in seconds: {total_playtime}')