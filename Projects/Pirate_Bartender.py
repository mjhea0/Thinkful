import random

all_questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?"
}

ingredients = {
    "strong": ["glug of rum", "slug of whiskey", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bcaon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"]
}


def questions():
    preferences = {}
    for key, val in all_questions.iteritems():
        response = raw_input(val)
        if (response == 'y' or response == 'yes'):
            preferences[key] = True
        else:
            preferences[key] = False
    return preferences


def create_drink(preferences):
    drink = []
    for preference, value in preferences.iteritems():
        if value:
            drink.append(random.choice(ingredients[preference]))
    return drink


def main():
    flavor = questions()
    served = create_drink(flavor)
    print "One drink coming right up!"
    print "Your drink's recipe includes: "
    for ingredient in served:
        print ingredient

if __name__ == '__main__':
    main()
