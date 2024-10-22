# https://leetcode.com/discuss/interview-question/1003648/low-level-design-question-amazon

# In design round i was asked to Design a coupon and voucher managment system's Low level design.

# Requirements were:
# Admin will create coupons with rules(like match age>18 and cart_value>1000);
# Coupons will have (averall uses limit / per ser limit ), expiry date , active/inactive etc.

# Vouchers will be of type
# Unassigned : anyone can use but only one uses
# "PreAssigned": Voucher attached to user id

# Was asked to design api too:
# User will see list of coupons available and Vouchers;
# Admin can delete/ create , activate or disable coupons etc.


from enum import Enum
from abc import ABC, abstractmethod

# Enums
class TokenStatus(Enum):
    ACTIVE = 1
    INACTIVE = 2

class UserType(Enum):
    ADMIN = 1
    USER = 2

# Rule
class Rule:
    def __init__(self, rule_type, rule_value):
        self.rule_type = rule_type
        self.rule_value = rule_value

# Tokens
class Token(ABC):
    def __init__(self, id, limit):
        self.id = id
        self.limit = limit

    @abstractmethod
    def get_status(self):
        pass

class Coupon(Token):
    def __init__(self, id, limit, expiry_date, status, rules):
        super().__init__(id, limit)
        self.rules = rules
        self.status = status
        self.expiry_date = expiry_date

    def get_id(self):
        return self.id

    def get_status(self):
        return self.status

    def set_status(self, status):
        self.status = status

class Voucher(Token):
    def __init__(self, id, voucher_type, limit, user_id=None):
        super().__init__(id, limit)
        self.voucher_type = voucher_type
        self.user_id = user_id

    def get_id(self):
        return self.id

    def get_user_id(self):
        return self.user_id

# API
class TokenManager:
    def __init__(self, coupons, vouchers):
        self.coupons = coupons
        self.vouchers = vouchers

    def get_coupons(self):
        return self.coupons

    def get_vouchers(self):
        return self.vouchers

    def create_coupon(self, id, limit, expiry_date, status, rules):
        coupon = Coupon(id, limit, expiry_date, status, rules)
        self.add_coupon(coupon)

    def add_coupon(self, coupon):
        self.coupons.append(coupon)

    def delete_coupon(self, coupon_id):
        for i, coupon in enumerate(self.coupons):
            if coupon.get_id() == coupon_id:
                break
        self.coupons.pop(i)

    def activate_coupon(self, coupon_id):
        for coupon in self.coupons:
            if coupon.get_id() == coupon_id:
                coupon.set_status(TokenStatus.ACTIVE)
                break

    def deactivate_coupon(self, coupon_id):
        for coupon in self.coupons:
            if coupon.get_id() == coupon_id:
                coupon.set_status(TokenStatus.INACTIVE)
                break

    def create_voucher(self, id, voucher_type, limit, user_id):
        voucher = Voucher(id, voucher_type, limit, user_id)
        self.add_voucher(voucher)

    def add_voucher(self, voucher):
        self.vouchers.append(voucher)

# EndUsers
class Consumer(ABC):
    def __init__(self, role, token_manager):
        self.role = role
        self.token_manager = token_manager

    @abstractmethod
    def get_role(self):
        pass

    @abstractmethod
    def get_all_coupons(self):
        pass

class User(Consumer):
    def __init__(self, role, token_manager):
        super().__init__(role, token_manager)

    def get_role(self):
        return self.role

    def get_all_coupons(self):
        return self.token_manager.get_coupons()

class Admin(Consumer):
    def __init__(self, role, token_manager):
        super().__init__(role)
        self.token_manager = token_manager

    def get_role(self):
        return self.role

    def create_coupon(self, id, limit, expiry_date, status, rules):
        self.token_manager.create_coupon(id, limit, expiry_date, status, rules)

    def delete_coupon(self, coupon_id):
        self.token_manager.delete_coupon(coupon_id)

    def activate_coupon(self, coupon_id):
        self.token_manager.activate_coupon(coupon_id)

    def deactivate_coupon(self, coupon_id):
        self.token_manager.deactivate_coupon(coupon_id)

    def get_all_coupons(self):
        return self.token_manager.get_coupons()

if __name__ == "__main__":
    pass