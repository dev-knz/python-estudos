from classes import Horista, Mensalista

def main():
    h1 = Horista(nome='Kevin', valor_hora=1000, horas_trabalhadas=10)
    print(f'{h1.calc_sal():.2f}')

    m1 = Mensalista(nome='Michel', sal_bruto=10000)
    print(f'{m1.calc_sal():.2f}')

if __name__ == '__main__':
    main()