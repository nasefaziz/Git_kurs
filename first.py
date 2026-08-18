 
print("IT career quiz")
score = 0
answer  = input("Do you like \
programming?")
if answer == "yes":
    score += 1

answer = input ("Do you like" \
" solving the problems")
if answer == "yes":
    score += 1

answer = input ("Do you like teamwork")
if answer == "yes":
    score += 1 


answer = input ("Do you like computer")
if answer == "yes":
    score += 1 


answer = input ("Do you like  Learning")
if answer == "yes":
    score += 1

    answer = input ("Do you like Coffe")
if answer == "yes":
    score += 1    
print ("Yous score  " , score ,5 )
if score >= 4:
    print("great IT you are good")
elif score>= 2:
    print("you are some good be IT")
else : 
    print("learning")