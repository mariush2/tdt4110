import math

def f(x):
    #f(x)=(x - 12) * math.e^(5*x) - 8 * (x + 2)^2
    answer = (x - 12) * math.e ** (5*x) - 8 * (x + 2) ** 2
    return answer


def g(x):
    #g(x)= -x - 2x^2 - 5x^3 + 6x^4
    answer = -x - 2 * x ** 2 - 5 * x ** 3 + 6 * x ** 4
    return answer


def h(x):
    #h(x)= e^x
    answer = math.e ** x
    return answer


def derivate(h, x, func):
    #f(x+h/2)−f(x−h/2) / h
    answer = float((func(x + (h / 2)) - func(x - (h / 2))) / h)
    return answer


def newtons_method(h, x, func, tol):
    while True:
        #Følger formelen som er vist på oppgave siden
        x_1 = x - (func(x)) / derivate(h, x, func)
        #abs fordi vi ikke vet om vi får et positivt eller negativt tall,
        #men ønsker å finne når x_1 og x er tilnærmet lik hverandre (nullpunkt)
        min = abs(x_1 - x)

        if(min < tol):
            break

        #Hvis vi ikke har kommet til en tilnærming som er innenfor "tol", gjør vi det samme om igjen
        x = x_1
        y = func(x)
    print("Funksjonen", func.__name__, "nærmer seg et nullpunkt når x = " + str(x) +", da er y =",y)
    return x, y


print("f(0) =",f(0))
print("g(1) =",g(1))
print("derivate(0.0001,-2,f) =",derivate(0.000001,-2,f))
newtons_method(0.0001,5,h,0.0001)
