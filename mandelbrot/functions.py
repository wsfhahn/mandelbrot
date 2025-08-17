from mandelbrot.types import Z
from math import sqrt

def step(z: Z, c: Z) -> Z:
    # We'll treat the real part of the constant as x and the imaginary part as y
    x = c.real
    y = c.imag

    # a_0 and b_0 are the real and imaginary parts of the constant respectively
    a_0 = z.real
    b_0 = z.imag

    # Evolve a and evolve b
    try:
        a_1 = a_0**2 - b_0**2 + x
        b_1 = 2*(a_0*b_0) + y
    # If the number grows too large, just return the input
    except OverflowError:
        return Z(
            real=a_0,
            imag=b_0
        )

    # Return our complex number
    return Z(
        real=a_1,
        imag=b_1
    )

def get_magnitude(z: Z) -> float:
    a = z.real
    b = z.imag

    # Because a complex number exists on a 2D plane, we can get the magnitude using pythag theorem
    mag = sqrt(a**2 + b**2)
    return mag

def in_mandelbrot_set(n: int, c: Z) -> tuple[list[Z], bool]:
    # Start with z at 0, per the definition
    z = Z(
        real=0,
        imag=0
    )

    # List to store results
    z_set: list[Z] = []

    # Iterate n times, evolving real and imaginary part with each step
    for _ in range(n):
        z_set.append(z)
        z = step(z, c)

        # If the magnitude is greater than 2, we know we've diverged
        if abs(get_magnitude(z)) >= 2:
            print("Diverging, not in set!")
            return (z_set, False)
    
    # If we get here, it didn't diverge with n iterations
    print("Did not diverge, in set!")
    return (z_set, True)

if __name__ == "__main__":
    n = 50
    c = Z(
        real=-1,
        imag=0
    )

    z_set, is_mandelbrot = in_mandelbrot_set(n, c)

    print(is_mandelbrot)