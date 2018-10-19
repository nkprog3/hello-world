pointspossible=37
score=20
studentname="Nick"
grade=score/pointspossible
#print(grade)
letter='ERROR'
if 1>=grade>=0.9:
  letter='A'
elif 0.9<grade<=0.8:
  letter='B'
elif 0.8<grade<=0.7:
  letter='C'
elif 0.7<grade<=0.6:
  letter='D'
else:
    letter='F'

print("{} - got grade {}".format(studentname,letter))
