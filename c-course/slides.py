from manim import (
    Scene,
    Code,
    Text,
    SurroundingRectangle,
    Transform,
    Create,
    Write,
    Arrow,
    Rectangle,
    VGroup,
    MathTex,
    UP,
    DOWN,
    LEFT,
    RIGHT,
    PI,
    GREEN,
)
from manim_editor import PresentationSectionType
from utils import remove_dot_objs, labelled_block, elbow_arrow, clear_scene
from math import sqrt


def hello_world_scene(scene: Scene):
    label = Text("C")
    scene.play(Create(label))

    scene.next_section(PresentationSectionType.NORMAL)
    codeblock = Code("examples/boilerplate.c", style="default")
    scene.play(Create(codeblock))
    scene.pause(1)
    scene.next_section(PresentationSectionType.NORMAL)

    r1 = SurroundingRectangle(remove_dot_objs(codeblock.code[3]), color=GREEN)
    r2 = SurroundingRectangle(remove_dot_objs(codeblock.code[7]), color=GREEN)

    scene.play(Create(r1), Create(r2))

    scene.next_section(PresentationSectionType.NORMAL)

    codeblock_2 = Code("examples/hello_world.c", style="default")
    scene.remove(r1, r2)
    scene.play(Transform(codeblock, codeblock_2))

    line = remove_dot_objs(codeblock_2.code[5])
    scene.next_section(PresentationSectionType.NORMAL)
    quote_rect = SurroundingRectangle(line[7], color=GREEN)
    endquote_rect = SurroundingRectangle(line[19], color=GREEN)
    semicolon_rect = SurroundingRectangle(line[21], color=GREEN)
    scene.next_section(PresentationSectionType.NORMAL)
    scene.play(Create(quote_rect), Create(endquote_rect))
    scene.next_section(PresentationSectionType.NORMAL)
    scene.play(Create(semicolon_rect))


def compiler_scene(scene: Scene):
    scene.next_section(type=PresentationSectionType.NORMAL)

    source_file = labelled_block("Source .c \nFile", height=2, width=2).shift(LEFT * 5)
    compiler_block = labelled_block("Compiler", height=1, width=2).shift(LEFT * 2)
    object_file = labelled_block("Object File \n*.o", height=2, width=2).shift(RIGHT)
    linker = labelled_block("Linker", height=1, width=2).shift(RIGHT * 4)
    arr2 = Arrow(start=compiler_block.get_right(), end=object_file.get_left(), buff=0)
    arr3 = Arrow(start=object_file.get_right(), end=linker.get_left(), buff=0)
    executable_file = Text("a.out", font_size=24).shift(RIGHT * 6)
    arr4 = Arrow(start=linker.get_right(), end=executable_file.get_left(), buff=0.1)
    gcc_grp = VGroup()
    gcc_grp.add(compiler_block, object_file, linker, arr2, arr3)
    arr1 = Arrow(start=source_file.get_right(), end=gcc_grp.get_left(), buff=0)
    gcc_block = VGroup(SurroundingRectangle(gcc_grp))
    gcc_block.add(Text("GCC").shift(gcc_block.get_center()))

    scene.next_section(type=PresentationSectionType.NORMAL)

    scene.play(Create(source_file))
    scene.play(Create(gcc_block), Create(arr1), Create(arr4), Create(executable_file))
    
    scene.next_section(type=PresentationSectionType.NORMAL)

    scene.play(Transform(gcc_block, gcc_grp))

    


def variable_scene(scene: Scene):

    codeblock = Code("examples/variable.c", style="default")

    codeblock.code = list(map(remove_dot_objs, codeblock.code))

    scene.add(codeblock)

    var_type = SurroundingRectangle(codeblock.code[5][0:3], color=GREEN)
    var_name = SurroundingRectangle(codeblock.code[5][3:6], color=GREEN)
    assign_symbol = SurroundingRectangle(codeblock.code[5][6:7], color=GREEN)
    value = SurroundingRectangle(codeblock.code[5][7:9], color=GREEN)
    semicolon = SurroundingRectangle(codeblock.code[5][9:10], color=GREEN)
    
    scene.play(Create(var_type))
    scene.remove(var_type)
    scene.play(Create(var_name))
    scene.remove(var_name)
    scene.play(Create(assign_symbol))
    scene.remove(assign_symbol)
    scene.play(Create(value))
    scene.remove(value)
    scene.play(Create(semicolon))

    pass


