# score_file=open("score.txt","w",encoding="utf8")
# print("수학: 0",file=score_file)
# print("영어: 50",file=score_file)
# score_file.close()

# score_file=open("score.txt","a",encoding="utf8")
# score_file.write("과학: 80")
# score_file.write("\n코딩: 100")
# score_file.close()

# score_file=open("score.txt","r",encoding="utf8")
# print(score_file.read())
# score_file.close()

# score_file=open("score.txt","r",encoding="utf8")
# print(score_file.readline()) #줄 별로 읽기
# print(score_file.readline())
# print(score_file.readline())
# print(score_file.readline())
# score_file.close()

# score_file=open("score.txt","r",encoding="utf8")
# while True:
#     line=score_file.readline()
#     if not line:
#         break
#     print(line)
# score_file.close()  

# score_file=open("score.txt","r",encoding="utf8")
# lines=score_file.readlines() #모든 라인들을 가져와서 한줄씩 리스트형태로 저장
# for line in lines:
#     print(line,end="")
# score_file.close()

# import pickle
# profile_file=open("profile.pickle","wb")
# profile={"이름":"박명수","나이":30,"취미":["축구","골프","코딩"]}
# print(profile)
# pickle.dump(profile,profile_file) #profile 에 있는 정보롤 file 에 저장
# profile_file.close()

# import pickle
# profile_file=open("profile.pickle","rb")
# profile=pickle.load(profile_file) #file에 있는 정보를 profile에 불러오기
# print(profile)
# profile_file.close()

# import pickle

# with open("profile.pickle","rb") as profile_file:
#     print(pickle.load(profile_file))  #따로 close해줄필요없음

# with open("study.txt","w",encoding="utf8")as study_file:
#     study_file.write("파이썬을 열심히 공부하고 있어요")

# with open("study.txt","r",encoding="utf8") as study_file:
#     print(study_file.read())
