filename = input("Enter name of file: ")
with open (filename, 'r') as handle:
  word_list = list()
  for line in handle:
    words = line.split()
    for word in words:
      if word not in word_list:
        word_list.append(word)
  word_list.sort()
  print(word_list)
  handle.close()