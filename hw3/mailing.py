from adress import Address
class Mailing:
    def __init__(self, to_address, from_address, cost, track):
        self.to_address = to_address
        self.from_address = from_address
        self.cost = cost
        self.track = track

    class toAdress:
        to_address = Address("123456", "Moscov", "st. Lenina", "5", "1")
        from_address = Address("987654", "Sochi", "st. Red", "6", "1")   

