from datetime import datetime
from math import pi, sin, cos, floor, ceil


def animation_loop(canvas_, render_in: str) -> None:
    """Repeatedly update the canvas with a circle-of-fifths clock.
    :param canvas_:       the tkinter canvas object
    :param render_in:       either "analog" or "digital", to indicate the type of clock that should be drawn
    """
    # Handle errors
    # render_in not a string
    if not isinstance(render_in, str):
        raise TypeError("render_in must be a string")
    # render_in not "analog" or "digital"
    if render_in not in ["analog", "digital"]:
        raise ValueError("render_in must be 'analog' or 'digital'")

    # Dictionary that converts from render_in value to the appropriate render function to use
    render_in_to_render_function = {
        "analog": render_analog,
        "digital": render_digital
    }

    # Run
    while True:
        # Get the current time
        current = datetime.now()
        hour, minute, second = current.hour, current.minute, current.second

        # Update the canvas using the appropriate function for render method
        render_in_to_render_function[render_in](canvas_, hour, minute, second)


def render_analog(canvas_in, hour_in: int, minute_in: int, second_in: int):
    """Draw an animated clock in 'analog' style
    """
    # Handle errors
    # hour_in not an int
    if not isinstance(hour_in, int):
        raise TypeError("hour_in must be an int")
    # minute_in not an int
    if not isinstance(minute_in, int):
        raise TypeError("minute_in must be an int")
    # second_in not an int
    if not isinstance(second_in, int):
        raise TypeError("second_in must be an int")
    # hour_in not a value from 0 through 23
    if not 0 <= hour_in <= 23:
        raise ValueError("hour_in must be somewhere from 0 through 23")
    # minute_in not a value from 0 through 59
    if not 0 <= minute_in <= 59:
        raise ValueError("minute_in must be somewhere from 0 through 59")
    # second_in not a value from 0 through 59
    if not 0 <= second_in <= 59:
        raise ValueError("second_in must be somewhere from 0 through 59")

    # Basic spatial constants
    guide_offset = 425  # Pixels
    guide_length = 450  # Pixels
    hour_hand_length = 200  # Pixels
    minute_hand_length = 400  # Pixels
    second_hand_length = 400  # Pixels

    # Conversions from angle ii to sharps/flats
    angle_ii_to_sharps_flats = ["3#", "2#", "1#", "", "1b", "2b", "3b", "4b", "5b", "6#", "5#", "4#"]

    # Conversions from angle ii to major
    angle_ii_to_major = ["A", "D", "G", "C", "F", "Bb", "Eb", "Ab", "Db", "F#", "B", "E"]

    # Conversions from angle ii to minor
    angle_ii_to_minor = ["F#", "B", "E", "A", "D", "G", "C", "F", "Bb", "Eb", "G#", "C#"]

    # Conversions from angle ii to roman numeral
    angle_ii_to_roman_numeral = ["vi", "ii", "V", "I", "IV", "", "", "", "", "", "vii", "iii"]

    # Wipe the canvas
    canvas_in.delete("all")

    # Draw the circle of the clock
    canvas_in.create_oval(0, 0, 900, 900, outline="black")

    # Draw hour guides
    for ii in range(12):
        angle = ii / 12 * 2 * pi
        canvas_in.create_line(450 + guide_offset * cos(angle), 450 - guide_offset * sin(angle), 450 + guide_length * cos(angle), 450 - guide_length * sin(angle), fill="gray")

    # Draw sharps/flats markings
    for ii in range(12):
        angle = ii / 12 * 2 * pi
        canvas_in.create_text(450 + 400 * cos(angle), 450 - 400 * sin(angle), text=angle_ii_to_sharps_flats[ii], font=("Helvetica", 18), fill="gray")

    # Draw major markings
    for ii in range(12):
        angle = ii / 12 * 2 * pi
        canvas_in.create_text(450 + 350 * cos(angle), 450 - 350 * sin(angle), text=angle_ii_to_major[ii], font=("Helvetica", 36), fill="black")

    # Draw minor markings
    for ii in range(12):
        angle = ii / 12 * 2 * pi
        canvas_in.create_text(450 + 250 * cos(angle), 450 - 250 * sin(angle), text=angle_ii_to_minor[ii], font=("Helvetica", 24), fill="gray")

    # Draw roman numerals
    for ii in range(12):
        angle = ii / 12 * 2 * pi
        canvas_in.create_text(450 + 150 * cos(angle), 450 - 150 * sin(angle), text=angle_ii_to_roman_numeral[ii], font=("Helvetica", 18), fill="blue")

    # Draw the hour hand
    hour_angle = pi / 2 - (hour_in / 12 * 2 * pi) - (minute_in / 60 / 12 * 2 * pi)
    canvas_in.create_line(450, 450, 450 + hour_hand_length * cos(hour_angle), 450 - hour_hand_length * sin(hour_angle), fill="black")

    # Draw the minute hand
    minute_angle = pi / 2 - (minute_in / 60 * 2 * pi)
    canvas_in.create_line(450, 450, 450 + minute_hand_length * cos(minute_angle), 450 - minute_hand_length * sin(minute_angle), fill="black")

    # Draw the second hand
    second_angle = pi / 2 - (second_in / 60 * 2 * pi)
    canvas_in.create_line(450, 450, 450 + second_hand_length * cos(second_angle), 450 - second_hand_length * sin(second_angle), fill="red")

    # Update the canvas
    canvas_in.update()


