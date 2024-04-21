# Initiate hash_table or a dictionary
my_menu = {
  'lasagna': 14.75,
  'moussaka': 21.15,
  'sushi': 16.05,
  'paella': 21,
  'samosas': 14
}

# Iterate the key and value of the dictionary
for key, value in my_menu.items():
    print(f"Menu: {key} = {value}")


# Initiate nested dictionary
my_menu1 = {
  'sushi' : {
    'price' : 19.25,
    'best_served' : 'cold'
  },
  'paella' : {
    'price' : 15,
    'best_served' : 'hot'
  },
  'samosa' : {
    'price' : 14,
    'best_served' : 'hot'
  },
  'gazpacho' : {
    'price' : 8,
    'best_served' : 'cold'
  }
}

# Iterate the key and value of the dictionary
for key, value in my_menu1.items():
    print(f"{key.title()} is best served {value['best_served']}")

