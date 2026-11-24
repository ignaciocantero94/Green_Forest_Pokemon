import os
import random

class Battle:
    @staticmethod
    def first_battle():
        charizard = 100
        butterfree = 100
        life_charizard = charizard
        life_butterfree = butterfree
        life_bar = 20
        scape = False

        life_bar_charizard = int(life_charizard * life_bar / charizard)
        print("Charizard´s life: [{} {}] [{}/{}]".format("*" * life_bar_charizard, " " * (life_bar - life_bar_charizard),
                                                        life_charizard, charizard))

        life_bar_butterfree = int(life_butterfree * life_bar / butterfree)
        print("Butterfree´s life: [{} {}] [{}/{}]".format("*" * life_bar_butterfree, " " * (life_bar - life_bar_butterfree),
                                                          life_butterfree, butterfree))

        # Turn´s begin
        while life_butterfree > 0 and life_charizard > 0:
            attack = None
            while attack != "A" and attack != "B" and attack != "C" and attack != "Q":
                attack = input("Charizard´s turn...\n"
                               "A. Embers\n"
                               "B. Flamethrower\n"
                               "C. Body blow\n"
                               "Q. Scape\n ")
                if attack == "A":
                    print("Charizard used Embers")
                    life_butterfree -= 12
                elif attack == "B":
                    print("Charizard used Flamethrower")
                    life_butterfree -= 15
                elif attack == "C":
                    print("Charizard used Body blow")
                    life_butterfree -= 10
                elif not ("A", "B", "C", "Q"):
                    print("You have to pick one of this four options!")

                if life_butterfree < 0:
                    life_butterfree = 0
                elif life_charizard < 0:
                    life_charizard = 0

            if attack == "Q":
                scape = True
                break

            os.system("clear")

            life_bar_charizard = int(life_charizard * life_bar / charizard)
            print("Charizard´s life: [{} {}] [{}/{}]".format("*" * life_bar_charizard, " " * (life_bar - life_bar_charizard),
                                                             life_charizard, charizard))

            life_bar_butterfree = int(life_butterfree * life_bar / butterfree)
            print("Butterfree´s life: [{} {}] [{}/{}]".format("*" * life_bar_butterfree, " " * (life_bar - life_bar_butterfree),
                                                              life_butterfree, butterfree))

            input("Enter to continue...\n")
            # Next Turn
            enemie_attack = random.randint(1,3)
            print("Butterfree´s turn...\n")
            if enemie_attack == 1:
                print("Butterfree used Confusion")
                life_charizard -= 8
            elif enemie_attack == 2:
                print("Butterfree used Wing attack")
                life_charizard -= 10
            elif enemie_attack == 3:
                print("Butterfree used Poison")
                life_charizard -= 12

            if life_butterfree < 0:
                life_butterfree = 0
            elif life_charizard < 0:
                life_charizard = 0

            life_bar_charizard = int(life_charizard * life_bar / charizard)
            print("Charizard´s life: [{} {}] [{}/{}]".format("*" * life_bar_charizard, " " * (life_bar - life_bar_charizard),
                                                             life_charizard, charizard))

            life_bar_butterfree = int(life_butterfree * life_bar / butterfree)
            print("Butterfree´s life: [{} {}] [{}/{}]".format("*" * life_bar_butterfree, " " * (life_bar - life_bar_butterfree),
                                                              life_butterfree, butterfree))

            input("Enter to continue...\n")

        if life_charizard == 0:
            print("Butterfree wins!")
            return "Defeat"
        elif life_butterfree == 0:
            print("Charizard wins!")
            return "Victory"
        elif scape == True:
            return "Scape"
        return None


    @staticmethod
    def second_battle():
        charizard = 100 
        raichu = 100
        life_charizard = charizard
        life_raichu = raichu
        life_bar = 20
        scape = False
        
        life_bar_charizard = int(life_charizard * life_bar / charizard)
        print("Charizar´s life: [{} {}] [{}/{}]".format("*" * life_bar_charizard, " " * (life_bar - life_bar_charizard),
                                                        life_charizard, charizard))
        life_bar_raichu = int(life_raichu * life_bar / raichu)
        print("Raichu´s life: [{} {}] [{}/{}]".format("*" * life_bar_raichu, " " * (life_bar - life_bar_raichu),
                                                        life_raichu, raichu))
        
        while life_charizard > 0 and life_raichu > 0:
            
            attack = None
            while attack not in ("A", "B", "C", "Q"):
                attack = input("Charizard´s turn...\n"
                               "A. Embers\n"
                               "B. Flamethrower\n"
                               "C. Body blow\n"
                               "Q: Scape\n")
                if attack == "A":
                    print("Charizard used Embers")
                    life_raichu -= 12
                elif attack == "B":
                    print("Charizard used Flamethrower")
                    life_raichu -= 15
                elif attack == "C":
                    print("Charizard used Body blow")
                    life_raichu -= 10
                elif not ("A", "B","C","Q"):
                    print("You have to pick one of this four options!")
                
                if life_raichu < 0:
                    life_raichu = 0
                elif life_charizard < 0:
                    life_charizard = 0

            if attack == "Q":
                scape = True
                break

            os.system("clear")

            life_bar_charizard = int(life_charizard * life_bar / charizard)
            print("Charizar´s life: [{} {}] [{}/{}]".format("*" * life_bar_charizard, " " * (life_bar - life_bar_charizard),
                                                            life_charizard, charizard))
            life_bar_raichu = int(life_raichu * life_bar / raichu)
            print("Raichu´s life: [{} {}] [{}/{}]".format("*" * life_bar_raichu, " " * (life_bar - life_bar_raichu),
                                                            life_raichu, raichu))

            input("Enter to continue...\n")

            print("Raichu´s turn...\n")
            enemie_attack = random.randint(1,3)
            if enemie_attack == 1:
                print("Raichu used Lightning")
                life_charizard -= 10
            elif enemie_attack == 2:
                print("Raichu used Thunder")
                life_charizard -= 12
            elif enemie_attack == 3:
                print("Raichu used Quick attack")
                life_charizard -= 8

            if life_raichu < 0:
                life_raichu = 0
            elif life_charizard < 0:
                life_charizard = 0

            life_bar_charizard = int(life_charizard * life_bar / charizard)
            print("Charizar´s life: [{} {}] [{}/{}]".format("*" * life_bar_charizard, " " * (life_bar - life_bar_charizard),
                                                            life_charizard, charizard))
            life_bar_raichu = int(life_raichu * life_bar / raichu)
            print("Raichu´s life: [{} {}] [{}/{}]".format("*" * life_bar_raichu, " " * (life_bar - life_bar_raichu),
                                                            life_raichu, raichu))

            input ("Enter to continue...\n")

        if life_charizard == 0:
            print("Raichu wins!")
            return "Defeat"
        elif life_raichu == 0:
            print("Charizard wins")
            return "Victory"
        elif scape == True:
            return "Scape"
        return None


    @staticmethod
    def third_battle():
        charizard = 100
        venasaur = 100
        life_charizard = charizard
        life_venasaur = venasaur
        life_bar = 20
        scape = False

        life_bar_charizard = int(life_charizard * life_bar / charizard)
        print("Charizard´s life: [{} {}] [{}/{}]".format("*" * life_bar_charizard, " " * (life_bar - life_bar_charizard),
                                                         life_charizard, charizard))

        life_bar_venasaur = int(life_venasaur * life_bar / venasaur)
        print("Venasaur´s life: [{} {}] [{}/{}]".format("*" * life_bar_venasaur, " " * (life_bar - life_bar_venasaur),
                                                          life_venasaur, venasaur))

        # Turn´s begin
        while life_venasaur > 0 and life_charizard > 0:
            attack = None
            while attack != "A" and attack != "B" and attack != "C" and attack != "Q":
                attack = input("Charizard´s turn...\n"
                               "A. Embers\n"
                               "B. Flamethrower\n"
                               "C. Body blow\n"
                               "Q. Scape\n ")
                if attack == "A":
                    print("Charizard used Embers")
                    life_venasaur -= 12
                elif attack == "B":
                    print("Charizard used Flamethrower")
                    life_venasaur -= 15
                elif attack == "C":
                    print("Charizard used Body blow")
                    life_venasaur -= 10
                elif not ("A", "B", "C", "Q"):
                    print("You have to pick one of this four options!")

                if life_venasaur < 0:
                    life_venasaur = 0
                elif life_charizard < 0:
                    life_charizard = 0

            if attack == "Q":
                scape = True
                break

            os.system("clear")

            life_bar_charizard = int(life_charizard * life_bar / charizard)
            print("Charizard´s life: [{} {}] [{}/{}]".format("*" * life_bar_charizard, " " * (life_bar - life_bar_charizard),
                                                             life_charizard, charizard))

            life_bar_venasaur = int(life_venasaur * life_bar / venasaur)
            print("Venasaur´s life: [{} {}] [{}/{}]".format("*" * life_bar_venasaur, " " * (life_bar - life_bar_venasaur),
                                                              life_venasaur, venasaur))

            input("Enter to continue...\n")
            # Next Turn
            enemie_attack = random.randint(1,3)
            print("Venasaur´s turn...\n")
            if enemie_attack == 1:
                print("Venasaur used Sharp leaf")
                life_charizard -= 8
            elif enemie_attack == 2:
                print("Venasaur used Whip vine")
                life_charizard -= 10
            elif enemie_attack == 3:
                print("Venasaur used Body blow")
                life_charizard -= 12

            if life_venasaur < 0:
                life_venasaur = 0
            elif life_charizard < 0:
                life_charizard = 0

            life_bar_charizard = int(life_charizard * life_bar / charizard)
            print("Charizard´s life: [{} {}] [{}/{}]".format("*" * life_bar_charizard, " " * (life_bar - life_bar_charizard),
                                                             life_charizard, charizard))

            life_bar_venasaur = int(life_venasaur * life_bar / venasaur)
            print("Venasaur´s life: [{} {}] [{}/{}]".format("*" * life_bar_venasaur, " " * (life_bar - life_bar_venasaur),
                                                              life_venasaur, venasaur))

            input("Enter to continue...\n")

        if life_charizard == 0:
            print("Venasaur wins!")
            return "Defeat"
        elif life_venasaur == 0:
            print("Charizard wins!")
            return "Victory"
        elif scape == True:
            return "Scape"
        return None


    @staticmethod
    def fourth_battle():
        charizard = 100
        machamp = 100
        life_charizard = charizard
        life_machamp = machamp
        life_bar = 20
        scape = False

        life_bar_charizard = int(life_charizard * life_bar / charizard)
        print("Charizard´s life: [{} {}] [{}/{}]".format("*" * life_bar_charizard, " " * (life_bar - life_bar_charizard),
                                                         life_charizard, charizard))

        life_bar_machamp = int(life_machamp * life_bar / machamp)
        print("Machamp´s life: [{} {}] [{}/{}]".format("*" * life_bar_machamp, " " * (life_bar - life_bar_machamp),
                                                        life_machamp, machamp))

        # Turn´s begin
        while life_machamp > 0 and life_charizard > 0:
            attack = None
            while attack != "A" and attack != "B" and attack != "C" and attack != "Q":
                attack = input("Charizard´s turn...\n"
                               "A. Embers\n"
                               "B. Flamethrower\n"
                               "C. Body blow\n"
                               "Q. Scape\n ")
                if attack == "A":
                    print("Charizard used Embers")
                    life_machamp -= 12
                elif attack == "B":
                    print("Charizard used Flamethrower")
                    life_machamp -= 15
                elif attack == "C":
                    print("Charizard used Body blow")
                    life_machamp -= 10
                elif not ("A", "B", "C", "Q"):
                    print("You have to pick one of this four options!")

                if life_machamp < 0:
                    life_machamp = 0
                elif life_charizard < 0:
                    life_charizard = 0

            if attack == "Q":
                scape = True
                break

            os.system("clear")

            life_bar_charizard = int(life_charizard * life_bar / charizard)
            print("Charizard´s life: [{} {}] [{}/{}]".format("*" * life_bar_charizard, " " * (life_bar - life_bar_charizard),
                                                             life_charizard, charizard))

            life_bar_machamp = int(life_machamp * life_bar / machamp)
            print("Machamp´s life: [{} {}] [{}/{}]".format("*" * life_bar_machamp, " " * (life_bar - life_bar_machamp),
                                                           life_machamp, machamp))

            input("Enter to continue...\n")
            # Next Turn
            enemie_attack = random.randint(1,3)
            print("Machamp´s turn...\n")
            if enemie_attack == 1:
                print("Machamp used Cross-cut")
                life_charizard -= 8
            elif enemie_attack == 2:
                print("Machamp used Demolition")
                life_charizard -= 10
            elif enemie_attack == 3:
                print("Machamp used Mega-punch")
                life_charizard -= 12

            if life_machamp < 0:
                life_machamp = 0
            elif life_charizard < 0:
                life_charizard = 0

            life_bar_charizard = int(life_charizard * life_bar / charizard)
            print("Charizard´s life: [{} {}] [{}/{}]".format("*" * life_bar_charizard, " " * (life_bar - life_bar_charizard),
                                                             life_charizard, charizard))

            life_bar_machamp = int(life_machamp * life_bar / machamp)
            print("Machamp´s life: [{} {}] [{}/{}]".format("*" * life_bar_machamp, " " * (life_bar - life_bar_machamp),
                                                           life_machamp, machamp))

            input("Enter to continue...\n")

        if life_charizard == 0:
            print("Machamp wins!")
            return "Defeat"
        elif life_machamp == 0:
            print("Charizard wins!")
            return "Victory"
        elif scape == True:
            return "Scape"
        return None


    @staticmethod
    def fith_battle():
        charizard = 100
        pidgeot = 100
        life_charizard = charizard
        life_pidgeot = pidgeot
        life_bar = 20
        scape = False

        life_bar_charizard = int(life_charizard * life_bar / charizard)
        print("Charizard´s life: [{} {}] [{}/{}]".format("*" * life_bar_charizard, " " * (life_bar - life_bar_charizard),
                                                         life_charizard, charizard))

        life_bar_pidgeot = int(life_pidgeot * life_bar / pidgeot)
        print("Pidgeot´s life: [{} {}] [{}/{}]".format("*" * life_bar_pidgeot, " " * (life_bar - life_bar_pidgeot),
                                                       life_pidgeot, pidgeot))

        # Turn´s begin
        while life_pidgeot > 0 and life_charizard > 0:
            attack = None
            while attack != "A" and attack != "B" and attack != "C" and attack != "Q":
                attack = input("Charizard´s turn...\n"
                               "A. Embers\n"
                               "B. Flamethrower\n"
                               "C. Body blow\n"
                               "Q. Scape\n ")
                if attack == "A":
                    print("Charizard used Embers")
                    life_pidgeot -= 12
                elif attack == "B":
                    print("Charizard used Flamethrower")
                    life_pidgeot -= 15
                elif attack == "C":
                    print("Charizard used Body blow")
                    life_pidgeot -= 10
                elif not ("A", "B", "C", "Q"):
                    print("You have to pick one of this four options!")

                if life_pidgeot < 0:
                    life_pidgeot = 0
                elif life_charizard < 0:
                    life_charizard = 0

            if attack == "Q":
                scape = True
                break

            os.system("clear")

            life_bar_charizard = int(life_charizard * life_bar / charizard)
            print("Charizard´s life: [{} {}] [{}/{}]".format("*" * life_bar_charizard, " " * (life_bar - life_bar_charizard),
                                                             life_charizard, charizard))

            life_bar_pidgeot = int(life_pidgeot * life_bar / pidgeot)
            print("Pidgeot´s life: [{} {}] [{}/{}]".format("*" * life_bar_pidgeot, " " * (life_bar - life_bar_pidgeot),
                                                           life_pidgeot, pidgeot))

            input("Enter to continue...\n")
            # Next Turn
            enemie_attack = random.randint(1,3)
            print("Pidgeot´s turn...\n")
            if enemie_attack == 1:
                print("Pidgeot used Air strike")
                life_charizard -= 8
            elif enemie_attack == 2:
                print("Pidgeot used Wing attack")
                life_charizard -= 10
            elif enemie_attack == 3:
                print("Pidgeot used Tornado")
                life_charizard -= 12

            if life_pidgeot < 0:
                life_pidgeot = 0
            elif life_charizard < 0:
                life_charizard = 0

            life_bar_charizard = int(life_charizard * life_bar / charizard)
            print("Charizard´s life: [{} {}] [{}/{}]".format("*" * life_bar_charizard, " " * (life_bar - life_bar_charizard),
                                                             life_charizard, charizard))

            life_bar_pidgeot = int(life_pidgeot * life_bar / pidgeot)
            print("Pidgeot´s life: [{} {}] [{}/{}]".format("*" * life_bar_pidgeot, " " * (life_bar - life_bar_pidgeot),
                                                           life_pidgeot, pidgeot))

            input("Enter to continue...\n")

        if life_charizard == 0:
            print("Pidgeor wins!")
            return "Defeat"
        elif life_pidgeot == 0:
            print("Charizard wins!")
            return "Victory"
        elif scape == True:
            return "Scape"
        return None


    @staticmethod
    def sixth_battle():
        charizard = 100
        snorlax = 100
        life_charizard = charizard
        life_snorlax = snorlax
        life_bar = 20
        scape = False

        life_bar_charizard = int(life_charizard * life_bar / charizard)
        print("Charizard´s life: [{} {}] [{}/{}]".format("*" * life_bar_charizard, " " * (life_bar - life_bar_charizard),
                                                         life_charizard, charizard))

        life_bar_snorlax = int(life_snorlax * life_bar / snorlax)
        print("Snorlax´s life: [{} {}] [{}/{}]".format("*" * life_bar_snorlax, " " * (life_bar - life_bar_snorlax),
                                                       life_snorlax, snorlax))

        # Turn´s begin
        while life_snorlax > 0 and life_charizard > 0:
            attack = None
            while attack != "A" and attack != "B" and attack != "C" and attack != "Q":
                attack = input("Charizard´s turn...\n"
                               "A. Embers\n"
                               "B. Flamethrower\n"
                               "C. Body blow\n"
                               "Q. Scape\n ")
                if attack == "A":
                    print("Charizard used Embers")
                    life_snorlax -= 12
                elif attack == "B":
                    print("Charizard used Flamethrower")
                    life_snorlax -= 15
                elif attack == "C":
                    print("Charizard used Body blow")
                    life_snorlax -= 10
                elif not ("A", "B", "C", "Q"):
                    print("You have to pick one of this four options!")

                if life_snorlax < 0:
                    life_snorlax = 0
                elif life_charizard < 0:
                    life_charizard = 0

            if attack == "Q":
                scape = True
                break

            os.system("clear")

            life_bar_charizard = int(life_charizard * life_bar / charizard)
            print("Charizard´s life: [{} {}] [{}/{}]".format("*" * life_bar_charizard, " " * (life_bar - life_bar_charizard),
                                                             life_charizard, charizard))

            life_bar_snorlax = int(life_snorlax * life_bar / snorlax)
            print("Snorlax´s life: [{} {}] [{}/{}]".format("*" * life_bar_snorlax, " " * (life_bar - life_bar_snorlax),
                                                           life_snorlax, snorlax))

            input("Enter to continue...\n")
            # Next Turn
            enemie_attack = random.randint(1,3)
            print("Snorlax´s turn...\n")
            if enemie_attack == 1:
                print("Snorlax used Snoring")
                life_charizard -= 8
            elif enemie_attack == 2:
                print("Snorlax used Body blow")
                life_charizard -= 10
            elif enemie_attack == 3:
                print("Snorlax used Rest")
                print("...Snorlax fells sleep...")
                life_charizard -= 0

            if life_snorlax < 0:
                life_snorlax = 0
            elif life_charizard < 0:
                life_charizard = 0

            life_bar_charizard = int(life_charizard * life_bar / charizard)
            print("Charizard´s life: [{} {}] [{}/{}]".format("*" * life_bar_charizard, " " * (life_bar - life_bar_charizard),
                                                             life_charizard, charizard))

            life_bar_snorlax = int(life_snorlax * life_bar / snorlax)
            print("Snorlax´s life: [{} {}] [{}/{}]".format("*" * life_bar_snorlax, " " * (life_bar - life_bar_snorlax),
                                                           life_snorlax, snorlax))

            input("Enter to continue...\n")

        if life_charizard == 0:
            print("Snorlax wins!")
            return "Defeat"
        elif life_snorlax == 0:
            print("Charizard wins!")
            return "Victory"
        elif scape == True:
            return "Scape"
        return None


    @staticmethod
    def seventh_battle():
        charizard = 100
        golem = 100
        life_charizard = charizard
        life_golem = golem
        life_bar = 20
        scape = False

        life_bar_charizard = int(life_charizard * life_bar / charizard)
        print("Charizard´s life: [{} {}] [{}/{}]".format("*" * life_bar_charizard, " " * (life_bar - life_bar_charizard),
                                                         life_charizard, charizard))

        life_bar_golem = int(life_golem * life_bar / golem)
        print("Golem´s life: [{} {}] [{}/{}]".format("*" * life_bar_golem, " " * (life_bar - life_bar_golem),
                                                       life_golem, golem))

        # Turn´s begin
        while life_golem > 0 and life_charizard > 0:
            attack = None
            while attack != "A" and attack != "B" and attack != "C" and attack != "Q":
                attack = input("Charizard´s turn...\n"
                               "A. Embers\n"
                               "B. Flamethrower\n"
                               "C. Body blow\n"
                               "Q. Scape\n ")
                if attack == "A":
                    print("Charizard used Embers")
                    life_golem -= 12
                elif attack == "B":
                    print("Charizard used Flamethrower")
                    life_golem -= 15
                elif attack == "C":
                    print("Charizard used Body blow")
                    life_golem -= 10
                elif not ("A", "B", "C", "Q"):
                    print("You have to pick one of this four options!")

                if life_golem < 0:
                    life_golem = 0
                elif life_charizard < 0:
                    life_charizard = 0

            if attack == "Q":
                scape = True
                break

            os.system("clear")

            life_bar_charizard = int(life_charizard * life_bar / charizard)
            print("Charizard´s life: [{} {}] [{}/{}]".format("*" * life_bar_charizard, " " * (life_bar - life_bar_charizard),
                                                             life_charizard, charizard))

            life_bar_golem = int(life_golem * life_bar / golem)
            print("Golem´s life: [{} {}] [{}/{}]".format("*" * life_bar_golem, " " * (life_bar - life_bar_golem),
                                                         life_golem, golem))

            input("Enter to continue...\n")
            # Next Turn
            enemie_attack = random.randint(1,3)
            print("Golem´s turn...\n")
            if enemie_attack == 1:
                print("Golem used Rock strike")
                life_charizard -= 8
            elif enemie_attack == 2:
                print("Golem used Earthquake")
                life_charizard -= 10
            elif enemie_attack == 3:
                print("Golem used Avalanche")
                life_charizard -= 12

            if life_golem < 0:
                life_golem = 0
            elif life_charizard < 0:
                life_charizard = 0

            life_bar_charizard = int(life_charizard * life_bar / charizard)
            print("Charizard´s life: [{} {}] [{}/{}]".format("*" * life_bar_charizard, " " * (life_bar - life_bar_charizard),
                                                             life_charizard, charizard))

            life_bar_golem = int(life_golem * life_bar / golem)
            print("Golem´s life: [{} {}] [{}/{}]".format("*" * life_bar_golem, " " * (life_bar - life_bar_golem),
                                                         life_golem, golem))

            input("Enter to continue...\n")

        if life_charizard == 0:
            print("Golem wins!")
            return "Defeat"
        elif life_golem == 0:
            print("Charizard wins!")
            return "Victory"
        elif scape == True:
            return "Scape"
        return None
