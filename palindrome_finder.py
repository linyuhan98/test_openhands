def find_palindromic_substrings(s):
    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            palindromes.add(s[left:right+1])
            left -= 1
            right += 1

    palindromes = set()
    for i in range(len(s)):
        expand_around_center(i, i)       # Odd length palindromes
        expand_around_center(i, i + 1)   # Even length palindromes

    return list(palindromes)

if __name__ == "__main__":
    test_string = "ababa"
    palindromes = find_palindromic_substrings(test_string)
    print("Palindromic substrings:", palindromes)