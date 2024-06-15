hours_dict = dict()
with open("mbox-short.txt", 'r') as handle:
  for line in handle:
    if not line.startswith("From "): 
      continue
    words = line.split(':')
    hours_dict[words[0][-2:]] = hours_dict.get(words[0][-2:], 0) + 1
  for hours, count in sorted(hours_dict.items()):
    print(hours, count)
  handle.close()