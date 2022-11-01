"""Demonstrate defining a module imported elsewhere."""


THE_ANSWER: int = 42


def main() -> None:
    print(power(2,10))
    print("helpers.py run as a module")



def powerful(x: float, n: float) -> float:
    """Riase x to the power of n."""
    return x ** n 

# Idiom for making a module ble to run as a program 
# or have its global definitions imported elsewhere.
if __name__ == "__main__":
    main()
else:
    # It is not idiomatic to have an else branch
    print("helpers.py was evaluated")
