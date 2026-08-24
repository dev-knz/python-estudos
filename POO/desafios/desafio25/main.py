from transporte import Caminhao, Drone, Moto

def main():
    c1 = Caminhao(50)
    print(c1.calc_frete())

    m1 = Moto(20)
    print(m1.calc_frete())

    d1 = Drone(5)
    print(d1.calc_frete())

if __name__ == '__main__':
    main()