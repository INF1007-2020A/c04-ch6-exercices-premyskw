#!/usr/bin/env python
# -*- coding: utf-8 -*-

def order(values: list = None) -> bool:
    if values is None:
        pass
    resultat = True
    index = 0
    while index < len(values) - 1:
        if values[index] > values[index+1]:
            resultat = False
            break
        index += 1
    return resultat

def anagrams(words: list = None) -> bool:
    if words is None:
        mot1 = str(input())
        mot2 = str(input())
        i = 0
        for char in mot1:
          i -= 1
          if char == mot2[i]:
            pass
          else:
            return False
    return True

def contains_doubles(items: list) -> bool:
    for elem in items:
      if items.count(elem) > 1:
        return True
    return False

def best_grades(student_grades: dict) -> dict:
    best_grade = {}
    highest_average = 0
    for key in student_grades:
      average = sum(student_grades[key]) / len(student_grades[key])
      if average > highest_average:
        highest_average = average
        best_grade = {}
        best_grade[key] = average
    return best_grade

def frequence(sentence: str) -> dict:
    sentence.replace(" ", "")
    frequency = dict()
    for letter in sentence:
        frequency[letter] = sentence.count(letter)
    sorted_keys = sorted(frequency, key=frequency.__getitem__, reverse=True)
    for key in sorted_keys:
        if frequency[key] > 5:
            print(f"Le caractere {key} revient {frequency[key]} fois.")

    return frequency

def get_recipes():
    recipe = {}
    nom = str(input("Entrez le nom de la recette: "))
    ingredients = str(input("Entrez les ingredients separes par ', ': ")).split(", ")
    recipe[nom] = ingredients
    return recipe

def print_recipe(ingredients) -> None:
    try:
      print(ingredients[str(input("Entrez le nom de la recette: "))])
    except:
      return False

def main() -> None:
    print(f"On essaie d'ordonner les valeurs...")
    order()

    print(f"On vérifie les anagrammes...")
    anagrams()

    my_list = [3, 3, 5, 6, 1, 1]
    print(f"Ma liste contient-elle des doublons? {contains_doubles(my_list)}")

    grades = {"Bob": [90, 65, 20], "Alice": [85, 75, 83]}
    best_student = best_grades(grades)
    print(f"{list(best_student.keys())[0]} a la meilleure moyenne: {list(best_student.values())[0]}")

    sentence = "bonjour, je suis une phrase. je suis compose de beaucoup de lettre. oui oui"
    frequence(sentence)

    print("On enregistre les recettes...")
    recipes = get_recipes()

    print("On affiche une recette au choix...")
    print_recipe(recipes)


if __name__ == '__main__':
    main()