def conditionals_scene(scene: Scene):

    entry_block = labelled_block("Entry", 1, 2.5).shift(UP * 3)
    condition_block = labelled_block(
        "If Condition", sqrt(2), sqrt(2), rotate=PI / 4
    ).shift(UP)

    condition_arrow = Arrow(
        start=entry_block.get_bottom(), end=condition_block.get_top(), buff=0
    )

    if_body = labelled_block("If Body", 1, 2).shift(LEFT * 2 + DOWN)

    else_body = labelled_block("Else Body", 1, 2).shift(RIGHT * 2 + DOWN)

    exit_block = labelled_block("Exit", 1, 2).shift(DOWN * 3)

    if_body_arrow = elbow_arrow(
        start=condition_block.get_left(), end=if_body.get_top(), width=0
    )

    else_body_arrow = elbow_arrow(
        start=condition_block.get_right(), end=else_body.get_top(), width=0
    )

    if_exit_arrow = elbow_arrow(
        start=if_body.get_bottom(), end=exit_block.get_left(), width=-1
    )

    else_exit_arrow = elbow_arrow(
        start=else_body.get_bottom(), end=exit_block.get_right()
    )

    true_label = Text("True", font_size=24).shift(if_body_arrow.get_left() + 0.5 * LEFT)
    false_label = Text("False", font_size=24).shift(
        else_body_arrow.get_right() + 0.5 * RIGHT
    )

    fallthrough_arrow = elbow_arrow(condition_block.get_right(), exit_block.get_right())

    else_block_group = VGroup(else_body, else_body_arrow, else_exit_arrow)

    scene.play(Create(entry_block))
    scene.play(Create(condition_arrow))
    scene.play(Create(condition_block))
    scene.play(Create(if_body))
    scene.play(Create(if_body_arrow))
    scene.play(Create(true_label))
    scene.play(Create(exit_block))
    scene.play(Create(if_exit_arrow))
    scene.play(Create(fallthrough_arrow))
    scene.play(Create(false_label))
    scene.pause(2)
    scene.play(Transform(fallthrough_arrow, else_block_group))
    scene.pause(2)
    pass


def if_else_if_scene(scene: Scene):
    c1 = labelled_block("Condition 1", 2, 2, rotate=PI / 4).shift(LEFT * 4 + UP * 2)
    c2 = labelled_block("Condition 2", 2, 2, rotate=PI / 4).shift(UP * 2)
    c3 = labelled_block("Condition 3", 2, 2, rotate=PI / 4).shift(RIGHT * 4 + UP * 2)

    c1_c2 = Arrow(start=c1.get_right(), end=c2.get_left(), buff=0)
    c2_c3 = Arrow(start=c2.get_right(), end=c3.get_left(), buff=0)

    c1_body = labelled_block("Body", 1, 2).shift(LEFT * 4 + DOWN)
    c2_body = labelled_block("Body", 1, 2).shift(DOWN)
    c3_body = labelled_block("Body", 1, 2).shift(RIGHT * 4 + DOWN)

    c1_body_arrow = Arrow(start=c1.get_bottom(), end=c1_body.get_top(), buff=0)
    c2_body_arrow = Arrow(start=c2.get_bottom(), end=c2_body.get_top(), buff=0)
    c3_body_arrow = Arrow(start=c3.get_bottom(), end=c3_body.get_top(), buff=0)

    exit_blk = labelled_block("Exit", 1, 2).shift(DOWN * 3)

    c1_exit = elbow_arrow(c1_body.get_bottom(), exit_blk.get_left(), width=-3)
    c2_exit = Arrow(c2_body.get_bottom(), exit_blk.get_top(), buff=0)
    c3_exit = elbow_arrow(c3_body.get_bottom(), exit_blk.get_right(), width=3)

    s1 = VGroup(
        c1,
        c2,
        c3,
        c1_c2,
        c2_c3,
        c1_body,
        c2_body,
        c3_body,
        c1_body_arrow,
        c2_body_arrow,
        c3_body_arrow,
        exit_blk,
        c1_exit,
        c2_exit,
        c3_exit,
    )

    scene.play(Create(s1, run_time=2))

    scene.pause(1)

    scene.play(s1.animate.scale(0.75).shift(LEFT * 2))

    cn = (
        labelled_block("Condition N", 2, 2, rotate=PI / 4)
        .scale(0.75)
        .shift(c3.get_right() + RIGHT * 2.5)
    )

    cn_body = (
        labelled_block("Body", 1, 2).shift(cn.get_bottom() + DOWN * 1.23).scale(0.75)
    )

    cn_body_arrow = Arrow(start=cn.get_bottom(), end=cn_body.get_top(), buff=0)
    cn_exit = elbow_arrow(start=cn_body.get_bottom(), end=exit_blk.get_right(), width=6)
    ellipsis = Text(". . .").shift(cn.get_left() + LEFT * 0.75)

    scene.play(
        Create(cn),
        Create(cn_body),
        Create(cn_body_arrow),
        Create(cn_exit),
        Create(ellipsis),
    )

    scene.pause(2)


