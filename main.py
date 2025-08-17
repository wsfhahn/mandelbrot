from dataclasses import dataclass

def apply_polynomial_map(c: float, n: int) -> float:
    z: float = 0
    for _ in range(n):
        z = z**2 + c
        print(z)
    return z

if __name__ == "__main__":
    c = -1
    n = 5
    apply_polynomial_map(c, n)