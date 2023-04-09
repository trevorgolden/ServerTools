import os
import yaml
print("BossShopPro Shop Creator")
print("Created by Trevor, BlastGamingMC")
# get list of yml files from dir
yaml_files = [f for f in os.listdir('.') if f.endswith('.yml')]

# display yml files ask user to select or create new one
if yaml_files:
    print("Select a Shop .yml file:")
    for i, f in enumerate(yaml_files):
        print(f"{i+1}. {f}")
    print(f"{len(yaml_files)+1}. Create new shop .yml file")
else:
    print("No YAML files found in current directory")
file_index = None
while file_index is None:
    try:
        if yaml_files:
            file_index = int(input("Enter the number of the file to use: "))
            if file_index < 1 or file_index > len(yaml_files) + 1:
                raise ValueError()
        else:
            file_index = len(yaml_files) + 1
        if file_index == len(yaml_files) + 1:
            filename = input("Enter the name for the new YAML file: ")
            if not filename.endswith('.yml'):
                filename += '.yml'
            yaml_files.append(filename)
            open(filename, 'a').close()
            # Add shop configuration block to new YAML file
            shopName = input("Enter the shop name: ")
            shopDisplayName = input("Enter the shop display name: ")
            shopCommand = input("Enter the shop command: ")
            shopSignText = input("Enter the shop sign text: ")
            config = f"""\
ShopName: {shopName}
DisplayName: '{shopDisplayName}'
Command: {shopCommand}
signs:
  text: '[{shopSignText}]'
  NeedPermissionToCreateSign: true
shop:
"""
            with open(filename, "w") as f:
                f.write(config)
        else:
            filename = yaml_files[file_index-1]
    except ValueError:
        print("Error: invalid input")
        file_index = None

# loop to add items to the shop file
while True:
    item_name = input("Enter a unique identifier for the item in the shop: ")
    item_type = input("Enter Item Material Ex. GRASS_BLOCK: ")
    buy_price = input("Enter buy price: ")
    sell_price = input("Enter sell price: ")
    inventory_slot = input("Enter inventory slot(Minimum 1 Maximum 54): ")

    config = f"""\
  {item_name}:
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
    Message_right: '&eYou just sold 1 {item_name}!'
    ExtraPermission: ''
    InventoryLocation: {inventory_slot}

"""

    with open(filename, "a") as f:
        f.write(config)

    print("Item added to config!")

    add_more = input("Add another item? (y/n): ")
    if add_more.lower() != "y":
        break

print("Exiting program...")
