from client_interface import app_logo
import pandas as pd

# Files
filename = "Dear_Universe/dear_universe.xlsx"
planets_db = pd.read_excel(filename, sheet_name="Planets", header=0)

def app_menu():
    print("1. Planets")
    print("2. Moons")
    print("3. Constellations")

    menu_choice()

def menu_choice():
    while True:
        try:
            i = input("What is your choice ? > ")
            if i in ["1", "2", "3"]:
                # If user chooses 1, send to the Planets def
                if i in "1":
                    planets()
                # If user chooses 2, send to the Moons def
                elif i in "2":
                    print()
                # If user chooses 3, send to the Constellations def
                elif i in "3":
                    print()
            else:
                raise AssertionError
        # If neither of 1, 2, 3 choices, returns an error and lets the User try again
        except AssertionError:
            print("An error has occured.\n")

def planets():
    while True:
        try:
            p = input("Which planet would you like to see ? > ")
            if p in ["mercury", "venus", "neptune", "mars", "jupiter", "earth", "uranus", "saturn"]:
                if p in "mercury":
                    planet = planets_db.loc[planets_db["planet"] == p].get("planet").to_string(index=False)
                    print(f"You chose {planet}")
                elif p in "venus":
                    planet = planets_db.loc[planets_db["planet"] == p].get("planet").to_string(index=False)
                    print(f"You chose {planet}")
                elif p in "neptune":
                    planet = planets_db.loc[planets_db["planet"] == p].get("planet").to_string(index=False)
                    print(f"You chose {planet}")
                elif p in "mars":
                    planet = planets_db.loc[planets_db["planet"] == p].get("planet").to_string(index=False)
                    print(f"You chose {planet}")
                elif p in "jupiter":
                    planet = planets_db.loc[planets_db["planet"] == p].get("planet").to_string(index=False)
                    print(f"You chose {planet}")
                elif p in "earth":
                    planet = planets_db.loc[planets_db["planet"] == p].get("planet").to_string(index=False)
                    print(f"You chose {planet}")
                elif p in "uranus":
                    planet = planets_db.loc[planets_db["planet"] == p].get("planet").to_string(index=False)
                    print(f"You chose {planet}")
                elif p in "saturn":
                    planet = planets_db.loc[planets_db["planet"] == p].get("planet").to_string(index=False)
                    print(f"You chose {planet}")
            else:
                raise AssertionError
        except AssertionError:
            print("An error has occured.\n")

app_menu()