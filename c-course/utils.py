from manim import *


def labelled_block(label: str, height: int, width: int, font_size=24, rotate=0) -> VGroup:

    rect = Rectangle(height=height, width=width).rotate(rotate)

    label_text = Text(label, font_size=font_size)

    label_text.shift(rect.get_center())

    vg = VGroup()
    vg.add(rect, label_text)

    return vg

def remove_dot_objs(vg: VGroup):

    new_vg = VGroup()

    for v in vg:

        if isinstance(v, Dot):
            continue

        new_vg.add(v)

    return new_vg


def elbow_arrow(start, end, width=1):

    steps = end - start

    first_bend = start + (steps[0] + width) * RIGHT
    second_bend = first_bend + steps[1] * UP

    grp = VGroup()
    grp.add(Line(start, first_bend))

    if (second_bend != end).any():
        grp.add(Line(first_bend, second_bend), Arrow(second_bend, end, buff=0))
    else:
        grp.add(Arrow(first_bend, second_bend, buff=0))



    return grp

def clear_scene(scene: Scene):
    
    scene.remove(*scene.mobjects)    


