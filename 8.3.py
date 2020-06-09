class Script(Exception):
    def __init__(self, data, sheld):
        self.data = data

    try:
        sheld = []
        data = input("Enter number to exit enter 'stop'").lower()
        while data !="stop":
            if data.isdigit() == True:
                sheld.append(data)
                data = input("Enter number to exit enter 'stop'")
            else:
                raise Exception("Enter only numbers")
    except Exception as sc:
            data = input("Enter number to exit enter 'stop'")
    except data < 0 :
        print("Enter positive numbers")
    except ValueError:
        print("Not text only numbers")

    finally:
        ("Programm has been ending")
