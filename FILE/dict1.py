word_dict = {
  "apple": "a round fruit with red or green skin and a white inside",
  "banana": "a long curved fruit with a yellow skin",
  "cherry": "a small round fruit with a red or black skin and a hard seed inside"
}

word = input("Enter a word: ")
if word in word_dict:
  print(word_dict[word])
else:
  print("Sorry, that word is not in the dictionary.")
