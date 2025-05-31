"""
#DEMO: replace() 
# Define the string containing the hyphen
number_string = "09-10992678"

# Use the replace method to remove the hyphen
cleaned_number_string = number_string.replace("-", "")

# Print the result
print(cleaned_number_string)
"""
def clean_song(song_str):
    """Converts all characters to lowercase and replaces punctuation with spaces."""
    for ch in ".,?":
        song_str = song_str.replace(ch, ' ')
    return song_str

def count_words(song):
    """Splits the song into words and counts the occurrence of each word."""
    song_list = song.split() #String to list
    word_dict = {word: song_list.count(word) for word in set(song_list)}
    return word_dict

# Sample data
data = "She's always buzzing just likeNeon, neon Neon, neon Who knows how long, how long, how long She can go before she burns away"

# Processing
print("全改小寫與用空白分開")
cleaned_song = clean_song(data.lower())
print(cleaned_song)
word_dictionary = count_words(cleaned_song)
print("result")
print(word_dictionary)
