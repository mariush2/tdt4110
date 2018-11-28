class Cookies:
    percookie  = [
        400/48,
        320/48,
        500/48,
        2/48,
        460/48,
    ]
    recipe = [0, 0, 0, 0, 0]
    amount = 0;

    def __init__(self, amount):
        self.amount = amount;
        self.update();

    def update(self):
        for i, ingredient in enumerate(self.percookie):
            self.recipe[i] = ingredient * self.amount;

    def changeamount(self, amount):
        self.amount = amount;
        self.update();

    def tostring(self):
        print("Antall Cookies: " + str(self.amount));
        print("sukker(g): " + str(self.recipe[0]));
        print("smør(g): " + str(self.recipe[1]));
        print("sjokolade(g): " + str(self.recipe[2]));
        print("egg: " + str(self.recipe[3]));
        print("hvetemel(g): " + str(self.recipe[4]));

def askRecipe():
    amount = input("Hvor mange cookies? ");
    amount = int(amount);
    print(amount);
    recipe = Cookies(amount)
    recipe.tostring();
