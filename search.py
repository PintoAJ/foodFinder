import tkinter as tk

# root window
root = tk.Tk()
root.title("Food Finder")
root.geometry('800x700')

# search bar
entry = tk.Entry(root, width=50)
entry.place(x=150, y=20)

# search button
search_button = tk.Button(root, text="Search",width=20, height=2)
search_button.place(x=250, y=625)

filters = [
    ("Location:", ["Toronto", "Brock", "Oshawa", "Burlington", "Oakville", "Brampton", "Mississauga", "Markham", "Vaughan"]),
    ("Cuisines:", ["Canadian", "American", "Ramen", "Seafood", "Italian", "French", "Jamaican", "Mediterranean", "Burgers", "Steakhouse", "Global", "Thai", "Somalian", "Mexican", "Indian", "Chinese", "European", "Japanese", "Iranian", "Irish"]),
    ("Dietary Restrictions:", ["Halal", "Gluten Free", "Kosher", "Vegetarian"])
]

# BooleanVars to track the state of checkboxes
location_vars = [tk.BooleanVar() for _ in range(len(filters[0][1]))]
cuisine_vars = [tk.BooleanVar() for _ in range(len(filters[1][1]))]
restriction_vars = [tk.BooleanVar() for _ in range(len(filters[2][1]))]

# initial y position for title, options, and checkboxes
y_position = 100

for (label, options), var_list in zip(filters, [location_vars, cuisine_vars, restriction_vars]):
    # create label for the filter category
    tk.Label(root, text=label, font=("Poppins", 17, "bold")).place(x=10, y=y_position)
    
    # checkboxes for each option in the category
    for i, option in enumerate(options):
        # column and row positions for placing the checkboxes
        col = i % 3
        row = i // 3
        tk.Checkbutton(root, text=option, variable=var_list[i]).place(x=10 + col * 200, y=y_position + 25 + row * 25)
    y_position += (len(options) + 2) // 3 * 25 + 50

root.mainloop()


