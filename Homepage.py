import tkinter as tk
from tkinter import ttk


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
        self.hide()
        self.search_page.show()


class SearchPage(Page):
    def __init__(self, parent):
        super().__init__(parent)
        self.search_frame = ttk.Frame(self.parent)
        self.search_frame.pack(fill='both', expand=True)

        # Add widgets for search page
        label = ttk.Label(self.search_frame, text="Search Page")
        label.pack(pady=10)

        # Add back button
        back_button = ttk.Button(self.search_frame, text="Back", command=self.go_back)
        back_button.pack(pady=10)

    def go_back(self):
        self.hide()
        self.parent.home_page.show()


root = tk.Tk()

# Define styles
style = ttk.Style(root)
style.configure('Green.TFrame', background='green')
style.configure('AppName.TLabel', background='green', foreground='white', font=('Arial', 16, 'bold'))
style.configure('Circle.TFrame', background='white', borderwidth=2, relief='solid')
style.configure('Plus.TButton', font=('Arial', 16, 'bold'))

app = FoodDeliveryApp(root)
root.mainloop()
