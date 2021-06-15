def article(word):
  vowels = ['a','e','i','o','u']
  for vowel in vowels:
    if word[0] == vowel:
      return "an"
  return "a"

