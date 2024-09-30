class Item:
    def __init__(self, name, price):
        self.name = str(name)
        self.price = float(price)

    def __str__(self):
        return f"{self.name}: {self.price} Kč."


class Pizza(Item):
    def __init__(self, name, price, ingredients):
        super().__init__(name, price)
        self.ingredients = ingredients
        self.total_price = price

    def add_extra(self, ingredient, quantity, price_per_ingredient):
        self.price_per_ingredient = price_per_ingredient
        self.ingredient = ingredient
        self.quantity = quantity
        if ingredient in self.price_per_ingredient:
            self.ingredients[ingredient] = quantity
            self.total_price += quantity * self.price_per_ingredient[ingredient]
        else:
            print(f"Ingredience {ingredient} není k dispozici.")

    def __str__(self):
        ingredient_list = [f"{ingredient} ({quantity}g)" for ingredient, quantity in self.ingredients.items()]
        ingredients_str = ", ".join(ingredient_list)
        return super().__str__() + f", Ingredients: {ingredients_str}, Total price: {self.total_price} Kč"

    
ingredients = {
    "cheese": 300,
    "ham": 200,
    "mushrooms": 100,
    "garlic": 50,
    "olives": 80
    
}

price_per_ingredient = {
    "olives": 0.07,
    "cheese": 0.10,
    "ham": 0.08,
    "mushrooms": 0.03,
    "garlic": 0.02
}

pizza_se_vsemi_ingrediencemi = Pizza("Sunkova pizza", 190, ingredients)
print(pizza_se_vsemi_ingrediencemi)

pizza_se_syrem = Pizza("Sunkova pizza se sýrem", 210, {"cheese": 300, "ham": 200})
print(pizza_se_syrem)

# Přidání extra ingredience
pizza = Pizza("Žampionová", 250, {"mushrooms": 100, "olives": 80})
pizza.add_extra("ham", 400, price_per_ingredient)
print(pizza)

margarita = Pizza("Margarita", 200, {"sýr": 100, "rajčata": 150})
margarita.add_extra("olives", 100, price_per_ingredient)
print(margarita)

class Drink(Item):
    def __init__(self, name, volume, price):
        super().__init__(name, price)
        self.volume = int(volume)
    def __str__(self):
        return f" Nápoj: {self.name}, objem {self.volume}ml stojí {self.price} Kč"
    
napoj = Drink("Coca cola", 300, 27)
print(napoj)


class Order:
    def __init__(self, customer_name, delivery_address, items, status):
        self.customer_name = str(customer_name)
        self.delivery_address = str(delivery_address)
        self.items = list(items)
        self.status = str(status)

    def mark_delivered(self):

        self.status = "Doručeno"

    def __str__(self):
        item_list = ",".join(str(item) for item in self.items)
        return f"Zákazník {self.customer_name}, adresa doručení {self.delivery_address}, objednávka {item_list}, stav objednávky: {self.status}"
    
objednavka_1 = Order("Pan X", "Brno-střed 146", [margarita, napoj], "nová")

print(objednavka_1)

class DeliveryPerson:
    def __init__(self, name, phone_number, available=True, current_order=None):
        self.name = str(name)
        self.phone_number = str(phone_number)
        self.available = bool(available)
        self.current_order = current_order

    def assign_order(self, order):
        if self.available:
            self.current_order = order
            order.status = "Na cestě"
        else:
            self.available = False
    
# complete_delivery(): Označí objednávku jako doručenou a doručovatele znovu učiní dostupným.
    def complete_delivery(self):
        if self.current_order:
            self.current_order.mark_delivered()
            self.available = True
            self.current_order = None


    def __str__(self):
        if self.available:
            availability = "Dostupný" 
        else:
            "Nedostupný"
            
        if self.current_order:
            order_info = f", aktuální objednávka: {self.current_order}"
    
        else:
            order_info = ""

        return f"Doručovatel {self.name}, telefonní číslo {self.phone_number}, dostupnost {availability}, objednávka číslo: {self.current_order}."
    
delivery_person = DeliveryPerson("Pepa Nový", "123456789", available=True)
print(delivery_person)  

# Přiřazení objednávky
delivery_person.assign_order(objednavka_1)
print(delivery_person) 

# Dokončení doručení
delivery_person.complete_delivery()
print(delivery_person) 

print(objednavka_1)
