# Mandelbrot

<img src="assets/plot.gif" width="250"/>

## What does this project do?

This project creates an animated GIF of the Mandelbrot plot with increasing precision in each frame.

## How do I use it?

This project is built with `uv`. To create a virtual environment and install the necessary packages, run:

```zsh
uv sync
```

Inside `main.py`, there are a few variables to set:

1. `MAX_PRECISION`: Precision of the plot in the last frame of the GIF
2. `X_MIN` Minimum X value (minimum value of the real component)
3. `X_MAX` Maximum X value (maximum value of the real component)
4. `Y_MIN`: Minimum Y value (minimum value of the complex component)
5. `Y_MAX`: Maximum Y value (maximum valeu of the complex component)
6. `STEP_SIZE`: Controls the resolution of the plot
7. `IMAGE_PATH`: Path to save the animated plot to.

Once these variables are set, it's ready to rip. Run the main loop with the following command:

```zsh
uv run main.py
```

## Is this entirely human written?

Yes, this project is entirely human-written. It is a zero-AI weekend project.