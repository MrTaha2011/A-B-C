def of() : # Open files function
    g = open("a.txt", "w")
    b = open("b.txt" , "w")
    n = open("n.txt", "w")
    return g, b, n

g, b, n = of() 

def wif(name, score, g, b, n) : # Write in files function
    if score >= 18 :
        g.write(f'{name} : {str(score)}\n')
    elif 14<score<18 :
        n.write(f'{name} : {str(score)}\n')
    else :
        b.write(f'{name} : {str(score)}\n')


def cf(g,n,b) : # Close files function
    g.close()
    n.close()
    b.close()

def gd(t, g, n, b) : # Get data function
    for i in range(t) :
        ina = input("Enter student name :\n")
        ins = float(input("Enter student score :\n"))
        wif(name = ina, score = ins, g=g , n=n, b=b)

