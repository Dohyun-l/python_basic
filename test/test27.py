# import pickle

# with open("profile.pickle", "rb") as profile_file: # 따로 close() 안함, with 나오면서 알어서 close()
#     print(pickle.load(profile_file))

# with open("study.txt", "w", encoding="utf-8") as study_file:
#     study_file.write("파이썬을 열심히 공부하고 있어요")

with open("study.txt", "r", encoding="utf-8") as study_file:
    print(study_file.read())