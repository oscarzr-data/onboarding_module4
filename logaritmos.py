import math


def log_natural(x):
    if x > 0:
        return math.log(x)
    return "Value must be greater than 0"


def log_base10(x):
    if x > 0:
        return math.log10(x)
    return "Value must be greater than 0"


def log_base2(x):
    if x > 0:
        return math.log2(x)
    return "Value must be greater than 0"


def log_base_n(x, base):
    if x <= 0:
        return "Value must be greater than 0"
    if base <= 0 or base == 1:
        return "Base must be positive and not equal to 1"
    return math.log(x) / math.log(base)


def exponencial(x):
    return math.exp(x)


def potencia_de_10(x):
    return 10 ** x


def potencia_de_2(x):
    return 2 ** x


if __name__ == "__main__":
    valores = [0.5, 1, 2, 10, 100, 1000]
    print(f"{'x':>8} {'ln(x)':>10} {'log10(x)':>10} {'log2(x)':>10}")
    print("-" * 42)
    for v in valores:
        ln   = round(log_natural(v), 4)
        l10  = round(log_base10(v), 4)
        l2   = round(log_base2(v), 4)
        print(f"{v:>8} {str(ln):>10} {str(l10):>10} {str(l2):>10}")

    print(f"\nlog_base_5(125)  = {log_base_n(125, 5)}")
    print(f"exp(1)           = {round(exponencial(1), 6)}")
    print(f"10^3             = {potencia_de_10(3)}")
    print(f"2^8              = {potencia_de_2(8)}")