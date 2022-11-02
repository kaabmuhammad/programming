import click


@click.command()
@click.option("--num", default=1)
def to_roman_numeral(num):
    val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    syb = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    roman_num = ""
    i = 0
    if num == 0:
        roman_num += "nulla"
    while num > 0:
        for _ in range(num // val[i]):
            roman_num += syb[i]
            num -= val[i]
        i += 1
    click.echo(f"The converted roman numeral for the arabic number is {roman_num}")


if __name__ == "__main__":
    to_roman_numeral()
