import numpy
def macierz(rozmiar):
    print('Wprowadź macierz')
    macierz = [[float(input("Podaj element: " )) for j in range(rozmiar)] for i in range(rozmiar)]
    return macierz



        

def main():
    rozmiar = int(input("Podaj wymiar tablicy: "))
    m1 = macierz(rozmiar)
    m2 = macierz(rozmiar)
    m3 = []
    for w in range(rozmiar):
        m3.append([])
        for k in range(rozmiar):
            element = 0
            for i in range(rozmiar):
                element += m1[w][i] * m2[i][k]
            m3[-1].append(element)    
    
    print(m3)

