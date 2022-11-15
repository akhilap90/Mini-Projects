# Merge Different Name and single mail body
#Name taken as input
i=input("Enter number of persons: ")
a=int(i)
for names in range(a):
    name = input("Type name and press Enter ")
    x= open ("name.txt","a")
    x.write(name + "\n")
x.close()
with open("name.txt") as n_file:
    with open("demo.txt") as m_file:
        body= m_file.read()
        for name in n_file:
            mail= "Hello"+" "+ name +"\n"+ body
            with open(name.strip() +".txt","w") as new_file:
                new_file.write(mail)
