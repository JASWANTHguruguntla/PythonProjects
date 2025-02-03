class Animal:
    def __init__(self, name, species, age, diet):
        self.name = name
        self.species = species
        self.age = age
        self.diet = diet

    def sound(self):
        return "Generic animal sound"


class Mammal(Animal):
    def __init__(self, name, species, age, diet, nocturnal=False):
        super().__init__(name, species, age, diet)
        self.nocturnal = nocturnal

    def sound(self):
        return f"{self.name} says: Roar or growl!"


class Bird(Animal):
    def __init__(self, name, species, age, diet, can_fly=True):
        super().__init__(name, species, age, diet)
        self.can_fly = can_fly

    def sound(self):
        return f"{self.name} says: Chirp or squawk!"


class Reptile(Animal):
    def __init__(self, name, species, age, diet, venomous=False):
        super().__init__(name, species, age, diet)
        self.venomous = venomous

    def sound(self):
        return f"{self.name} says: Hiss!"


class Enclosure:
    def __init__(self, enclosure_type, capacity):
        self.enclosure_type = enclosure_type
        self.capacity = capacity
        self.residents = []

    def add_animal(self, animal):
        if len(self.residents) < self.capacity:
            self.residents.append(animal)
            print(f"{animal.name} added to {self.enclosure_type} enclosure.")
        else:
            print(f"Enclosure {self.enclosure_type} is full. Cannot add {animal.name}.")

    def remove_animal(self, animal_name):
        self.residents = [animal for animal in self.residents if animal.name != animal_name]
        print(f"{animal_name} removed from {self.enclosure_type} enclosure.")

    def list_animals(self):
        return [f"{animal.name} ({animal.species})" for animal in self.residents]


class Staff:
    def __init__(self, name, role):
        self.name = name
        self.role = role
        self.assigned_enclosure = None

    def assign_to_enclosure(self, enclosure):
        self.assigned_enclosure = enclosure
        print(f"{self.name} assigned to {enclosure.enclosure_type} enclosure.")


def add_animal_to_enclosure(animal, enclosure):
    enclosure.add_animal(animal)


def transfer_animal(animal_name, source_enclosure, destination_enclosure):
    for animal in source_enclosure.residents:
        if animal.name == animal_name:
            source_enclosure.remove_animal(animal_name)
            destination_enclosure.add_animal(animal)
            print(f"{animal_name} transferred successfully.")
            return
    print(f"{animal_name} not found in {source_enclosure.enclosure_type} enclosure.")


def assign_staff_to_enclosure(staff, enclosure):
    staff.assign_to_enclosure(enclosure)


def search_animal_by_name_or_species(zoo, search_term):
    results = []
    for enclosure in zoo:
        for animal in enclosure.residents:
            if animal.name == search_term or animal.species == search_term:
                results.append((animal.name, animal.species, enclosure.enclosure_type))
    return results


def view_zoo_details(zoo):
    for enclosure in zoo:
        print(f"\nEnclosure: {enclosure.enclosure_type}")
        print(f"Capacity: {len(enclosure.residents)}/{enclosure.capacity}")
        print("Animals: ", ", ".join(enclosure.list_animals()) if enclosure.residents else "No animals")



if __name__ == "__main__":
    savanna = Enclosure("Savanna", 3)
    aviary = Enclosure("Aviary", 2)
    reptile_house = Enclosure("Reptile House", 2)
    
    lion = Mammal("Leo", "Lion", 5, "Carnivore", nocturnal=False)
    parrot = Bird("Polly", "Parrot", 2, "Herbivore", can_fly=True)
    snake = Reptile("Slyther", "Python", 4, "Carnivore", venomous=True)

    add_animal_to_enclosure(lion, savanna)
    add_animal_to_enclosure(parrot, aviary)
    add_animal_to_enclosure(snake, reptile_house)

    keeper = Staff("John", "Keeper")
    vet = Staff("Emma", "Veterinarian")

    assign_staff_to_enclosure(keeper, savanna)
    assign_staff_to_enclosure(vet, reptile_house)


    print("\n--- Zoo Overview ---")
    view_zoo_details([savanna, aviary, reptile_house])

    print("\n--- Search Results ---")
    search_results = search_animal_by_name_or_species([savanna, aviary, reptile_house], "Python")
    for result in search_results:
        print(f"Found {result[0]} ({result[1]}) in {result[2]} enclosure.")

    print("\n--- Transferring Animal ---")
    transfer_animal("Polly", aviary, savanna)

    print("\n--- Zoo Overview After Transfer ---")
    view_zoo_details([savanna, aviary, reptile_house])
