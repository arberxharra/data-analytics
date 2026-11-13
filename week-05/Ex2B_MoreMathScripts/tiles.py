import math

room_length = 14
room_width = 11
tiles_per_box = 12
extra_tiles_rate = 0.10

tiles_needed = room_length * room_width
tiles_with_extra = tiles_needed * (1 + extra_tiles_rate)
boxes_to_buy = math.ceil(tiles_with_extra / tiles_per_box)

print(f"Tiles needed: {tiles_needed}")
print(f"Boxes to buy, including 10% extra: {boxes_to_buy}")