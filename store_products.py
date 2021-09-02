class Store():
    def __init__(self, name):
        self.name = name
        self.products = []
    def add_product(self, new_product):
        self.products.append(new_product)
        print(self.products)
        return self
    def sell_product(self, id):
        for i in range(0,len(self.products)-1):
            if self.products[i] == id:
                self.products.remove(id)
                print(self.products)
            else:
                print(f"{id} not in stock")
        return self




class Product():
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category
    def update_price(self, percent_change, is_increased):
        if is_increased:
            self.price += self.price*percent_change
            return self
        else:
            self.price -= self.price*percent_change
            return self
    def print_info(self):
        print(self.name, self.category, self.price)
        return self


kroger = Store("Kroger")
print(kroger.name)

soup = Product("Soup", 3, "Can")
crackers = Product("Crackers", 4, "Box")
pop = Product("Pop", 1, "Bottle")

soup.print_info().update_price(.3, True).print_info()
crackers.print_info().update_price(.3, True).print_info()
pop.print_info().update_price(.3, True).print_info()

kroger.add_product(soup.name).add_product(pop.name).sell_product(soup.name).add_product(crackers.name).sell_product(pop.name)