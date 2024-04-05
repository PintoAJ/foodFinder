import tkinter as tk
from tkinter import ttk
import sqlite3
import sql

class FoodDeliveryApp:
    def __init__(self, root):
        
        self.root = root
        self.root.title("Food Finder")

        # Create main container
        self.main_container = ttk.Frame(self.root)
        self.main_container.pack(fill='both', expand=True)

        # Create pages
        self.home_page = HomePage(self.main_container)
        self.search_page = SearchPage(self.main_container)

        # Show home page initially
        self.home_page.show()


class Page:
    def __init__(self, parent):
        self.parent = parent

    def show(self):
        self.parent.pack(fill='both', expand=True)

    def hide(self):
        self.parent.pack_forget()


class HomePage(Page):
    def __init__(self, parent):
        super().__init__(parent)
        self.home_frame = ttk.Frame(self.parent)
        self.home_frame.pack(fill='both', expand=True)

        # Add green nav bar
        nav_bar = ttk.Frame(self.home_frame, height=50, style='Green.TFrame')
        nav_bar.pack(side='top', fill='x')

        # Add app name to nav bar
        app_name_label = ttk.Label(nav_bar, text="Food Finder", style='AppName.TLabel')
        app_name_label.pack(pady=5)

        # Add circle with '+' button
        circle_frame = ttk.Frame(self.home_frame, width=100, height=100, style='Circle.TFrame')
        circle_frame.pack(side='bottom', anchor='se', padx=10, pady=10)
        plus_button = ttk.Button(circle_frame, text="+", style='Plus.TButton', command=self.open_search_page)
        plus_button.pack()

        # Add text when there are no saved searches
        self.no_saved_label = ttk.Label(self.home_frame,
                                        text="You have no saved searches.\nClick the '+' button below to create a new "
                                             "search!",
                                        font=('Arial', 12), foreground='gray')
        self.no_saved_label.pack(expand=True)

    def open_search_page(self):
        global app
        
        # self.hide()
        # app.search_page.show()
        
        self.home_frame.pack_forget()
        app.search_page.search_frame.pack(fill='both', expand=True)


class SearchPage(Page):
    def __init__(self, parent):
        super().__init__(parent)
        self.search_frame = ttk.Frame(self.parent)
        # self.search_frame.pack(fill='both', expand=True)

        # Add widgets for search page
        # label = ttk.Label(self.search_frame, text="Search Page")
        # label.pack(pady=10)

        # Add back button
        back_button = ttk.Button(self.search_frame, text="Back", command=self.go_back)
        back_button.pack(pady=10)
        
        # search button
        search_button = tk.Button(self.search_frame, text="Search", command=self.search, width=20, height=2)
        search_button.place(x=250, y=625)

        # self.filters = {
        #     "Location:": ["Toronto", "Brock", "Oshawa", "Burlington", "Oakville", "Brampton", "Mississauga", "Markham", "Vaughan"],
        #     "Cuisines:": ["Canadian", "American", "Ramen", "Seafood", "Italian", "French", "Jamaican", "Mediterranean", "Burgers", "Steakhouse", "Global", "Thai", "Somalian", "Mexican", "Indian", "Chinese", "European", "Japanese", "Iranian", "Irish"],
        #     "Dietary Restrictions:": ["Halal", "Gluten Free", "Kosher", "Vegetarian"],
        # }
        
        self.filters = [
            ("Location:", ["Toronto", "Brock", "Oshawa", "Burlington", "Oakville", "Brampton", "Mississauga", "Markham", "Vaughan"]),
            ("Cuisines:", ["Canadian", "American", "Ramen", "Seafood", "Italian", "French", "Jamaican", "Mediterranean", "Burgers", "Steakhouse", "Global", "Thai", "Somalian", "Mexican", "Indian", "Chinese", "European", "Japanese", "Iranian", "Irish"]),
            ("Dietary Restrictions:", ["Halal", "Gluten_Free", "Kosher", "Vegetarian"])
        ]
        
        # print(self.filters)

        # BooleanVars to track the state of checkboxes
        self.location_vars = [tk.BooleanVar() for _ in range(len(self.filters[0][1]))]
        self.cuisine_vars = [tk.BooleanVar() for _ in range(len(self.filters[1][1]))]
        self.restriction_vars = [tk.BooleanVar() for _ in range(len(self.filters[2][1]))]

        # initial y position for title, options, and checkboxes
        y_position = 100

        for (label, options), var_list in zip(self.filters, [self.location_vars, self.cuisine_vars, self.restriction_vars]):
            # create label for the filter category
            tk.Label(self.search_frame, text=label, background='grey', bg='grey', font=("Poppins", 17, "bold")).place(x=10, y=y_position)
            
            # checkboxes for each option in the category
            for i, option in enumerate(options):
                # column and row positions for placing the checkboxes
                col = i % 3
                row = i // 3
                tk.Checkbutton(self.search_frame, text=option, variable=var_list[i]).place(x=10 + col * 200, y=y_position + 25 + row * 25)
            y_position += (len(options) + 2) // 3 * 25 + 50

    def go_back(self):
        global app
        
        # self.hide()
        # app.home_page.show()
        
        self.search_frame.pack_forget()
        app.home_page.home_frame.pack(fill='both', expand=True)
    
    def search(self):
        conn = sqlite3.connect("project.db")
        c = conn.cursor()
        sql.init_db(c)
        
        selected_locations = [self.filters[0][1][i] for i, loc in enumerate(self.location_vars) if loc.get()]
        selected_cuisines = [self.filters[1][1][i] for i, cuis in enumerate(self.cuisine_vars) if cuis.get()]
        selected_restrictions = [self.filters[2][1][i] for i, rest in enumerate(self.restriction_vars) if rest.get()]

        # print("Selected Locations:", selected_locations)
        # print("Selected Cuisines:", selected_cuisines)
        # print("Selected Dietary Restrictions:", selected_restrictions)
        
        rs = sql.get_restaurants(c, selected_locations, selected_cuisines, selected_restrictions)
        
        # for r in rs:
        #     print(r)
        
        conn.commit()
        conn.close()

root = tk.Tk()
root.geometry('800x700')

# Define styles
style = ttk.Style(root)
style.configure('Green.TFrame', background='green', bg='green')
style.configure('AppName.TLabel', background='green', bg='green', foreground='white', fg='white', font=('Arial', 16, 'bold'))
style.configure('Circle.TFrame', background='white', bg='white', borderwidth=2, relief='solid')
style.configure('Plus.TButton', font=('Arial', 16, 'bold'))

app = FoodDeliveryApp(root)
root.mainloop()
