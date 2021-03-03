def reverse(s):
    # if len(s) < 1:
    #     return s
    if len(s) < 2:
        return s[len(s)-1]
    else:
        return s[len(s)-1] + reverse(s[:len(s)-1])


print(reverse("hello"))
