import random
import string

def stworz_haslo(z):
    random_source = string.ascii_letters + string.digits + string.punctuation
    haslo = random.choice(string.ascii_lowercase)
    haslo += random.choice(string.ascii_uppercase)
    haslo += random.choice(string.digits)
    haslo += random.choice(string.punctuation)
    for i in range((z-4)):
       haslo += random.choice(random_source)
    return haslo

print(stworz_haslo(10))
# ,,z" ktore podajesz uzywajac metody to liczba znakow inaczej dlugosc hasla (: