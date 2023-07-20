def check_palindrome(n):
    n = n.lower().replace(" ", "")
    return n == n[::-1]

names = "civic"
palindrome = check_palindrome(names)
print(palindrome)