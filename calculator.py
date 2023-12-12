#Using Function...
def add(a, b):
    print(a + b)


def sub(a, b):
    print(a - b)


def mul(a, b):
    print(a * b)


def div(a, b):
    print(a / b)

   

def calculation():

    #Using Exception Handling...
    try:
        num_1 = int(input("Enter the 1st number :"))
        num_2 = int(input("Enter the 2nd number :"))
        #global choice
        choice=input("Enter your Choice :")

        if choice== '1':
            print("\nResult :",end="")
            return add(num_1,num_2)

        elif choice== '2':
            print("\nResult :",end="")
            return sub(num_1,num_2)

        elif choice== '3':
            print("\nResult :",end="")
            return mul(num_1,num_2)

        elif choice== '4':
            if num_2==0:
                print("\nCann't Divide with 'Zero'...")
                nxt_calculation()
            else:
                print("\nResult :",end="")
                return div(num_1,num_2)

            
        else:
            print("Invalid Operator...")
        
    except ValueError:
        print("\nIsn't Valid input !,Give Valid input...")
     
        
            
def nxt_calculation():

    nxt_cal=input("\nDo you wnat to continue (yes/no) :")
    while nxt_cal=="YES" or nxt_cal=="yes":
        print("\n")
        calculation()

        if nxt_cal=="NO" or nxt_cal=="no":
            
            break

        elif nxt_cal!="YES" or nxt_cal!="yes":
            break


calculation()
nxt_calculation()

print("\nUngalukku Yaennoda Vazhthukkal...")