def for_loop_scene(scene: Scene):
    def chart_block(text: str) -> VGroup:
        blk = Rectangle(height=1, width=2)
        txt = Text(text).scale(0.5)
        txt.move_to(blk.get_center())

        grp = VGroup()
        grp.add(blk, txt)

        return grp

    def condition_block(text: str) -> VGroup:
        blk = Rectangle(height=sqrt(2) + 0.2, width=sqrt(2) + 0.2).rotate(PI / 4)
        txt = Text(text).scale(0.4)
        txt.move_to(blk.get_center())

        grp = VGroup()
        grp.add(blk, txt)

        return grp

    initializer = chart_block("Initializer").shift(UP * 3)
    condition = condition_block("Loop Condition")
    body = chart_block("Loop Body").shift(LEFT * 4)
    update = chart_block("Update").shift(LEFT * 4 + DOWN * 2)
    exit_blk = chart_block("Exit").shift(DOWN * 3.5)

    arrows = [
        Arrow(start=initializer.get_bottom(), end=condition.get_top(), buff=0),
        t := Arrow(start=condition.get_left(), end=body.get_right(), buff=0),
        Text("True").move_to(t.get_top() + UP * 0.3).scale(0.5),
        f := elbow_arrow(condition.get_right(), exit_blk.get_right()),
        Text("False").move_to(f.get_right() + RIGHT * 0.5).scale(0.5),
        Arrow(start=body.get_bottom(), end=update.get_top(), buff=0),
        elbow_arrow(update.get_right(), condition.get_bottom(), width=0),
    ]

    scene.next_section(type=PresentationSectionType.NORMAL)
    scene.play(Create(initializer))

    scene.next_section(type=PresentationSectionType.NORMAL)
    scene.play(Create(condition))

    scene.next_section(type=PresentationSectionType.NORMAL)
    scene.play(Create(update))

    scene.next_section(type=PresentationSectionType.NORMAL)
    scene.play(Create(body))

    scene.next_section(type=PresentationSectionType.NORMAL)
    scene.play(Create(exit_blk))

    for p in arrows:
        scene.next_section(type=PresentationSectionType.NORMAL)
        scene.play(Create(p))


def while_loop_scene(scene: Scene):
    entry_block = labelled_block("Loop Entry", 1, 2).shift(UP * 3)

    condition_block = labelled_block("Loop Condition", 2, 2, rotate=PI / 4)
    body_block = labelled_block("Body", 1, 2).shift(DOWN * 3)

    entry_arrow = Arrow(
        start=entry_block.get_bottom(), end=condition_block.get_top(), buff=0
    )

    true_arrow = Arrow(
        start=condition_block.get_bottom(), end=body_block.get_top(), buff=0
    )

    loop_arrow = elbow_arrow(body_block.get_left(), condition_block.get_left(), -1)

    exit_block = labelled_block("Loop Exit", 1, 2).shift(RIGHT * 4)

    exit_arrow = Arrow(
        start=condition_block.get_right(), end=exit_block.get_left(), buff=0
    )

    true_label = Text("True", font_size=24).shift(true_arrow.get_right() + RIGHT * 0.4)
    false_label = Text("False", font_size=24).shift(exit_arrow.get_top() + UP * 0.2)

    scene.play(Create(entry_block))
    scene.play(Create(condition_block))
    scene.play(Create(body_block))
    scene.play(Create(exit_block))

    scene.play(Create(entry_arrow))
    scene.play(Create(true_arrow), Create(true_label))
    scene.play(Create(loop_arrow))
    scene.play(Create(exit_arrow), Create(false_label))

    scene.add(
        condition_block,
        body_block,
        true_arrow,
        loop_arrow,
        exit_block,
        exit_arrow,
        true_label,
        false_label,
        entry_block,
        entry_arrow,
    )

    scene.pause(2)


