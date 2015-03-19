import random

questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?"
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"]
}

def questioner(questiondict):
  answerdict = {}
  for flav, question in questiondict.iteritems():
    answer = raw_input("{} ".format(question))
    if answer == 'yes' or answer == 'y':
      answerdict[flav] = True
    else:
      answerdict[flav] = False 
  return answerdict

def tender(answersdict, ingredientsdict):
  drink = []
  for flav, answer in answersdict.iteritems():
    if answersdict[flav] == True:
      ingredientslist = ingredientsdict[flav]
      drink.append(random.choice(ingredientslist))
  return drink

if __name__ == '__main__':
  answers = questioner(questions)
  drinklist = tender(answers, ingredients) 
  print "Your drink consists of: {}.".format( ', '.join(drinklist) )