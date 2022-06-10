from tag import tag_list as tag
from Items import items_list as item

class SellingPrice:
	def price_logic:
		# 1 currency = 1 log = 5 rock = 4 ore = 1 sand/clay = 10 crop = 0.1 Bison
		Currency = 0
		Log = 1
		Rock = 5
		Ore = 4
		Sand = 1
		Clay = 1
		Crop = 10
		Bison = 0.1
		
	def tag_currency:
		tag(wood) = currency+1
		tag(stone) = currency+5
		tag(ore) = 4
		item(sand) = 1
		item(clay) = 1
		tag(crop) = 10
		tag(bison) = 0.1