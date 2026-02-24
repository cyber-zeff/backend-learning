# basic syntax
# print("hello world")

# vars and data types
name = "Huzaifa" # string type of data
age = 20 # integer type of data
strAge = str(age)
fl = 2.44 # floating type
isMarried = False # bool type
favLang = ["TS", "PY", "Cpp"] # list type
ordinals = { 1: "first", 2: "second", 3: "third" } # dictionary (dict) / obj type

# print(type(ordinals))
# print(type(favLang))


# TODO: common str ops
str = "Hi there"
# print(str.upper())
# print(str.lower())
print("2" + str) # concatenation
print(str.split("her",1))

# slicing (start, end, step)
abc = slice(0,favLang.__len__(),2)
result = favLang[abc]
print(result)