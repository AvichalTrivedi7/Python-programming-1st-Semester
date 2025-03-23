fabo=int(input("Enter the amount of numbers you need in the series: "))

list1=[1,1]

if fabo>2:

    for i in range(0,fabo-2):

        list1.append(list1[i]+list1[i+1])

    print(list1)


elif fabo==2:

    print(list1)



elif fabo==1:

    list1.pop()

    print(list1)


    