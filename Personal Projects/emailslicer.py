email=input("What is your email?: ").strip()

#Slice out username
username=email[:email.index("@")]


# slice domain
domain=email[email.index("@")+1:]



#format message

output=("Your username is: "+username+" and your domain is "+domain)
print(output)

            
