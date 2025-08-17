from mandelbrot.types import Z

def step(z: Z, c: Z) -> Z:
    # We'll treat the real part of the constant as x and the imaginary part as y
    x = c.real
    y = c.imag

    # a_0 and b_0 are the real and imaginary parts of the constant respectively
    a_0 = z.real
    b_0 = z.imag

    # Evolve a and evolve b
    a_1 = a_0**2 - b_0**2 + x
    b_1 = 2*(a_0*b_0) + y

    # Return our complex number
    return Z(
        real=a_1,
        imag=b_1
    )

def iterate(n: int, c: Z) -> list[Z]:
    # z begins as 0
    z = Z(
        real=0,
        imag=0
    )

    # Evolve z with our constant c and save each step in a list
    z_set: list[Z] = []
    for _ in range(n):
        z_set.append(z)
        z = step(z, c)
    
    # Return the list
    return z_set

if __name__ == "__main__":
    n = 5
    c = Z(
        real=-1,
        imag=0
    )

    results = iterate(n, c)

    for r in results:
        print(r)