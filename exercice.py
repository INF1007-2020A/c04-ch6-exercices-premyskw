#!/usr/bin/env python
# -*- coding: utf-8 -*-

def order(values: list = None) -> list:
    if values is None:
        # TODO: demander les valeurs ici
        for i in range(9):
            value = float(input("Entrez une valeur: "))
            values.append(value)
        values.sort()

    return values


def anagrams(words: list = None) -> bool:
    if words is None:
        # TODO: demander les mots ici
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
    # TODO: Retourner un dictionnaire contenant le nom de l'étudiant ayant la meilleure moyenne ainsi que sa moyenne
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
    # TODO: Afficher les lettres les plus fréquentes
    #       Retourner le tableau de lettres
    wordcount = {}
    wordlist = list(sentence)
    for elem in wordlist:
      wordcount[elem] = wordlist.count(elem)
    
    return sorted(wordcount.items(), key=lambda x: x[1], reverse=True)

def get_recipes():
    # TODO: Demander le nom d'une recette, puis ses ingredients et enregistrer dans une structure de données
    recipe = {}
    nom = str(input("Entrez le nom de la recette: "))
    ingredients = str(input("Entrez les ingredients separes par ', ': ")).split(", ")
    recipe[nom] = ingredients
    
    return recipe


def print_recipe(ingredients) -> None:
    # TODO: Demander le nom d'une recette, puis l'afficher si elle existe
    
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
