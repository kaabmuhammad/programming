import click


@click.command()
@click.option("--s", default="")
def to_arabic_number(s):
    roman = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
        "IV": 4,
        "IX": 9,
        "XL": 40,
        "XC": 90,
        "CD": 400,
        "CM": 900,
    }
    if s == "nulla":
        num += 0
    i = 0
    num = 0
    while i < len(s):
        if i + 1 < len(s) and s[i : i + 2] in roman:
            num += roman[s[i : i + 2]]
            i += 2
        else:
            # print(i)
            num += roman[s[i]]
            i += 1
    click.echo(f"The converted arabic numeral for the given roman numeral is {num}")


if __name__ == "__main__":
    to_arabic_number()
