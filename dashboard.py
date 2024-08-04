import mesop as me
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import base64

# Sample data for the table and chart
data = {
    "Category": ["A", "B", "C", "D"],
    "Value": [10, 15, 7, 12]
}

df = pd.DataFrame(data)

# Function to convert a Matplotlib plot to a base64 string
def plot_to_base64():
    plt.figure(figsize=(5, 3))
    plt.bar(df['Category'], df['Value'], color='skyblue')
    plt.xlabel('Category')
    plt.ylabel('Value')
    plt.title('Sample Data Chart')
    buf = BytesIO()
    plt.savefig(buf, format='png')
    plt.close()
    buf.seek(0)
    return base64.b64encode(buf.read()).decode('utf-8')

# Define the state for the application
@me.stateclass
class State:
    name: str = ""
    age: int = 0
    data: pd.DataFrame = df

# Define the navigation bar component
@me.component
def navbar():
    me.button("Home", path="/")
    me.button("Form", path="/form")
    me.button("Data", path="/data")

# Define the form page
@me.page(path="/form")
def form_page():
    state = me.state(State)
    me.header("User Information Form", size="h3")
    state.name = me.text_input("Name", value=state.name)
    state.age = me.number_input("Age", value=state.age, min=0)
    if me.button("Submit"):
        me.text(f"Hello, {state.name}. You are {state.age} years old.")

# Define the data page
@me.page(path="/data")
def data_page():
    state = me.state(State)
    me.header("Data Table and Chart", size="h3")
    me.dataframe(state.data)
    img_data = plot_to_base64()
    me.image(src=f"data:image/png;base64,{img_data}")

# Define the main page
@me.page(path="/")
def main_page():
    me.header("Welcome to the Data Dashboard", size="h1")
    me.text("Use the navigation bar to access different features.")

# Define the layout
@me.content_component
def layout():
    with me.box():
        navbar()
        me.slot()

# Define the scaffold to use the layout
@me.component
def scaffold():
    with layout():
        main_page()

# Run the application
if __name__ == "__main__":
    me.run()
