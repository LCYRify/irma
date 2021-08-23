def try_me():

    name = input("Enter your name : ")

    cities = ['Tokyo', 'Delhi', 'Seoul', 'Shanghai', 'Sao Paulo', 'Mexico', 'Cairo', 'Mumbai', 'Beijing',
              'Dhaka', 'Osaka','New York', 'Karachi', 'Buenos Aires', 'Chongqinq',
              'Istanbul', 'Kolkata', 'Manila', 'Lagos', 'Rio de Janeiro']

    if name.lower() in ['maxime', 'etienne']:
        print("You are gonna live in Paris in the future")
    else:
        print(f"You are gonna live in {random.choice(cities)} in the future")
