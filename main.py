from mandelbrot.functions import animate_prec

MAX_PRECISION = 25
X_MIN = -2.5
X_MAX = 0.5
Y_MIN = -1.5
Y_MAX = 1.5
STEP_SIZE = 0.01

IMAGE_PATH = "plot.gif"

def main() -> None:
    animate_prec(
        MAX_PRECISION,
        X_MIN,
        X_MAX,
        Y_MIN,
        Y_MAX,
        STEP_SIZE,
        IMAGE_PATH
    )

if __name__ == "__main__":
    main()