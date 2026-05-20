import datetime
import os
import math
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# ─────────────────────────────────────────
#  Base Operations
# ─────────────────────────────────────────
class BasicCalculator:
    """Arithmetic operations: suma, resta, multiplicacion, division."""

    def suma(self, a, b):
        result = a + b
        logger.info(f"suma({a}, {b}) = {result}")
        return result

    def resta(self, a, b):
        result = a - b
        logger.info(f"resta({a}, {b}) = {result}")
        return result

    def multiplicacion(self, a, b):
        result = a * b
        logger.info(f"multiplicacion({a}, {b}) = {result}")
        return result

    def division(self, a, b):
        if b != 0:
            result = a / b
            logger.info(f"division({a}, {b}) = {result}")
            return result
        logger.error("Division by zero attempted")
        return "Division by zero is not allowed"


# ─────────────────────────────────────────
#  Trigonometric Operations
# ─────────────────────────────────────────
class TrigonometricCalculator:
    """Geometric transformations: sin, cos, tan and their inverses."""

    def seno(self, angulo_grados):
        result = math.sin(math.radians(angulo_grados))
        logger.info(f"seno({angulo_grados}°) = {result:.4f}")
        return result

    def coseno(self, angulo_grados):
        result = math.cos(math.radians(angulo_grados))
        logger.info(f"coseno({angulo_grados}°) = {result:.4f}")
        return result

    def tangente(self, angulo_grados):
        if angulo_grados % 180 == 90:
            return "Undefined (vertical asymptote)"
        result = math.tan(math.radians(angulo_grados))
        logger.info(f"tangente({angulo_grados}°) = {result:.4f}")
        return result

    def hipotenusa(self, cateto_a, cateto_b):
        result = math.sqrt(cateto_a ** 2 + cateto_b ** 2)
        logger.info(f"hipotenusa({cateto_a}, {cateto_b}) = {result}")
        return result

    def angulo_desde_seno(self, valor):
        if -1 <= valor <= 1:
            return math.degrees(math.asin(valor))
        return "Value out of range [-1, 1]"

    def angulo_desde_coseno(self, valor):
        if -1 <= valor <= 1:
            return math.degrees(math.acos(valor))
        return "Value out of range [-1, 1]"

    def angulo_desde_tangente(self, valor):
        return math.degrees(math.atan(valor))


# ─────────────────────────────────────────
#  Logarithmic Operations
# ─────────────────────────────────────────
class LogarithmicCalculator:
    """Logarithmic and exponential transformations."""

    def log_natural(self, x):
        if x > 0:
            result = math.log(x)
            logger.info(f"ln({x}) = {result:.4f}")
            return result
        return "Value must be greater than 0"

    def log_base10(self, x):
        if x > 0:
            result = math.log10(x)
            logger.info(f"log10({x}) = {result:.4f}")
            return result
        return "Value must be greater than 0"

    def log_base2(self, x):
        if x > 0:
            result = math.log2(x)
            logger.info(f"log2({x}) = {result:.4f}")
            return result
        return "Value must be greater than 0"

    def log_base_n(self, x, base):
        if x <= 0:
            return "Value must be greater than 0"
        if base <= 0 or base == 1:
            return "Base must be positive and not equal to 1"
        result = math.log(x) / math.log(base)
        logger.info(f"log_base_{base}({x}) = {result:.4f}")
        return result

    def exponencial(self, x):
        result = math.exp(x)
        logger.info(f"exp({x}) = {result:.4f}")
        return result

    def potencia_de_10(self, x):
        return 10 ** x

    def potencia_de_2(self, x):
        return 2 ** x


# ─────────────────────────────────────────
#  Main Calculator — inherits everything
# ─────────────────────────────────────────
class Calculator(BasicCalculator, TrigonometricCalculator, LogarithmicCalculator):
    """
    Unified calculator that exposes all operations:
      - Basic arithmetic  (suma, resta, multiplicacion, division)
      - Trigonometry      (seno, coseno, tangente, hipotenusa, ...)
      - Logarithms        (log_natural, log_base10, log_base2, log_base_n, ...)

    Usage:
        calc = Calculator()
        calc.suma(5, 10)
        calc.seno(45)
        calc.log_natural(100)
    """

    def info(self):
        print("=== Calculator App ===")
        print(f"Date : {datetime.datetime.now()}")
        print(f"Files: {os.listdir()}")


# ─────────────────────────────────────────
#  Demo
# ─────────────────────────────────────────
if __name__ == "__main__":
    calc = Calculator()
    calc.info()

    print("\n── Basic ──────────────────────")
    print(f"suma(5, 10)          = {calc.suma(5, 10)}")
    print(f"resta(10, 5)         = {calc.resta(10, 5)}")
    print(f"multiplicacion(5,10) = {calc.multiplicacion(5, 10)}")
    print(f"division(10, 5)      = {calc.division(10, 5)}")
    print(f"division(10, 0)      = {calc.division(10, 0)}")

    print("\n── Trigonometry ───────────────")
    for deg in [0, 30, 45, 60, 90]:
        s = round(calc.seno(deg), 4)
        c = round(calc.coseno(deg), 4)
        t = calc.tangente(deg)
        t_str = round(t, 4) if isinstance(t, float) else t
        print(f"  {deg:>3}°  sin={s:<8} cos={c:<8} tan={t_str}")
    print(f"hipotenusa(3, 4)     = {calc.hipotenusa(3, 4)}")

    print("\n── Logarithms ─────────────────")
    for v in [1, 2, 10, 100]:
        print(f"  ln({v:<4}) = {round(calc.log_natural(v), 4):<8}  "
              f"log10({v:<4}) = {round(calc.log_base10(v), 4):<8}  "
              f"log2({v:<4}) = {round(calc.log_base2(v), 4)}")
    print(f"log_base_5(125)      = {calc.log_base_n(125, 5):.4f}")
    print(f"exp(1)               = {calc.exponencial(1):.6f}")