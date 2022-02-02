# Workshop OOP

## Découvrez la programmation orientée objet

### C'est quoi un objet ?

Un objet est une instance de classe. C'est une structure de données qui contient des variables ou des fonctions (ou d'autres objets).

Un équivalent grossier en C:
```c
typedef struct
{
    int data1;
    char data2;
} object;

// Plus tard dans le code

object *obj = malloc(sizeof(object));
// obj->data1
// obj->data2
```

Une structure en C permet de stocker des données. Le principe est le même avec un object, avec des comportements supplémentaire.

### Du coup c'est quoi une classe ?

> Un objet est une instance de classe.

Ok, c'est bien beau mais c'est quoi ce truc ? Une classe est un type de données, un modèle qu'on utilisera pour créer un objet.

Si on reprend l'exemple du dessus, la "classe" serait la définition de la structure.

## En Python ça se passe comment ?
### Créer un objet

La déclaration d'une classe se fait comme suit:
```py
class Klass:
    def __init__(self):
        self.data1 = 5
        self.data2 = 'c'
```

Dans l'utilisation:
```py
def main():
    obj = Klass()
    print(obj.data1)
    print(obj.data2)
```

Un peu d'explication s'impose. Comme dit plus haut, un objet contient des variables (qu'on va nommer `attributs`) et des fonctions (des `methodes`).

La fonction `__init__` (ou méthode, vu qu'elle est définie dans une classe) sert à **construire** l'objet.
C'est dans cette fonction qu'on va initialiser les attributs de notre objet.

Rien n'empêche par la suite de modifier les valeurs:
```py
def main():
    obj = Klass()
    print(obj.data1)
    print(obj.data2)
    obj.data1 = 156
    obj.data2 = 'Other'
    print(obj.data1)
    print(obj.data2)
```
#### C'est quoi `self` ?
`self` est une variable spécifique, qui doit être présente dans chanque méthode que vous déclarez. Elle est en faite une référence sur l'obet qui appelle la méthode.
```py
class Klass:
    def __init__(self):
        self.data1 = 5
        self.data2 = 'c'

    def print(self):
        print(self.data1, self.data2)

def main():
    obj = Klass()
    obj.print()  # Pas besoin de redonner 'obj' en paramètre, ça se fera tout seul :)
    Klass.print(obj)  # Là on récupère la méthode depuis la classe, il lui faut donc l'objet à utiliser
```
#### On peut donner plusieurs arguments à une méthode ?
Bien sûr !
```py
class Klass:
    def __init__(self, data1, data2):
        self.data1 = data1
        self.data2 = data2

    def print(self):
        print(self.data1, self.data2)

def main():
    obj = Klass(5, 'c')  # N'oubliez pas que ça va implicitement appeler __init__
    obj.print()
```

#### Pourquoi ne pas directement appeler `__init__` ?
Bah essayons:
```py
class Klass:
    def __init__(self, data1, data2):
        self.data1 = data1
        self.data2 = data2

    def print(self):
        print(self.data1, self.data2)

def main():
    obj = Klass.__init__(<something>, 5, 'c')  # Vous mettez quoi à la place de <something> ?
    obj.print()
```
S'il a été possible d'initialiser notre objet, c'est qu'il a bien été créé à un moment précis. Le processus de création d'un objet va le créer, puis appeler le constructeur afin que vous puissiez l'initialiser.

## Pourquoi faire des objets ?

### Modéliser la vie réelle
Un objet sert avant tout à modéliser des choses de la vie réelle. Un `attribut` sert à garder des informations sur ce qu'on modélise, tandis qu'une méthode définit une action possible avec notre objet.

Prenons l'exemple d'une personne. On sait qu'une personne a:
- un prénom
- un nom
- un âge

Du coup toutes ses informations seront les attributs de notre objet.

Maintenant, il est possible qu'une personne sache parler (en théorie) pour se présenter. Ce sera fait avec une méthode.
```py
class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def present(self):
        print(f"My name is {self.first_name} {self.last_name}. I am {self.age}.")

def main():
    jack = Person("Jack", "Anderson", 38)
    john = Person("John", "Doe", 56)
    jack.present()
    john.present()
```
Tout ce qu'on a dit a été retranscrit dans une classe `Person`, et on peut se servir des objets pour créer (littéralement) une personne.
