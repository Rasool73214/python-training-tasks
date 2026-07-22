from tools import utility as ut
print(f"choose from above :\n1. is_even\n2. average\n3. check\n4. kg_to_p\n5. p_to_kg\n6. r_string\n7. counts\n8. palindrome")
while True:
    try:
        n = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue
    if n==1:
        num = int(input("Enter a number: "))
        print("it is ",ut.is_even(num))
    elif n==2:
        num = list(map(int, input("Enter numbers separated by ',': ").split(',')))
        print("average is ",ut.average(num))
    elif n==3:
        num = list(map(int, input("Enter numbers separated by ',': ").split(',')))
        print("max and min are ",ut.check(num))
    elif n==4:
        num = int(input("Enter a number in kg: "))
        print("in pounds is ",ut.kg_to_p(num))
    elif n==5:
        num = int(input("Enter a number in pounds: "))
        print("in kg is ",ut.p_to_kg(num))
    elif n==6:
        num = input("Enter the word: ")
        print("reversed string is ",ut.r_string(num))
    elif n==7:
        num = input("Enter the word: ")
        print("count of vowels is ",ut.counts(num))
    elif n==8:
        num = int(input("Enter the number: "))
        print("palindrome: ",ut.palindrome(num))
    else:
        print("Invalid choice")
        break