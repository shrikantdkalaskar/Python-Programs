Email=input("Enter Your Email Id : ")
k,j,d=0,0,0
if len(Email)>=6:
    if Email[0].isalpha():
        if ("@" in Email) and (Email.count("@")==1):
            if(Email[-4]==".") or (Email[-3]=="."):
                for i in Email:
                    if i.isspace():
                        k=1
                    elif i.isalpha():
                        if i.isupper():
                            j=1
                    elif i.isdigit():
                        continue
                    elif i=="_" or i=="." or i=="@":
                        continue
                    else:
                        d=1

                if k==0 ^ j==0 ^ d==0 :
                    print("Valid Email")
                else:
                    print("Wrong Email ,Error may due to space , Upper case Letter or Lack of Digit")
            else:
                print("Wrong Email , Error due to '.' ")
        else:
            print("Wrong Email , Their should only one '@' symbol is important")
    else:
        print("Wrong Email , First Letter is Always a alphabet")
else:
    print("Wrong Email , length of Email should be greater than 6 ")