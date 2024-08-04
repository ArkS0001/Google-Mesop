import mesop as me

@me.page()
def main():
    me.text("Welcome to Mesop!")
    if me.button("Click me"):
        me.text("Button clicked!")

if __name__ == "__main__":
    me.run()
