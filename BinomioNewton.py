#       Binomio de newton
class BinomioNewton:

    def binomionew(n):
        c = [0] * (n+1)
        c[0] = 1
        for i in range(0,n):
            if i == 0:
                c[i+1] = (n-i) / (i+1)
            else:
                c[i+1] = c[i] * (n-i) / (i+1)
        return c

# print(binomionew(20))