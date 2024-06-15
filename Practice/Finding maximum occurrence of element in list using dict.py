names_list = ["marquad", "cwen", "cwen", "zhen", "marquad", "zhen", "csev", "zhen",
         "csev", "marquad", "zhen", "csev", "zhen"]
names_dict = dict()
for name in names_list:
  # if name in names_dict.keys():
  #   names_dict[name] += 1
  # else:
  #   names_dict[name] = 1
  names_dict[name] = names_dict.get(name, 0) + 1
max_count = max(names_dict.values())
print(list(names_dict.keys())[list(names_dict.values()).index(max_count)], "occurs maximum in given list")