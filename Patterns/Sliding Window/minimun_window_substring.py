# Leetcode 76. Minimum Window Substring


def min_window(s, t):
    tmap = {} # Store all the characters with count needed in s string
    window = {} # Current window of s string
    for char in t:
        tmap[char] = tmap.get(char, 0) + 1 # Inset the char and count on t string
    left = 0 # Left pointer
    unique = 0 # No of unique characters of t string are present in s string 
    ln = float("inf") # Longest length
    idx_left = 0 # Index of left pointer
    idx_right = 0 # Index of right pointer
    for right in range(len(s)): # Right pointer
        char = s[right]
        window[char] = window.get(char, 0) + 1 # Add the char to the window
        if char in tmap and window[char] == tmap[char]: # Agar window me right ptr ka char t string me hai or count same hai , it means that char with frequency is present in window  
            unique += 1 # Increment the unique count
        while unique == len(tmap): # While the unique count is equal to the number of unique characters in tmap
            win_len = right - left + 1 # Calculate the length of the window
            if ln > win_len: # Check for minimum length
                ln = win_len # Set the minimum length
                idx_left = left # set the left and right index to get substring
                idx_right = right

            window[s[left]] -= 1 # Remove the elememnt from left as we are shrinking from left
            if s[left] in tmap and window[s[left]] < tmap[s[left]]: # If unique character count is less than what we need from t string , decrese the unique count
                unique -= 1
            left += 1
    return s[idx_left : idx_right + 1]


print(min_window(s="ADOBECODEBANC", t="ABC"))
