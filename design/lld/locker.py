# Design a locker system

# locker - small, medium, large
# package - small, medium, large
# number of packages
# number of lockers

# Small l, w < 400
# Medium 400 <= l, w <= 800
# large 800 < l, w <= 1600  

from abc import ABC, abstractmethod

class Package:
    def __init__(self, name, length, width):
        self.name = name
        self.length = length
        self.width = width
        self.locker_id = None

    def get_length(self):
        return self.length
    
    def get_width(self):
        return self.width
    
    def get_locker_id(self):
        return self.locker_id

    def set_locker_id(self, locker_id):
        self.locker_id = locker_id

class Locker(ABC):
    def __init__(self, id, length, width, is_available=True):
        self.id = id
        self.length = length
        self.width = width
        self.is_available = is_available

    @abstractmethod
    def get_id(self):
        pass
    
    def get_length(self):
        return self.length
    
    def get_width(self):
        return self.width
    
class SmallLocker(Locker):
    def __init__(self, id, is_available=True):
        super().__init__(id, 400, 400, is_available)

    def get_id(self):
        return self.id
    
class MediumLocker(Locker):
    def __init__(self, id, is_available=True):
        super().__init__(id, 800, 800, is_available)

    def get_id(self):
        return self.id
    
class LargeLocker(Locker):
    def __init__(self, id, is_available=True):
        super().__init__(id, 1600, 1600, is_available)

    def get_id(self):
        return self.id
    
class LockerManagement:
    def __init__(self, lockers):
        self.lockers = lockers
        self.organise_lockers()

    def organise_lockers(self):
        self.locker_dict = {
            "small": dict(),
            "medium": dict(),
            "large": dict()
        }

        for locker in self.lockers:
            if locker.get_length() <= 400 and locker.get_width() <= 400:
                self.locker_dict["small"][locker.id] = locker
            elif locker.get_length() <= 800 and locker.get_width() <= 800:
                self.locker_dict["medium"][locker.id] = locker
            elif locker.get_length() <= 1600 and locker.get_width() <= 1600:
                self.locker_dict["large"][locker.id] = locker

    def get_next_available(self, size):
        for lid, locker in self.locker_dict[size].items():
            if locker.is_available:
                return lid
            
        return None

    def insert_into_hub(self, package):
        length = package.get_length()
        width = package.get_width()

        if package.get_locker_id() is None and length < 400 and width < 400:
            lid = self.get_next_available("small")
            if lid is not None:
                package.set_locker_id(lid)
                self.locker_dict["small"][lid].is_available = False
        if package.get_locker_id() is None and length <= 800 and width <= 800:
            lid = self.get_next_available("medium")
            if lid is not None:
                package.set_locker_id(lid)
                self.locker_dict["medium"][lid].is_available = False
        if package.get_locker_id() is None and length <= 1600 and width <= 1600:
            lid = self.get_next_available("large")
            if lid is not None:
                package.set_locker_id(lid)
                self.locker_dict["large"][lid].is_available = False

        return package

if __name__ == "__main__":
    lm = LockerManagement(
        [SmallLocker("1"), SmallLocker("2"), MediumLocker("3"), LargeLocker("4"), LargeLocker("5"), SmallLocker("4")]
        )
    print(lm.locker_dict)
    pack1 = Package("pack1", 200, 300)
    pack11 = Package("p11", 200, 300)
    pack2 = Package("pack2", 500, 800)
    pack3 = Package("p3", 600, 700)
    pack4 = Package("p4", 1500, 700)
    pack5 = Package("p5", 1200, 1100)
    
    for pack in [pack1, pack11, pack2, pack3, pack4, pack5]:
        pack = lm.insert_into_hub(pack)
        if pack.get_locker_id() is not None:
            print(f"Package is in locker, {pack.get_locker_id()}")
        if pack.get_locker_id() is None:
            print("Doesn't fit")