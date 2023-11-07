from typing import Tuple

UI = False


def main():
    formula_1, formula_2 = get_formulae()

    chemical_set_1 = get_chemicals_in_formula(formula_1)
    chemical_set_2 = get_chemicals_in_formula(formula_2)

    state_common_chemicals(chemical_set_1, chemical_set_2)


def get_formulae(user_interface: bool = UI) -> Tuple[str]:
    """Asks the user for two chemical formulae, and returns them."""

    formula_1 = input("Enter a chemical formula:\n" if user_interface else "")
    formula_2 = input("Enter another chemical formula:\n" if user_interface else "")

    return formula_1, formula_2


def get_chemicals_in_formula(chemical_formula: str) -> set:
    """Returns the set of element found in the formula."""
    compounds = chemical_formula.split()
    print(compounds)
    chemical_set = set()

    for item in compounds:
        # if itme is a compund add it to the dict else dont add it 
        

        # compoint is 1
        # compond is 2
        pass 

    return chemical_set


def state_common_chemicals(chemical_set_1: set, chemical_set_2: set) -> None:
    """Prints the chemicals common to both sets, in alphabetical order."""

    common_chemicals = chemical_set_1 & chemical_set_2

    print()


if __name__ == "__main__":
    main()
