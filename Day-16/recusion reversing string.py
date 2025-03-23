def reverse_String(str1):

    if len(str1)<=1:

        return str1

    else:

        return reverse_String(str1[1:])+str1[0]
        

print(reverse_String("avichal"))