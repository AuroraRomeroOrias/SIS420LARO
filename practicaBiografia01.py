from secrets import choice


validation =True
biography ="Nombre:Lizeth Aurora Romero Orias\nEdad:20años\nCarrera:Ing. en Diseño y Animacion Digital\nNacida:30-11-2001"
while validation :
    print ("1.Biography")
    print("2.Exit")
    choice = input("Enter your choice :")
    if choice == "1" :
     print(biography)
    elif choice =="2":
        validation = False