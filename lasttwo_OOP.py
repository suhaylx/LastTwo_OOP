class User:
    def sign_in(self):
        print("Joined ")


class Archer(User):
    def __init__(self, name, arch):
        self.name = name
        self.arch = arch

    def num_archs(self):
        print(f"Attacking and number of arrows left {self.arch}")

    def run(self):
        print("Running fast")


class Wizard(User):
    def __init__(self, name, power_lvl):
        self.name = name
        self.power_lvl = power_lvl

    def attack(self):
        print(f"Attacking with {self.power_lvl}")


class HybridBorg(Wizard, Archer):
    def __init__(self, name, arch, power_lvl):
        Archer.__init__(self, name, arch)
        Wizard.__init__(self, name, power_lvl)


hybrid_gamer = HybridBorg("Kura", 100, 75)
print(f"{hybrid_gamer.name} has")
hybrid_gamer.sign_in()
hybrid_gamer.attack()
hybrid_gamer.run()
hybrid_gamer.num_archs()
