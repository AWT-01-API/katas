def expanded_form(num):
    i = 10**(len(str(num))-1)
    ans = ''
    while num:
        if (num//i)*i != 0:
            ans += str((num//i)*i) + ' + '
        num = num % i
        i //= 10
    return (ans[0:len(ans)-3])