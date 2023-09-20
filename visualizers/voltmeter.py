from vpython import *
import math
import numpy as np


def create_scene() -> canvas:
    return canvas(
        width=400,
        height=400,
        center=vector(0, 0, 0),
        background=color.white
    )


def create_outline() -> box:
    return box(
        pos=vector(0, 0, 0),
        size=vector(2.5, 2.5, 0.1),
        color=color.black
    )


def create_cypher() -> cylinder:
    return cylinder(
        pos=vector(0, 0, 0),
        radius=1,
        color=color.white,
        axis=vector(0, 0, 1),
        length=0.055,
    )


def create_ticks(
        volt: int,
        tick_end: float,
        tick_start: float,
        tick_radius: float,
        tick_origin: vector,
        tick_length: float,
        x: float,
        y: float
) -> None:
    for increment in np.linspace(tick_end, tick_start, 25):
        if volt % 5 == 0:
            radius = tick_radius * 2
        else:
            radius = tick_radius
        ticks = cylinder(
            pos=tick_origin,
            radius=radius,
            color=color.black,
            axis=vector(1, 0, 0),
            length=tick_length,
        )
        ticks.rotate(increment, axis=vector(0, 0, 1), origin=vector(0, y, x))
        ticks.length = tick_length
        volt = volt + 1


def create_text(
        tick_arc_radius: float,
        tick_length: float,
        tick_start: float,
        tick_end: float,
        y: float
) -> (float, float):
    text_radius = tick_arc_radius * 1.1
    text_color = color.black
    text_height = 2 * tick_length
    text_depth = 0.06
    text_angle_increment = -(tick_start - tick_end) / 5
    for number in range(0, 6, 1):
        text_angle = tick_start + text_angle_increment * number
        text_position = vector(
            text_radius * np.cos(text_angle), text_radius * np.sin(text_angle) + y, 0.06
        )
        text(
            text=str(number),
            pos=text_position,
            color=text_color,
            height=text_height,
            align="center",
            depth=text_depth,
        )
    return text_height, text_depth


def visualize_data() -> (arrow, float, float):
    scene = create_scene()
    outline = create_outline()
    cypher = create_cypher()

    tick_start = 3 * math.pi / 4
    tick_end = math.pi / 4
    tick_radius = 0.005
    tick_arc_radius = 1
    tick_length = 0.05
    x = tick_arc_radius
    y = -0.4
    z = 0.06
    tick_origin = vector(x, y, z)
    volt = 0

    create_ticks(volt, tick_end, tick_start, tick_radius, tick_origin, tick_length, x, y)

    text_height, text_depth = create_text(tick_arc_radius, tick_length, tick_start, tick_end, y)

    text(
        text="Voltmeter",
        pos=vector(0, -0.6, 0.06),
        color=color.black,
        height=2 * text_height,
        align="center",
        depth=text_depth,
    )

    needle = arrow(
        pos=vector(0, -0.4, 0.08),
        round=True,
        shaftwidth=0.02,
        axis=vector(0.9, 0, 0.08),
        color=color.red,
        opacity=1,
        headlength=0.08,
        headwidth=0.06,
    )

    needle.rotate(tick_start, axis=vector(0, 0, 1), origin=vector(0, -0.4, 0.08))

    needle_angle = tick_start
    needle_range = tick_start - tick_end

    return needle, needle_range
