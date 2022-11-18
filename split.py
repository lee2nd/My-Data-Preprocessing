# https://stackoverflow.com/questions/36300158/split-text-after-the-second-occurrence-of-character

>>> a = "some-sample-filename-to-split"
>>> "-".join(a.split("-", 2)[:2])
'some-sample'

# a.split("-", 2) will split the string upto the second occurrence of -.
# a.split("-", 2)
# ['some', 'sample', 'filename-to-split']
# a.split("-", 3)
# ['some', 'sample', 'filename', 'to-split']
# a.split("-", 2)[:2] will give the first 2 elements in the list. Then simply join the first 2 elements.
# ['some', 'sample']
