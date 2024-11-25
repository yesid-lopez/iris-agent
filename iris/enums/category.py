from enum import Enum


class CategoryEnum(str, Enum):
    product = "product"
    refund = "refund"
    other = "other"
