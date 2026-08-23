def build_pokemon_team():#main function is only to take pokemon team.
    print("welcome trainer")
    pokemon_team = []
    print("create your 6 member pokemon team")
    print("type undo to remove your previously entered pokemon")
    while len(pokemon_team) < 6 :
        enter_pokemon = input(str("enter your pokemon ")).strip().lower()
        if enter_pokemon == "undo" and len(pokemon_team) >=1 :
            removed = pokemon_team.pop()
            print(str(removed)+"  removed from team")
        elif enter_pokemon == "undo" and len(pokemon_team) < 1:
            print("your pokemon team is empty")
        elif enter_pokemon != "undo":
            pokemon_team.append(enter_pokemon)
            print("current team: "+str(pokemon_team))
    print("pokemon team successfully built")
    convert_to_string =",".join(pokemon_team)
    return convert_to_string
if __name__ == "__main__":
    build_pokemon_team()