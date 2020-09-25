# Num Py import
import numpy as np


JULIA_DEFAULT_ITERATIONS = 150
JULIA_MAX = 2
JULIA_MIN = -2


MANDELBROT_DEFAULT_ITERATIONS = 150
MANDELBROT_X_MAX = 1
MANDELBROT_X_MIN = -2
MANDELBROT_Y_MAX = 1
MANDELBROT_Y_MIN = -2


def mandelbrot_iteration(z_init, c, iterations, limit=4):
    z = z_init
    count = 0
    for i in range(iterations):
        z = (z * z) + c
        count += 1
        if(abs(z) > limit):
            break
    return count


def mandelbrot_set(num_rows, num_columns, iterations=MANDELBROT_DEFAULT_ITERATIONS):
    x_space = np.linspace(MANDELBROT_X_MIN, MANDELBROT_X_MAX, num_rows)
    y_space = np.linspace(MANDELBROT_Y_MIN, MANDELBROT_Y_MAX, num_columns)
    x_len = len(x_space)
    y_len = len(y_space)
    result = np.zeros((x_len, y_len))
    for i in range(x_len):
        for j in range(y_len):
            c = complex(x_space[i], y_space[j])
            z = complex(0, 0)
            result[i, j] = mandelbrot_iteration(z, c, iterations)
    return result


def julia_set(num_rows, num_columns, cx, cy, iterations=JULIA_DEFAULT_ITERATIONS):
    c = complex(cx, cy)
    x_space = np.linspace(JULIA_MIN, JULIA_MAX, num_rows)
    y_space = np.linspace(JULIA_MIN, JULIA_MAX, num_columns)
    x_len = len(x_space)
    y_len = len(y_space)
    result = np.zeros((x_len, y_len))
    for i in range(x_len):
        for j in range(y_len):
            z = complex(x_space[i], y_space[j])
            result[i, j] = mandelbrot_iteration(z, c, iterations)
    return result