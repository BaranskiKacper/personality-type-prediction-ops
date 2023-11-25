import random
import customtkinter as ctk
import webbrowser
from chart_frame import ChartFrame
from tkinter import filedialog


class PredictFrame(ctk.CTkFrame):
    def __init__(self, master, back_callback, method):
        super().__init__(master, width=400, height=300)
        self.back_callback = back_callback
        self.method = method

        coins, category_name = self.get_names()

        # Segmented button
        self.segmented_button_var = ctk.StringVar(value=coins[0])
        self.segmented_button = ctk.CTkSegmentedButton(
            self,
            values=coins,
            command=self.segmented_button_callback,
            variable=self.segmented_button_var,
            height=30,
            width=300,
            dynamic_resizing=False,
        )
        self.segmented_button.pack(side="top", pady=(10))

        # Label to display the selected option
        self.selected_label = ctk.CTkLabel(self, text="", font=('Arial', 16))
        self.selected_label.pack(pady=8)

        # Create a frame for the buttons
        button_frame = ctk.CTkFrame(self, fg_color="transparent")
        button_frame.pack(side="bottom", pady=10, padx=10, anchor="center")

        # Try again button
        ctk.CTkButton(button_frame, text="Try again", command=self.back, width=100, height=40, font=('Arial', 14)).pack(
            side="left", padx=10)

        # Save button
        self.save_button = ctk.CTkButton(button_frame, text="Save", command=self.save, width=100,
                                         height=40, font=('Arial', 14))
        self.save_button.pack(side="left", padx=10)

        # Show chart button
        self.show_chart_button = ctk.CTkButton(button_frame, text="Show chart", command=self.show_chart, width=100,
                                               height=40,
                                               font=('Arial', 14))
        self.show_chart_button.pack(side="right", padx=10)

        # Set default value to "Human" and update the label
        self.segmented_button_var.set(coins[0])
        self.segmented_button_callback(coins[0])

        # Hyperlink at the bottom, centered
        self.hyperlink_label = ctk.CTkLabel(self, text="Find your twin and analyze the type", font=('Arial', 14),
                                            cursor="hand2",
                                            text_color="#1F6AA5")
        self.hyperlink_label.bind("<Button-1>", lambda event: self.open_browser(
            "http://app.subjectivepersonality.com/analyzer?m=FF&s1=Fe&s2=Se&a=PCSB"))
        self.hyperlink_label.pack(side="bottom")

    def back(self):
        if self.back_callback:
            # Go back to the previous frame
            self.back_callback()
            self.destroy()

    def save(self):

        # Retrieve data
        coins, category_name = self.get_names()
        categories, values = self.get_data()

        # Create a string with the formatted data
        result_str = f"Predicted coins (method for prediction -> {self.method}):\n"

        for i, category in enumerate(categories):
            if i == 0:
                result_str += f"\n{coins[0]} coins:\n"
            if i == 3:
                result_str += f"\n{coins[1]} coins:\n"
            if i == 7:
                result_str += f"\n{coins[2]} coins:\n"
            if i == 9:
                result_str += f"\n{coins[3]} coins:\n"

            result_str += f"'{category_name[i]}': {category} {values[i]}%\n"

        # Ask the user for the file name and location
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")],
                                                 initialfile=[f"prediction_{self.method}.txt"])

        # Check if the user clicked "Cancel" or closed the dialog
        if not file_path:
            print("Save operation canceled.")
            return

        # Save the data to the selected file
        with open(file_path, "w") as file:
            file.write(result_str)

        print(f"Data saved to {file_path}")

    def open_browser(self, url):
        webbrowser.open(url)

    def get_data(self):
        observer = "Oi"
        decider = "Di"
        preferences = "OO"
        observing = "Si"
        deciding = "Ti"
        energy = "Sleep"
        info = "Consume"
        dominant = "Info"
        intro_extro = "Extro"
        sensory = "modality0"
        ex_decider = "modality1"

        rand1 = random.randint(55, 90)
        rand2 = random.randint(55, 90)
        rand3 = random.randint(55, 90)
        rand4 = random.randint(55, 90)
        rand5 = random.randint(55, 90)
        rand6 = random.randint(55, 90)
        rand7 = random.randint(55, 90)
        rand8 = random.randint(55, 90)
        rand9 = random.randint(55, 90)
        rand10 = random.randint(55, 90)
        rand11 = random.randint(55, 90)

        categories = [observer, decider, preferences, observing, deciding, energy, info, dominant, intro_extro, sensory,
                      ex_decider]
        values = [rand1, rand2, rand3, rand4, rand5, rand6, rand7, rand8, rand9, rand10, rand11]

        return categories, values

    def get_names(self):

        coins = ["Human", "Letter", "Animal", "Sexual"]

        category_name = ["Observer", "Decider", "Preferences", "Observer", "Decider", "Energy Animal", "Info Animal",
                         "Dominant Animal", "Introverted vs Extraverted", "Sensory", "Extraverted Decider"]

        return coins, category_name,

    def segmented_button_callback(self, value):
        print("Segmented button clicked:", value)

        coins, category_name = self.get_names()
        categories, values = self.get_data()

        # Update the label text based on the selected option
        if value == f'{coins[0]}':
            text = f"'{category_name[0]}': {categories[0]} {values[0]}%\n\n" + \
                   f"'{category_name[1]}': {categories[1]} {values[1]}%\n\n" + \
                   f"'{category_name[2]}': {categories[2]} {values[2]}%"
            cat = [categories[0], categories[1], categories[2]]
            val = [values[0], values[1], values[2]]
        elif value == f'{coins[1]}':
            text = f"'{category_name[3]}': {categories[3]} {values[3]}%\n\n" + \
                   f"'{category_name[4]}': {categories[4]} {values[4]}%"
            cat = [categories[3], categories[4]]
            val = [values[3], values[4]]
        elif value == f'{coins[2]}':
            text = f"'{category_name[5]}': {categories[5]} {values[5]}%\n\n" + \
                   f"'{category_name[6]}': {categories[6]} {values[6]}%\n\n" + \
                   f"'{category_name[7]}': {categories[7]} {values[7]}%\n\n" + \
                   f"'{category_name[8]}': {categories[8]} {values[8]}%"
            cat = [categories[5], categories[6], categories[7], categories[8]]
            val = [values[5], values[6], values[7], values[8]]
        elif value == f'{coins[3]}':
            text = f"'{category_name[9]}': {categories[9]} {values[9]}%\n\n" + \
                   f"'{category_name[10]}': {categories[10]} {values[10]}%"
            cat = [categories[9], categories[10]]
            val = [values[9], values[10]]

        # Set the label text
        self.selected_label.configure(text=text)

        return cat, val

    def show_chart(self):
        selected_option = self.segmented_button_var.get()
        print(f"Showing chart for option: {selected_option}")

        # Retrieve data based on the selected option
        categories, values = self.segmented_button_callback(selected_option)

        # Create and pack the ChartFrame with the provided data
        self.chart_frame = ChartFrame(self, categories, values, selected_option)
        self.chart_frame.place(in_=self, relwidth=1, relheight=1)
        self.chart_frame.lift()