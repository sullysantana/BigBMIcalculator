#This program calculates BMI and CPA for a large data set of individuals

womenTotalBMI = 0
menTotalBMI = 0

womenTotalCPA = 0
menTotalCPA = 0

womenCount = 0
menCount = 0

totalWomenHeight = 0
TotalMenHeight = 0

totalMenWeight = 0
totalWomenWeight = 0

#Calculations:
class Respondents:
    def Kg2lbs(kg):
        try:
            pounds = kg * 2.20462
        except Exception:
            print("Error! Cant convert Kg to lbs. Check the data types of your input! not all strings can be converted to numbers.")
            print("and not all number types are the same.")
        return pounds

    def cm2inches(cm):
        try:
            inch = cm * 0.393701
        except Exception:
            print("Error! Cant convert from cm to inch. Check the data types of your input! not all strings can be converted to numbers.")
            print("and not all number types are the same.")
        return inch

    def GetDaCPA(daChestDiameter, daChestDepth, daBistroDiameter, daWristGirth, daAnkleGirth, height):
        try:
            daCPA = -110+(1.34*daChestDiameter)+(1.54*daChestDepth)+(1.20*daBistroDiameter)+(1.11 * daWristGirth)+(1.15 * daAnkleGirth)+(0.177 * height)
        except Exception:
            print("Error! Cant calculate CPA. Check the data types of your input! not all strings can be converted to numbers.")
            print("and not all number types are the same.")
        return daCPA

    def GetDaBMI(wait, heit):
        try:
            daBMI = (wait/(heit*heit))*703
        except Exception:
            print("Error! Cant calculate BMI. Check the data types of your input! not all strings can be converted to numbers.")
            print("and not all number types are the same.")
        return daBMI

#pulling the file and reading each line into a list:
try:
    o = open("datafile.txt", 'r')
except Exception:
    print("Error with file! ARGGGHH, the file name or path may be incorrect.")
    print("Or you may have left the file open somewhere else...")
else:
    daRespondents = o.readlines()

#conversion function calls in loop:
for i in range(0, len(daRespondents), 1):
    thisPerson = (daRespondents[i].split(","))
    print("Respondent #:{}".format(i+1))
    print("Weight:", "{:.2F}".format(Respondents.Kg2lbs(float(thisPerson[22]))), "(lbs.)")
    print("Height", "{:.2F}".format(Respondents.cm2inches(float(thisPerson[23]))), "(inches)")

    if thisPerson[24] == "0\n" or thisPerson[24] == "0":
        print("Sex: Female")
    else:
        print("Sex: Male")

#conversion calls
    print("BMI: ", "{:.2F}".format(Respondents.GetDaBMI(Respondents.Kg2lbs(float(thisPerson[22])),Respondents.cm2inches(float(thisPerson[23])))))
    print("CPA: ", "{:.2F}".format(Respondents.GetDaCPA(float(thisPerson[4]),float(thisPerson[3]),float(thisPerson[2]),float(thisPerson[20]),float(thisPerson[19]),float(thisPerson[23]))))
    print("----------")

    if thisPerson[24] == "0\n" or thisPerson[24] == "0":
        womenCount += 1
        totalWomenWeight += Respondents.Kg2lbs(float(thisPerson[22]))
        totalWomenHeight += Respondents.cm2inches(float(thisPerson[23])) #add em up, add em up, add em up
        womenTotalBMI += Respondents.GetDaBMI(Respondents.Kg2lbs(float(thisPerson[22])),Respondents.cm2inches(float(thisPerson[23])))
        womenTotalCPA += Respondents.GetDaCPA(float(thisPerson[4]),float(thisPerson[3]),float(thisPerson[2]),float(thisPerson[20]),float(thisPerson[19]),float(thisPerson[23]))
    else:
        menCount += 1
        totalMenWeight += Respondents.Kg2lbs(float(thisPerson[22]))
        TotalMenHeight += Respondents.cm2inches(float(thisPerson[23])) #add em up, add em up, add em up
        menTotalBMI += Respondents.GetDaBMI(Respondents.Kg2lbs(float(thisPerson[22])),Respondents.cm2inches(float(thisPerson[23])))
        menTotalCPA += Respondents.GetDaCPA(float(thisPerson[4]),float(thisPerson[3]),float(thisPerson[2]),float(thisPerson[20]),float(thisPerson[19]),float(thisPerson[23]))

print('\033[1m' + 'Averages' + '\033[0m')
print("----------")
print("Sex-->Females:", womenCount, "| Males: ", menCount, "| Total:", womenCount + menCount)
print("Height-->Females: {:.2F} | Males: {:.2F} | Total: {:.2F} (inches)".format((totalWomenHeight/womenCount),(TotalMenHeight/menCount),(totalWomenHeight+TotalMenHeight)/(menCount+womenCount)))
print("Weight-->Females: {:.2F} | Males: {:.2F} | Overall: {:.2F} (lbs.)".format((totalWomenWeight/womenCount),(totalMenWeight/menCount),(totalMenWeight+totalWomenWeight)/(menCount+womenCount)))
print("BMI-->Females: {:.2F} | Males: {:.2F} | Overall: {:.2F}".format((womenTotalBMI/womenCount),(menTotalBMI/menCount),(womenTotalBMI+menTotalBMI)/(menCount+womenCount)))
print("CPA-->Females: {:.2F} | Males: {:.2F} | Overall: {:.2F}".format((womenTotalCPA/womenCount),(menTotalCPA/menCount),(womenTotalCPA+menTotalCPA)/(menCount+womenCount)))
#FIN