def do_while_loop_scene(scene: Scene):
    entry_block = labelled_block("Loop Entry", 1, 2).shift(UP * 3)

    condition_block = labelled_block("Loop Condition", 2, 2, rotate=PI / 4).shift(
        DOWN * 2
    )
    body_block = labelled_block("Body", 1, 2).shift(UP)

    entry_arrow = Arrow(
        start=entry_block.get_bottom(), end=body_block.get_top(), buff=0
    )

    condition_arrow = Arrow(
        start=body_block.get_bottom(), end=condition_block.get_top(), buff=0
    )
    loop_arrow = elbow_arrow(condition_block.get_left(), body_block.get_left(), -1)

    exit_block = labelled_block("Loop Exit", 1, 2).shift(RIGHT * 4 + DOWN * 2)

    exit_arrow = Arrow(
        start=condition_block.get_right(), end=exit_block.get_left(), buff=0
    )

    true_label = Text("True", font_size=24).shift(loop_arrow.get_left() + LEFT * 0.4)
    false_label = Text("False", font_size=24).shift(exit_arrow.get_top() + UP * 0.2)

    scene.play(Create(entry_block))
    scene.play(Create(body_block))
    scene.play(Create(condition_block))
    scene.play(Create(exit_block))

    scene.play(Create(entry_arrow))
    scene.play(Create(condition_arrow))
    scene.play(Create(loop_arrow), Create(true_label))
    scene.play(Create(exit_arrow), Create(false_label))

    scene.pause(2)


def base16_scene(scene: Scene):
    base10_symbols = Text("Base 10: 0-9").shift(UP)
    base16_symbols = Text("Base 16: 0-9, A-F")

    b10_number = Text("1269").shift(UP)
    b16_number = Text("4F5")

    scene.add(base16_symbols, base10_symbols)

    scene.play(Transform(base10_symbols, b10_number))
    scene.pause(1)
    scene.play(Transform(base16_symbols, b16_number))
    scene.pause(1)

    b16_expanded = MathTex("4 \cdot 16^2 + F \cdot 16^1 + 5 \cdot 16^0 = 1269").shift(
        DOWN
    )
    scene.play(Write(b16_expanded))
    scene.pause(1)


def memory_model_scene(scene: Scene):

    def variable_block(name: str, height: int, font_size=24):

        blk = Rectangle(height=height, width=2)
        label = Text(name, font_size=font_size).shift(blk.get_center())
        vg = VGroup()
        vg.add(blk, label)

        return vg

    mem = Rectangle(height=7, width=2).shift(RIGHT * 5)

    code_block = Code("examples/memory_model.c", line_spacing=1)
    code_block.shift(LEFT * 3)

    x_highlight = SurroundingRectangle(remove_dot_objs(code_block.code[2]))
    y_highlight = SurroundingRectangle(remove_dot_objs(code_block.code[4]))

    v1 = variable_block("age", 1).shift(UP * 3 + RIGHT * 2)

    v2 = variable_block("temperature", 1.5)
    v2.shift(v1.get_bottom() + v2.height / 2 * DOWN)

    scene.add(mem, code_block)
    scene.next_section(type=PresentationSectionType.NORMAL)
    scene.play(Create(x_highlight))
    scene.play(Create(v1))
    scene.play(v1.animate.shift(RIGHT * 3))
    scene.next_section(type=PresentationSectionType.NORMAL)

    scene.play(Transform(x_highlight, y_highlight))
    scene.play(Create(v2))
    scene.play(v2.animate.shift(RIGHT * 3))
    scene.next_section(type=PresentationSectionType.NORMAL)

    low_addr = Text("0x0000", font_size=24)
    low_addr.shift(mem.get_bottom() + LEFT * (mem.width / 2 + low_addr.width / 2 + 0.2))

    high_addr = Text("0x...", font_size=24)
    high_addr.shift(mem.get_top() + LEFT * (mem.width / 2 + high_addr.width / 2 + 0.2))
    scene.next_section(type=PresentationSectionType.NORMAL)

    scene.play(Create(low_addr), Create(high_addr))


SCENES = [
    hello_world_scene,
    compiler_scene,
    variable_scene,
    conditionals_scene,
    if_else_if_scene,
    for_loop_scene,
    while_loop_scene,
    do_while_loop_scene,
    base16_scene,
    memory_model_scene,
]


class Slides(Scene):

    def construct(self):
        for scene in SCENES:
            scene(self)
            self.next_section(type=PresentationSectionType.NORMAL)
            clear_scene(self)
            self.next_section(type=PresentationSectionType.NORMAL)

