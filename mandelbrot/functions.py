from mandelbrot.types import Z
from math import sqrt
from numpy import arange
from PIL import Image

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
            return (z_set, False)
    
    # If we get here, it didn't diverge with n iterations
    return (z_set, True)

def make_plot(precision: int,
              x_min: float,
              x_max: float,
              y_min: float,
              y_max: float,
              step_size: float) -> list[list[bool]]:
    buffer: list[bool] = []
    plot: list[list[bool]] = []

    # Set x to min to begin with, because we're counting up
    # Set y to max to begin, because in this case we're counting down (otherwise plot would be upside down)
    x = x_min
    y = y_max

    # Loop over X and Y, computing if mandelbrot with each step
    while y >= y_min:
        while x <= x_max:
            c = Z(
                real=x,
                imag=y
            )
            _, is_mandelbrot = in_mandelbrot_set(precision, c)
            buffer.append(is_mandelbrot)
            x += step_size
        plot.append(buffer)
        buffer = []
        x = x_min
        y -= step_size

    # Return the plot
    return plot

def plot_to_image(plt: list[list[bool]]) -> Image.Image:
    x_dim = len(plt[0])
    image = Image.new("RGB", (x_dim, len(plt)))

    x = 0
    y = 0

    for row in plt:
        if len(row) != x_dim:
            raise ValueError("Found row of different size than x_dim")
        
        for val in row:
            if val == True:
                image.putpixel((x, y), (0, 255, 0))
            else:
                image.putpixel((x, y), (0, 0, 255))
            x += 1
        y += 1
        x = 0
    
    return image

def animation_prec(max_precision: int,
                   x_min: float,
                   x_max: float,
                   y_min: float,
                   y_max: float,
                   step_size: float) -> None:
    frames: list[Image.Image] = []
    
    for p in range(max_precision):
        plot = make_plot(
            p,
            x_min,
            x_max,
            y_min,
            y_max,
            step_size
        )
        frame = plot_to_image(plot)
        frames.append(frame)
    
    first_frame = frames[0]
    first_frame.save("plot.gif", format="GIF", append_images=frames[1:], duration=100, loop=0)

            

if __name__ == "__main__":
    prec = 45
    x_min = -1.25
    x_max = -0.25
    y_min = -0.5
    y_max = 0.5
    step_size = 0.0025

    animation_prec(
        prec,
        x_min,
        x_max,
        y_min,
        y_max,
        step_size
    )
