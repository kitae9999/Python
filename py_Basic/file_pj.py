for week in range(1,51):
    with open("{}주차.txt".format(week),"w",encoding="utf8") as temp:
        temp.write("- {}주차 주간보고 -".format(week))
        temp.write("\n부서 : ")
        temp.write("\n이름 : ")
        temp.write("\n업무 요약 : ")


        