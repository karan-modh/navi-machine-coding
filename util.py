import math

def amount_left_after_emi_payment(emi_amount, num_of_emis, amount_left):
    return amount_left - emi_amount*num_of_emis

def amount_left_after_lump_sum_payment(emi_amount, num_of_emis, lump_sum_amount, amount_left):
    return amount_left_after_emi_payment(emi_amount, num_of_emis, amount_left) - lump_sum_amount

def calculate_num_emis_left(amount_left, emi_amount):
    return math.ceil(amount_left/emi_amount)
