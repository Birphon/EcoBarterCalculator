from tag import tag_list as tag
from Items import items_list as item


class SellingPrice:

    def __init__(self, currency=0, log=1, rock=5, ore=4, sand=1, clay=1, crop=10, bison=0.1) -> None:
        self.currency = currency
        self.log = log
        self.rock = rock
        self.ore = ore
        self.sand = sand
        self.clay = clay
        self.crop = crop
        self.bison = bison

    def tag_currency(self):
        tag.wood = self.currency+1
        tag.stone = self.currency+5
        tag.ore = self.currency+4
        item.sand = self.currency+1
        item.clay = self.currency+1
        tag.crop = self.currency+10
        tag.bison = self.currency+0.1
