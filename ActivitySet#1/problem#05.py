'''
input
score deci


'''


def inp():
    score=float(input("enter the score  between 0.0 and 1.0:"))
    return score
def grades(score):
    if 1.0>=score>= 0.9:
        grade='A'
    elif 0.9>=score>= 0.8 :
        grade='B'
    elif 0.8>=score>= 0.7 :
        grade='C'
    elif 0.7>=score>= 0.6 :
        grade='D'
    elif score< 0.6 :
        grade='E'
    else:
        grade='n'
    return grade
def display(grade):
    if grade=="A":
        print("your grade is 'A")
    if grade=="B":
        print("your grade is 'B")
    if grade=="C":
        print("your grade is 'C")
    if grade=="D":
        print("your grade is 'D")
    if grade=="E":
        print("your grade is 'E")
    if grade=="n":
        print(""" 
        ERROR:
        enter the value between the range of 0 to 1
        
        """)
def main():
    score=inp()
    grade=grades(score)
    display(grade)
if __name__=='__main__':
    main()



    


