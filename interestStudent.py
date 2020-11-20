##################################################################
# Student contributions to the interest calculator      "This is a Draft"
#
# You are free to add additional utility functions as you see fit,
# but you must implement each of the following functions while
# adhering to the specifications given in the project description
##################################################################

#---------------------------------------------------------------------------------

def greeting():
    print("This interest calculator will ask you to select an interest rate,\nfollowed by a principal value.  It will then calculate and display\nthe principal, interest rate, and balance after one year.  You will\nthen be invited to execute the process again or terminate.")
    print("")

#---------------------------------------------------------------------------------

def getRate(choices):
    valid_input=False
    while not valid_input:
        print("Please select an interest rate:")
        for j in range(len(choices)):
            msg=f'{chr(65+j)}){choices[j]:3}%'
            print(msg)
        input_1=input(f'Enter {chr(65)}-{chr(65+len(choices)-1)}: ')
        # 65 ='A' 90='Z'
        if input_1.isalpha()and len(input_1)==1 and ord(input_1)in range (65,65+len(choices)) :
            x=ord(input_1)-65
            rate=float(choices[x]/100)
            valid_input=True
            print("")
            return rate
        else:
            print("That is not a valid selection.\n")

    

#---------------------------------------------------------------------------------

def getPrincipal(limit):
    valid_input=False
    special_char='/?\+=!@#%&*(){}"`~,:; ][|><'
    alpha='abcdefghijklmnopqrstuvwxyz'
    while not valid_input:
        Check1=False
        Check2=False
        input1=input(f'Enter the principal (limit {limit}): ')
        if input1[0]=='$':
            input1=input1[1:]
        if input1.isnumeric() and float(input1)>limit:
            print(f'The principal can be at most {limit}.\n')
        if input1.isnumeric() and float(input1)<=limit and float(input1)>0:
            principal=float(input1)
            valid_input=True
            print("")
        else:
            if input1[0]=='-':
                x=input1.split('-')
                Check1=True
            if '.' in input1:
                y=input1.split('.')
                Check2=True
            if Check1:
                if not x[1].isnumeric() and not '.' in x[1]:
                    print('Please enter a number\n')
                elif len(x)>2:
                    print('Please enter a number\n')
                else:
                    print('You must enter a positive amount.\n')
            if Check2:
                if len(y)<3 and y[0].isnumeric() and y[1].isnumeric() and float(input1)<=limit and len(y[1])<3 :
                    principal=float(input1)
                    valid_input=True
                    break
                    print("")
                elif len(y)>2:
                    print('Please enter a number\n')
                elif y[0].isnumeric() and y[1].isnumeric() and float(input1)>limit:
                    print(f'The principal can be at most {limit}.\n')
                elif y[0].isnumeric() and y[1].isnumeric() and float(input1)<=limit and len(y[1])>=3:
                    print('The principal must be specified in dollars and cents.\n')
            elif input1.isalpha():
                print('Please enter a number\n')
            elif any(elem in input1 for elem in special_char)or any(elem in input1 for elem in alpha):
                print('Please enter a number\n')
            elif float(input1)==0.0:
                print('You must enter a positive amount.\n')
    print(principal)
    return principal     

#---------------------------------------------------------------------------------

def computeBalance(principal, rate):
    balance = principal + (principal * rate)
    return balance




#---------------------------------------------------------------------------------

def displayTable(principal, rate, balance):
    str1=str(rate)
    str2=str(principal)
    print('Initial Principal   Interest Rate   End of Year Balance')
    print('=======================================================')
    print(f'{"$"+str(principal):<20}{rate:<16}${balance:<19.2f}\n')
    months=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    print('Month   Starting Balance    APR     Ending Balance')
    print('=======================================================')
    month1=principal
    for i in range(12):
        month2=month1
        monthly_rate=pow(1+rate, 1.0/12) - 1
        monthly_increase=month2* monthly_rate
        month1+=monthly_increase
        msg=f'{months[i]:<8}${month2:<19.2f}{rate:<8}${month1:<14.2f}'
        print(msg)
        
    



    
#---------------------------------------------------------------------------------

def askYesNo(prompt):
    print(prompt,end='')
    valid_input=False
    while not valid_input:
        in1=input()
        print('')
        if ' 'in in1:
            check=in1.split(' ')
            for i in check:
                if i!='':
                    m=check.index(i)
                    break
            in2=check[m][0]
        else:
            in2=in1[0]
        if in2.lower()=='y':
            active=True
            valid_input=True
            print('')
        elif in2.lower()=='n':
            active=False
            valid_input=True
            print('')
        else:
            active = askYesNo('Another Computation [y/n]? ')
        
    return active
        


        

#---------------------------------------------------------------------------------


























