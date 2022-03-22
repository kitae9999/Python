def std_weight(height,gender):
    if gender=="male":
        weight=round((height*0.01*height*0.01*22),2)
        print("키 {}cm 남자의 표준 체중은 {}kg입니다".format(height,weight))
    elif gender=="female":
        weight=round((height*0.01*height*0.01*21),2)
        print("키 {}cm 여자의 표준 체중은 {}kg입니다".format(height,weight))
        

std_weight(175,"female")