class Gym(object):
    def __init__(self, name, equipments=None, members=None):
        self.name = name
        self.equipments = equipments
        self.members = members

    def __str__(self):
        result = self.name + " gym. It has\n"
        for equip in self.equipments:
            result += str(equip) + "\n"
        for member in self.members:
            result += str(member) + "\n"

        return result

    def add_member(self, member):

        if type(member) is Member:
            self.members.append(member)
        else:
            print("{} is not an instance of Member".format(str(member)))


class Equipment(object):
    def __init__(self, id: int, name):
        self.id = id
        self.name = name

    def __str__(self):
        return "Equipment id {}, named {}".format(self.id, self.name)


class Member(object):
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return "Member id {}, named {}".format(self.id, self.name)


equipments = [Equipment(1, "Treadmill"), Equipment(2, "Rowing Machine")]
members = [Member(1, "Lucas"), Member(2, "Sarah")]

my_gym = Gym("Lucas", equipments, members)
print(my_gym)

# new_member = Member(3, "Eoin")
# my_gym.add_member(new_member)
# print(my_gym)
