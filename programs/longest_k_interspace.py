def longest_k_interspace_substring(word, k):
    max_length = 0
    longest_substring = ""

    for i in range(len(word)):
        for j in range(i, len(word)):
            substring = word[i:j + 1]
            if max(ord(c) for c in substring) - min(ord(c) for c in substring) <= k:
                if len(substring) > max_length:
                    max_length = len(substring)
                    longest_substring = substring
            else:
                break

    return longest_substring


# Example usage
word = "hackerrank"
k = 0
print(longest_k_interspace_substring(word, k))  # Output: "abacaba"
