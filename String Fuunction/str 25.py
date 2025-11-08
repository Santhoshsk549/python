s = "Hello World"
print(sum(1 for ch in s if ch.lower() in "aeiou"))


s = "madam"
print(s == s[::-1])


s = "Hello world from Python"
print(s.replace(" ", "_"))


s = "abc123xy45"
print("".join(ch for ch in s if ch.isdigit()))


s = "The Sun Rises In The East"
print([w for w in s.split() if w[0].isupper()])
