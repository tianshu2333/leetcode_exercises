s = "abcabcbb"
sep_string = list(s)
# print(sep_string)
print(type(sep_string))
for i in range(len(sep_string)):
    mark = sep_string[i]
    sep_string[i] = True
    for key,value in enumerate(sep_string):
        if value == mark:
            sep_string[key] = False
