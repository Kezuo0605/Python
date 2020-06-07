class Script(Exception):
    def __init__(self, data, sheld):
        self.data = data

    try:
        sheld = []
        data = input("Enter number to exit enter 'stop'").lower()
        while data !="stop":
            if data.isdigit():
                sheld.append(data)
                data = input("Enter number to exit enter 'stop'").lower()

            else:
                raise Script("Enter only numbers")
    except int(data) < 0 or data != int:
        print("Enter positive numbers")
    except Script as sc:
        print(sc)
    finally:
        ("Programm has been ending")
