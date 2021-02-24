from ReverseString import reverse


def removeWhite(s):
    s = s.replace(" ", "")
    s = s.replace("'", "")
    return s


def isPal(s):
    s = removeWhite(s)
    if s == reverse(s):
        return True
    else:

        return False


print(reverse("madam i'm adam"))
print(isPal("madam i'm adam"))
