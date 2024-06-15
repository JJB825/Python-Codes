emails_dict = dict()
with open("mbox-short.txt", 'r') as handle:
  for line in handle:
    if not line.startswith("From "): 
      continue
    words = line.split()
    emails_dict[words[1]] = emails_dict.get(words[1], 0) + 1
  max_count = max(emails_dict.values())
  handle.close()

print(list(emails_dict.keys())[list(emails_dict.values()).index(max_count)], max_count)