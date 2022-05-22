"""Joke idea.  Virtual wall clock that uses the circle of fifths instead of ordinary numbers.
Command line arguments are as follows:
-r, --render:       determines whether the rendered image of the clock is 'analog' or 'digital'
"""


import argparse
import tkinter
from drawers import animation_loop


# TODO: Write readme
# TODO: "Digital" version


if __name__ == "__main__":
    # Parse arguments
    parser = argparse.ArgumentParser(description="Joke idea. Virtual wall clock that uses the circle of fifths instead of ordinary numbers")
    parser.add_argument("--render", "-r", action="store", type=str, required=False, default="analog", help="determines whether the rendered image of the clock is 'analog' or 'digital'", dest="render")
    args = parser.parse_args()
    render = args.render

    # Handle errors
    # render not "analog" or "digital"
    if render not in ["analog", "digital"]:
        raise ValueError("render must be 'analog' or 'digital'")

    # Begin a tkinter window with a canvas
    window = tkinter.Tk()
    window.title("Circle of fifths clock")
    window.geometry = "900x900"

    my_canvas = tkinter.Canvas(window, width=900, height=900, background="white")
    my_canvas.grid(row=0, column=0)

    # Repeatedly get the time and draw it
    my_canvas.after(1000, lambda: animation_loop(my_canvas, render))
    window.mainloop()