def render_digital(canvas_in, hour_in: int, minute_in: int, second_in: int):
    """Draw an animated clock in 'digital' style.
    """
    # Handle errors
    # hour_in not an int
    if not isinstance(hour_in, int):
        raise TypeError("hour_in must be an int")
    # minute_in not an int
    if not isinstance(minute_in, int):
        raise TypeError("minute_in must be an int")
    # second_in not an int
    if not isinstance(second_in, int):
        raise TypeError("second_in must be an int")
    # hour_in not a value from 0 through 23
    if not 0 <= hour_in <= 23:
        raise ValueError("hour_in must be somewhere from 0 through 23")
    # minute_in not a value from 0 through 59
    if not 0 <= minute_in <= 59:
        raise ValueError("minute_in must be somewhere from 0 through 59")
    # second_in not a value from 0 through 59
    if not 0 <= second_in <= 59:
        raise ValueError("second_in must be somewhere from 0 through 59")

    # Wipe the canvas
    canvas_in.delete("all")

    # Basic spatial constants
    outer_box_margin_horizontal = 50    # Pixels
    outer_box_margin_vertical = 250     # Pixels

    # Conversions from hour to major
    hour_to_major = ["C", "G", "D", "A", "E", "B", "F#", "Db", "Ab", "Eb", "Bb", "F"] * 2

    # Conversions from minute/5 to minor
    minute_over_five_to_minor = ["A", "E", "B", "F#", "C#", "G#", "Eb", "Bb", "F", "C", "G", "D"]

    # Draw outer black box
    canvas_in.create_rectangle(0 + outer_box_margin_horizontal, 0 + outer_box_margin_vertical, 900 - outer_box_margin_horizontal, 900 - outer_box_margin_vertical, outline="black")

    # Draw colon
    canvas_in.create_text(450, 450, text=":", font=("Helvetica", 128), fill="black")

    # Draw major symbol
    canvas_in.create_text((outer_box_margin_horizontal + 450) / 2, 450, text=hour_to_major[hour_in], font=("Helvetica", 128), fill="black")

    # Draw superposition of two minor symbols
    # Determine symbols to draw, and the opacities at which to draw them
    round_0 = floor(minute_in / 5)  # The minute that's a multiple of 5 that's closest to our number, and not greater than it -- divided by 5
    round_1 = ceil(minute_in / 5)   # The minute that's a multiple of 5 that's closest to our number, and not less than it -- divided by 5
    opacity_0 = abs(minute_in - round_0)
    if round_0 == round_1:
        opacity_1 = 0
    else:
        opacity_1 = abs(minute_in - round_1)
    symbol_0, symbol_1 = minute_over_five_to_minor[round_0], minute_over_five_to_minor[round_1]
    # Draw them
    canvas_in.create_text((900 - outer_box_margin_horizontal - 450) / 2, 450, text=symbol_0, font=("Helvetica", 128), fill="black", alpha=opacity_0)
    canvas_in.create_text((900 - outer_box_margin_horizontal - 450) / 2, 450, text=symbol_1, font=("Helvetica", 128), fill="black", alpha=opacity_1)

    # Update the canvas
    canvas_in.update()
