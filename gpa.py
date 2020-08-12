grade1=int(input("Entee grade 1(0-4) :"))
grade2=int(input("Entee grade 2(0-4) :"))
grade3=int(input("Entee grade 3(0-4) :"))
grade4=int(input("Entee grade 4(0-4) :"))
total=grade1+grade2+grade3+grade4
credit=4
gpa = total/credit
print()
print("You nave %d sublect"%credit)
print("You have total point =%.2f, %d credit"%(total,credit))
print("You grt gpa = %5.2f"% gpa)
