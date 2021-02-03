from sys import argv


file_name, virabotka, stavka, premiya = argv

print(f"заработная плата работника равна {int(virabotka) * int(stavka) + int(premiya)}")
