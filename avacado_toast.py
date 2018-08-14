class Avacado_Toast():
    def toast(self):
        print("First put the bread in the toaster.")

    def avacado(self):
        print("Then peel the skin off the avacado, remove the pit, and mash the avacado in a bowl.")

    def season(self):
        print("Then season the avacado in the bowl with salt, pepper, and oil.")

    def bread_done(self):
        print("Then take the bread out of the toaster when the toaster is done toasting the bread.")

    def assembling(self):
        print("Then spread the mashed, seasoned avacado on the toasted bread so that it is evenly spread on the surface.")

    def eat(self):
        print("Lastly, eat the delicious avacado toast sandwich! Yummmm!")

def making_breakfast(sandwich):
    sandwich.toast()
    sandwich.avacado()
    sandwich.season()
    sandwich.bread_done()
    sandwich.assembling()
    sandwich.eat()

for_lauren = Avacado_Toast()

making_breakfast(for_lauren)
