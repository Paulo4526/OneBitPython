import webbrowser

done = False

while not done:
    print("\nO que vc deseja fazer?")
    print("1 - Aprender Python")
    print("2 - Aprender JavaScript")
    print("3 - Aprender Java")
    print("4 - Aprender Automações com No-Code")
    print("0 - Sair")
    choice = input(">")
    if choice == "1":
        webbrowser.open("http://www.python.org")
    if choice == "2":
        webbrowser.open("https://www.w3schools.com/jsrEF/default.asp")
    if choice == "3":
        webbrowser.open("https://docs.oracle.com/en/java/")
    if choice == "4":
        webbrowser.open("https://n8n.io/")
    if choice == "0":
        print("Saindo...")
        done = True