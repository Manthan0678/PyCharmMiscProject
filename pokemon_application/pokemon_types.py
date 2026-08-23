# pokemon type matrix
def pokemon_type_matrix(type_list):
    type_matrix ={
        "Fire":{
            "strong_against":["Grass","Bug","Ice","Steel"],
            "weak_to":["Water","Rock","Ground"]
            },
        "Water":{
            "strong_against":["Fire","Ground","Rock"],
            "weak_to":["Grass","Electric"]
        },
        "Grass":{
            "strong_against":["Water","Ground","Rock"],
            "weak_to":["Fire","Ice","poison","Flying","Bug"]
        },
        "Electric":{
            "strong_against":["Water","Flying"],
            "weak_to":["Ground"]
        },
        "Fighting":{
            "strong_against":["Dark","Ice","Normal","Rock","Steel"],
            "weak_to":["Flying","Psychic","Fairy"]
        },
        "Psychic":{
            "strong_against":["Fighting","Poison"],
            "weak_to":["Bug","Dark","Ghost"]
        },
        "Poison":{
            "strong_against":["Grass"],
            "weak_to":["Ground","Psychic"]
        },
        "Ground":{
            "strong_against":["Electric","Fire","Poison","Rock","Steel"],
            "weak_to":["Ice","Water","Grass"]
        },
        "Bug":{
            "strong_against":["Psychic","Dark","Grass"],
            "weak_to":["Rock","Flying","Fire"]
        },
        "Dark":{
            "strong_against":["Ghost","Psychic"],
            "weak_to":["Bug","Fighting"]
        },
        "Flying":{
            "strong_against":["Grass","Bug","Fighting"],
            "weak_to":["Electric","Ice","Rock"]
        },
        "Dragon":{
            "strong_against":["Dragon"],
            "weak_to":["Dragon","Fairy","Ice"]
        },
        "Fairy":{
            "strong_against":["Dragon","Dark","Fighting"],
            "weak_to":["Steel","Poison"]
        },
        "Ghost":{
            "strong_against":["Ghost","Psychic"],
            "weak_to":["Dark","Ghost"]
        },
        "Ice":{
            "strong_against":["Dragon","Flying","Grass","Ground"],
            "weak_to":["Fighting","Fire","Rock","Steel"]
        },
        "Rock":{
            "strong_against":["Bug","Flying","Fire","Ice"],
            "weak_to":["Fighting","Grass","Ground","Steel","Water"]
        },
        "Steel":{
            "strong_against":["Fairy","Ice","Rock"],
            "weak_to":["Fighting","Fire","Ground"]
        },
        "Normal":{
            "strong_against":[],
            "weak_to":["Fighting"]
        }
    }
    for single_type in type_list:
        if single_type.title() in type_matrix:
            dictionary = type_matrix[single_type.title()]
            strengths = dictionary["strong_against"]
            weakness = dictionary["weak_to"]
            print("stats of "+str(single_type.title()+" type :"))
            print("strong against "+str(strengths))
            print("weak to "+str(weakness))
        else:
            print("pokemon type not found")