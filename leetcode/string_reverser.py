def reverse_segment(word, ch):
    """
    Reverses the segment of the word from the start up to and including the first occurrence of character ch.
    If ch is not found in word, the original word is returned.
    
    Time Complexity: O(n) - where n is the length of the string
    Space Complexity: O(n) - due to the creation of new string segments
    """
    index = word.find(ch)
    if index == -1:
        # If the character ch is not found, return the original word
        return word

    # Reverse the substring from 0 to index (inclusive)
    reversed_segment = word[:index + 1][::-1]

    # Append the part of the string after index
    return reversed_segment + word[index + 1:]

if __name__ == "__main__":
    print(reverse_segment("abcdefd", 'd'))  # Output: "dcbaefd"
    print(reverse_segment("xyxzxe", 'z'))   # Output: "zxyxxe"
    print(reverse_segment("abcd", 'z'))     # Output: "abcd"