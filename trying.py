import random
from functools import reduce

prefixes = ['Mystic', 'Golden', 'Dark', 'Shadow', 'Silver']
suffixes = ['storm', 'song', 'fire', 'blade', 'whisper']

def capitalize_suffix(word):
  return word.capitalize()

upper_word = list(map(capitalize_suffix, suffixes))

def create_fantasy_name(list_1, list_2):
  return random.choice(list_1) + ' ' + random.choice(list_2)

random_names = [create_fantasy_name(prefixes, upper_word) for _ in range(10)]

def fire_in_name(name):
  return 'Fire' in name 

def concatenate_names(name1, name2):
  return (f'{name1}{name2}')

fire_name = list(filter(fire_in_name, random_names))
add_filter = reduce(concatenate_names, fire_name)

def display_name_info():
  for name in random_names:
    print(name)
  print(fire_name)
  print(add_filter)

display_name_info()