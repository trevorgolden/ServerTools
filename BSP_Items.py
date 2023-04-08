import yaml

while True:
    shop_name = input("Enter shop name: ")
    item_type = input("Enter item type: ")
    buy_price = input("Enter buy price: ")
    sell_price = input("Enter sell price: ")
    inventory_slot = input("Enter inventory slot: ")

    config = f"""\
  {shop_name}:
    MenuItem:
    - type:{item_type}
    - amount:1
    - 'lore1:&6Left click to Buy %reward% for %price%'
    - 'lore2:&cClick &2right &eto sell &c%price_right% &efor &b%reward_right%&e.'
    RewardType: ITEM
    Reward:
    - - type:{item_type}
      - amount:1
    PriceType: MONEY
    Price: {buy_price}
    Message: '&eYou bought %reward%!'
    RewardType_right: MONEY
    Reward_right: {sell_price}
    PriceType_right: ITEM
    Price_right:
    - - type:{item_type}
      - amount:1
    Message_right: '&eYou just sold 1 {shop_name}!'
    ExtraPermission: ''
    InventoryLocation: {inventory_slot}

"""

    with open("config.yml", "a") as f:
        f.write(config)

    print("Item added to config!")

    add_more = input("Add another item? (y/n): ")
    if add_more.lower() != "y":
        break

print("Exiting program...")