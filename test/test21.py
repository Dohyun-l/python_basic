# def profile(name, age, lang1, lang2, lang3, lang4, lagn5):
#     print("이름 : {}\t나이: {}\t".format(name,age), end=" ")
#     print(lang1, lang2, lang3, lang4, lagn5)

def profile(name, age, *lang):
    print("이름 : {}\t나이: {}\t".format(name,age), end=" ")
    for lang in lang:
        print(lang, end=" ")
    print()

profile("유재석", 20, "Python", "Java", "C", "C++", "C#")
profile("김태호", 25, "Kotlin", "Swift")