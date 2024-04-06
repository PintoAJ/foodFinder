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
        self.results_page = ResultsPage(self.main_container)

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

        # Add a frame to display saved results
        self.dashboard_frame = ttk.Frame(self.home_frame)
        self.dashboard_frame.pack(fill='both', expand=True)
        self.display_saved_results()

    def display_saved_results(self):
        # saved results from the database
        conn = sqlite3.connect("project.db")
        c = conn.cursor()
        c.execute("SELECT id, result FROM dashboard_results")
        saved_results = c.fetchall()
        conn.close()

        if saved_results:
            self.no_saved_label.pack_forget()

            # display saved results
            saved_results_label = ttk.Label(self.dashboard_frame, text="Saved Results", font=("Arial", 16, 'bold'))
            saved_results_label.pack(pady=10)

            for result_id, result_text in saved_results:
                result_frame = ttk.Frame(self.dashboard_frame)
                result_frame.pack(fill='x', padx=10, pady=5)

                # display text result
                result_label = ttk.Label(result_frame, text=result_text, font=('Arial', 12))
                result_label.pack(side='left', padx=10, pady=5)

                # delete button
                delete_button = ttk.Button(result_frame, text="Delete", command=lambda id=result_id: self.delete_result(id))
                delete_button.pack(side='right', padx=10, pady=5)
        else:
            self.no_saved_label.pack(expand=True)

    def delete_result(self, result_id):
        # Delete the result with the given ID from the database
        conn = sqlite3.connect("project.db")
        c = conn.cursor()
        c.execute("DELETE FROM dashboard_results WHERE id=?", (result_id,))
        conn.commit()
        conn.close()

        # Refresh the display of saved results
        self.refresh_dashboard()

    def refresh_dashboard(self):
        for widget in self.dashboard_frame.winfo_children():
            widget.destroy()
        self.display_saved_results()

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
            ("Location:",
             ["Toronto", "Brock", "Oshawa", "Burlington", "Oakville", "Brampton", "Mississauga", "Markham", "Vaughan"]),
            ("Cuisines:",
             ["Canadian", "American", "Ramen", "Seafood", "Italian", "French", "Jamaican", "Mediterranean", "Burgers",
              "Steakhouse", "Global", "Thai", "Somalian", "Mexican", "Indian", "Chinese", "European", "Japanese",
              "Iranian", "Irish"]),
            ("Dietary Restrictions:", ["Halal", "Gluten_Free", "Kosher", "Vegetarian"])
        ]

        print(self.filters)

        # BooleanVars to track the state of checkboxes
        self.location_vars = [tk.BooleanVar() for _ in range(len(self.filters[0][1]))]
        self.cuisine_vars = [tk.BooleanVar() for _ in range(len(self.filters[1][1]))]
        self.restriction_vars = [tk.BooleanVar() for _ in range(len(self.filters[2][1]))]

        # initial y position for title, options, and checkboxes
        y_position = 100

        for (label, options), var_list in zip(self.filters,
                                              [self.location_vars, self.cuisine_vars, self.restriction_vars]):
            # create label for the filter category
            tk.Label(self.search_frame, text=label, background='grey', bg='grey', font=("Poppins", 17, "bold")).place(
                x=10, y=y_position)

            # checkboxes for each option in the category
            for i, option in enumerate(options):
                # column and row positions for placing the checkboxes
                col = i % 3
                row = i // 3
                tk.Checkbutton(self.search_frame, text=option, variable=var_list[i]).place(x=10 + col * 200,
                                                                                           y=y_position + 25 + row * 25)
            y_position += (len(options) + 2) // 3 * 25 + 50

    def go_back(self):
        global app

        # self.hide()
        # app.home_page.show()

        self.search_frame.pack_forget()
        app.home_page.home_frame.pack(fill='both', expand=True)

    def search(self):
        global app
        self.search_frame.pack_forget()
        app.results_page.results_frame.pack(fill='both', expand=True)

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

        #for r in rs:
            #print(r)

        conn.commit()
        conn.close()

        # Display search results
        app.results_page.display_results(rs)

    def open_results_page(self):
        global app
        self.search_frame.pack_forget()
        app.results_page.results_frame.pack(fill='both', expand=True)


class ResultsPage(Page):
    def __init__(self, parent):
        super().__init__(parent)
        self.results_frame = ttk.Frame(self.parent)
        # self.results_frame.pack(fill='both', expand=True)
        
        # Add back button
        back_button = ttk.Button(self.results_frame, text="Back", command=self.go_back)
        back_button.pack(pady=10)

        # Add label title for the results
        self.results_label = ttk.Label(self.results_frame, text="Search Results", font=("Arial", 16, 'bold'))
        self.results_label.pack(pady=10)

        # Add a canvas to hold the result frames
        self.canvas = tk.Canvas(self.results_frame, background='white')
        self.canvas.pack(side='left', fill='both', expand=True)

        # Add a scrollbar for the canvas
        scrollbar = ttk.Scrollbar(self.results_frame, orient='vertical', command=self.canvas.yview)
        scrollbar.pack(side='right', fill='y')
        self.canvas.configure(yscrollcommand=scrollbar.set)

        # Create a frame to contain the result frames
        self.results_container = ttk.Frame(self.canvas)
        self.results_container.bind('<Configure>', self.on_frame_configure)

        # Add the results container to the canvas
        self.canvas.create_window((0, 0), window=self.results_container, anchor='nw')

    def on_frame_configure(self, event):
        """Update scroll region whenever the size of the frame changes."""
        self.canvas.configure(scrollregion=self.canvas.bbox('all'))

    def go_back(self):
        global app
        self.results_frame.pack_forget()
        app.home_page.home_frame.pack(fill='both', expand=True)
        
    def save_result(self, result):
            # connect to the SQLite database
            conn = sqlite3.connect("project.db")
            c = conn.cursor()

            # create a table 
            c.execute('''CREATE TABLE IF NOT EXISTS dashboard_results 
            (record_id integer primary key, 
            search_result text)''')

            # insert the result into the database
            c.execute("INSERT INTO dashboard_results (result) VALUES (?)", (str(result),))

            # commit and close the connection
            conn.commit()
            conn.close()

            print("Result saved to dashboard:", result)


    def display_results(self, results):
        """Display the search results."""
        for result in results:
            # create a frame for each result
            result_frame = ttk.Frame(self.results_container, relief='solid', borderwidth=0)
            result_frame.pack(fill='x', padx=10, pady=5)

            # display the result information 
            result_label = ttk.Label(result_frame, text=result, font=('Arial', 12))
            result_label.pack(side='left', padx=10, pady=5)

            # save button for each result
            save_button = ttk.Button(result_frame, text="Save", command=lambda r=result: self.save_result(r))
            save_button.pack(side='right', padx=10, pady=5)


root = tk.Tk()
root.geometry('800x700')

# Define styles
style = ttk.Style(root)
style.configure('Green.TFrame', background='green', bg='green')
style.configure('AppName.TLabel', background='green', bg='green', foreground='white', fg='white',
                font=('Arial', 16, 'bold'))
style.configure('Circle.TFrame', background='white', bg='white', borderwidth=2, relief='solid')
style.configure('Plus.TButton', font=('Arial', 16, 'bold'))

app = FoodDeliveryApp(root)
root.mainloop()
