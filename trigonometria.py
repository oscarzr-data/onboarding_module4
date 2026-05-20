import math


def seno(angulo_grados):
    angulo_rad = math.radians(angulo_grados)
    return math.sin(angulo_rad)


def coseno(angulo_grados):
    angulo_rad = math.radians(angulo_grados)
    return math.cos(angulo_rad)


def tangente(angulo_grados):
    if angulo_grados % 180 == 90:
        return "Undefined (vertical asymptote)"
    angulo_rad = math.radians(angulo_grados)
    return math.tan(angulo_rad)


def hipotenusa(cateto_a, cateto_b):
    return math.sqrt(cateto_a ** 2 + cateto_b ** 2)


def angulo_desde_seno(valor):
    if -1 <= valor <= 1:
        return math.degrees(math.asin(valor))
    return "Value out of range [-1, 1]"


def angulo_desde_coseno(valor):
    if -1 <= valor <= 1:
        return math.degrees(math.acos(valor))
    return "Value out of range [-1, 1]"


def angulo_desde_tangente(valor):
    return math.degrees(math.atan(valor))


if __name__ == "__main__":
    angulos = [0, 30, 45, 60, 90]
    print(f"{'Angle':>8} {'sin':>10} {'cos':>10} {'tan':>15}")
    print("-" * 45)
    for a in angulos:
        s = round(seno(a), 4)
        c = round(coseno(a), 4)
        t = tangente(a)
        t_display = round(t, 4) if isinstance(t, float) else t
        print(f"{a:>8} {str(s):>10} {str(c):>10} {str(t_display):>15}")

    print(f"\nHypotenuse (3, 4) = {hipotenusa(3, 4)}")
    print(f"Angle from sin(0.5) = {angulo_desde_seno(0.5):.2f}°")
    print(f"Angle from cos(0.5) = {angulo_desde_coseno(0.5):.2f}°")
    print(f"Angle from tan(1.0) = {angulo_desde_tangente(1.0):.2f}°")