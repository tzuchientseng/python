def length_of_longest_substring(s):
    """
    Time complexity: O(n), where n is the length of the string s.
    Space complexity: O(min(m, n)), where m is the size of the character set, and n is the length of the string s.
    """
    n = len(s)
    ans = 0
    # Use a dictionary to store the last occurrence position of each character
    map = {}
    i = 0  # Starting position of the sliding window

    for j in range(n):
        if s[j] in map:
            # If the character has appeared before, move the start of the window to the right of its last occurrence
            i = max(map[s[j]], i)
        # Update the length of the longest substring
        ans = max(ans, j - i + 1)
        # Update the position of the character
        map[s[j]] = j + 1

    return ans

# Test code
input_str = "abcabcabc"
print("Length of the longest substring without repeating characters:", length_of_longest_substring(input_str))
