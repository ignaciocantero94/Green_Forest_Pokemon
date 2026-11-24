from pokemon_battles import Battle

class Fight:
    @staticmethod
    def battle_1():
        options = None
        while options != "S" and options != "N":
            options = input("Ash just found a trainer, would you like to start a battle? [S/N]\n ")
            if options == "S":
                head = "The battle begins!"
                print(head)
                print("_" * len(head))
                battle = Battle() # This is to open the class that contain the battles
                result = battle.first_battle() # Here we call our battle (method) from the class
                if result == "Victory":
                    print("Let´s go for the next one!")
                    return "Win"
                elif result == "Defeat":
                    print("Try again...")
                    return "Lost"
                elif result == "Scape":
                    print("You have scape!")
                    return "Run"
                break
            elif options == "N":
                print("Follow your journey")
                return "Deny"
            break
        return None

    @staticmethod
    def battle_2():
        options = None
        while options != "S" and options != "N":
            options = input("Ash just found a trainer, would you like to start a battle? [S/N]\n ")
            if options == "S":
                head = "The battle begins!"
                print(head)
                print("_" * len(head))
                battle = Battle() # This is to open the class that contain the battles
                result = battle.second_battle() # Here we call our battle (method) from the class
                if result == "Victory":
                    print("Let´s go for the next one!")
                    return "Win"
                elif result == "Defeat":
                    print("Try again...")
                    return "Lost"
                elif result == "Scape":
                    print("You have scape!")
                    return "Run"
                break
            elif options == "N":
                print("Follow your journey")
                return "Deny"
            break
        return None

    @staticmethod
    def battle_3():
        options = None
        while options != "S" and options != "N":
            options = input("Ash just found a trainer, would you like to start a battle? [S/N]\n ")
            if options == "S":
                head = "The battle begins!"
                print(head)
                print("_" * len(head))
                battle = Battle() # This is to open the class that contain the battles
                result = battle.third_battle() # Here we call our battle (method) from the class
                if result == "Victory":
                    print("Let´s go for the next one!")
                    return "Win"
                elif result == "Defeat":
                    print("Try again...")
                    return "Lost"
                elif result == "Scape":
                    print("You have scape!")
                    return "Run"
                break
            elif options == "N":
                print("Follow your journey")
                return "Deny"
            break
        return None

    @staticmethod
    def battle_4():
        options = None
        while options != "S" and options != "N":
            options = input("Ash just found a trainer, would you like to start a battle? [S/N]\n ")
            if options == "S":
                head = "The battle begins!"
                print(head)
                print("_" * len(head))
                battle = Battle() # This is to open the class that contain the battles
                result = battle.fourth_battle() # Here we call our battle (method) from the class
                if result == "Victory":
                    print("Let´s go for the next one!")
                    return "Win"
                elif result == "Defeat":
                    print("Try again...")
                    return "Lost"
                elif result == "Scape":
                    print("You have scape!")
                    return "Run"
                break
            elif options == "N":
                print("Follow your journey")
                return "Deny"
            break
        return None

    @staticmethod
    def battle_5():
        options = None
        while options != "S" and options != "N":
            options = input("Ash just found a trainer, would you like to start a battle? [S/N]\n ")
            if options == "S":
                head = "The battle begins!"
                print(head)
                print("_" * len(head))
                battle = Battle() # This is to open the class that contain the battles
                result = battle.fith_battle() # Here we call our battle (method) from the class
                if result == "Victory":
                    print("Let´s go for the next one!")
                    return "Win"
                elif result == "Defeat":
                    print("Try again...")
                    return "Lost"
                elif result == "Scape":
                    print("You have scape!")
                    return "Run"
                break
            elif options == "N":
                print("Follow your journey")
                return "Deny"
            break
        return None

    @staticmethod
    def battle_6():
        options = None
        while options != "S" and options != "N":
            options = input("Ash just found a trainer, would you like to start a battle? [S/N]\n ")
            if options == "S":
                head = "The battle begins!"
                print(head)
                print("_" * len(head))
                battle = Battle() # This is to open the class that contain the battles
                result = battle.sixth_battle() # Here we call our battle (method) from the class
                if result == "Victory":
                    print("Let´s go for the next one!")
                    return "Win"
                elif result == "Defeat":
                    print("Try again...")
                    return "Lost"
                elif result == "Scape":
                    print("You have scape!")
                    return "Run"
                break
            elif options == "N":
                print("Follow your journey")
                return "Deny"
            break
        return None

    @staticmethod
    def battle_7():
        options = None
        while options != "S" and options != "N":
            options = input("Ash just found a trainer, would you like to start a battle? [S/N]\n ")
            if options == "S":
                head = "The battle begins!"
                print(head)
                print("_" * len(head))
                battle = Battle() # This is to open the class that contain the battles
                result = battle.seventh_battle() # Here we call our battle (method) from the class
                if result == "Victory":
                    print("Let´s go for the next one!")
                    return "Win"
                elif result == "Defeat":
                    print("Try again...")
                    return "Lost"
                elif result == "Scape":
                    print("You have scape!")
                    return "Run"
                break
            elif options == "N":
                print("Follow your journey")
                return "Deny"
            break
        return None