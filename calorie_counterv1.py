KCAL={'rice':'1.30','chicken wing':'2.6','chicken thigh':'1.7','chicken':'2.1','steak':'2.38','turkey steak':'1.8','pork steak':'1.90','roast beef':'1.4','beef rib':'2.28','minced meat':'2.45','pork chop':'2.11','filet mignon':'2.67','chicken breast':'1.72','turkey breast':'1.34','tuscan sausage':'2.14','lettuce':'0.15','garlic':'1.2','potato':'0.77','sweet potato':'0.86','carrot':'0.40'}
UserMeal=[]
TOTAL=[]
run=1
run2=1

while run==1:
        REF=input('Enter with one food element from your meal (one at a time) (ex: rice): ').lower()
        if REF not in KCAL:
                print('Food is not on the menu :C ')
                continue
        else:
                run=0
                
        UserMeal.append(REF)
        while run2==1:
                
                QNT=input('Now the amount in grams (ex: 100): ')
                try:
                        float(QNT)
                        run2=0
                except:
                        print('Just numbers!')
                        continue
                run2=1
                if float(QNT)<=0:
                        print('Only amounts above zero!')
                        continue
                else:
                        run2=0
        run2=1      
        STOP=input('Anything else? (Y or N): ').lower()
        if STOP=='y':
                run=1
        elif STOP=='n':
                run=0
        else:
                break
for i in UserMeal:
        if i in KCAL:
                KCAL[i]=float(KCAL[i])
                QNT2=float(QNT)*(KCAL[i])
                TOTAL.append(QNT2)
TOTAL=sum(TOTAL)
print("The meal's caloric value: ", round(TOTAL, 2))

        
