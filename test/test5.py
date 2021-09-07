python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(python[1].isupper())
print(len(python)) # 문자열 길이
print(python.replace("Python", "Java"))

index = python.index("n")
print(index)
index = python.index("n", index+1)
print(index)

print(python.find("Java")) # 없으면 -1
# print(python.index("Java")) # 없으면 에러

print(python.count("n"))

