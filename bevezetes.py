def elsoFeladat():
    print("I/A:")
    autoNeve = input("\tAuto neve: ")
    gyarDatum = int(input("\tGyartasi datum: "))
    print("I/B:")
    if gyarDatum == 2023:
        print(f"\tEz az {autoNeve} friss gyartas")
    elif gyarDatum < 2000:
        print(f"\tEz az {autoNeve} oreg auto")
    else:
        print(f"\tEz az {autoNeve} atlagos koru")

