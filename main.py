# Mat Plot Lib import
import matplotlib.pyplot as plot

# My imports
from color_maps import color_maps
from fractals import julia_set, mandelbrot_set

DIRECTORY_PATH = "images/"

PIXELS_X = 2500
PIXELS_Y = 2500

JULIA_COLOR_MAP = "hot"
JULIA_COLOR_MAPS = [
    "hot",
    "twilight",
    "twilight_shifted",
    "ocean",
    "coolwarm",
    "seismic",
    "summer",
]
MANDELBROT_COLOR_MAP = "hot"
MANDELBROT_COLOR_MAPS = [
    "hot",
    "twilight",
    "twilight_shifted",
    "ocean",
    "coolwarm",
    "seismic",
    "spring",
    "summer",
    "autumn",
    "winter",
]


def render_image(data, path, color_map):
    plot.imshow(data, cmap=color_map)
    plot.axis("off")
    plot.savefig(DIRECTORY_PATH + path)


def render_julia_set(test_colors=False, use_all=False):
    c_x = -.4
    c_y = .62
    plot_data = julia_set(PIXELS_X, PIXELS_Y, c_x, c_y)
    if(test_colors):
        if not use_all:
            for color_map in JULIA_COLOR_MAPS:
                render_image(plot_data.T, "julia/" + color_map, color_map)
        else:
            for color_map_category in color_maps:
                for color_map in color_maps[color_map_category]:
                    render_image(plot_data.T, "julia/" + color_map_category + "_" + color_map, color_map)
    else:
        render_image(plot_data.T, "julia", JULIA_COLOR_MAP)


def render_mandelbrot_set(test_colors=False, use_all=False):
    plot_data = mandelbrot_set(PIXELS_X, PIXELS_Y)
    if test_colors:
        if not use_all:
            for color_map in MANDELBROT_COLOR_MAPS:
                render_image(plot_data.T, "mandelbrot/" + color_map, color_map)
        else:
            for color_map_category in color_maps:
                for color_map in color_maps[color_map_category]:
                    render_image(plot_data.T, "mandelbrot/" + color_map_category + "_" + color_map, color_map)
    else:
        render_image(plot_data.T, "mandelbrot", MANDELBROT_COLOR_MAP)


if __name__ == "__main__":
    render_mandelbrot_set(True)