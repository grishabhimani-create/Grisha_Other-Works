# Function using **kwargs

def report_card(**kwargs):
    print("----- Report Card -----")

    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Function call
report_card(
    Name="Amit",
    Age=18,
    Class="12th",
    Marks=92,
    Grade="A"
)
