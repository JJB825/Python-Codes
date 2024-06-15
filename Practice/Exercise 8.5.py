count = 0
with open("mbox-short.txt", 'r') as handle:
  for line in handle:
    if not line.startswith("From "): 
      continue
    words = line.split()
    print(words[1])
    count += 1
  handle.close()
print("There were", count, "lines in the file with From as the first word")