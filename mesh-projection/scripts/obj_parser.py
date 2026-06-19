import pyparsing.common as ppc
import pyparsing as pp
from pyparsing import Literal, Optional, OneOrMore, LineEnd, SkipTo, Suppress


def build_obj_parser():
    
    vertex_coordinate = (
        Suppress(Literal("v"))
        + pp.common.fnumber
        + pp.common.fnumber
        + pp.common.fnumber
        + Optional(pp.common.fnumber)
    ).set_parse_action(lambda r: ("v", *r))

    texture_coordinate = (
        Suppress(Literal("vt"))
        + pp.common.fnumber
        + Optional(pp.common.fnumber)
        + Optional(pp.common.fnumber)
    ).set_parse_action(lambda r: ("vt", *r))

    vertex_normal = (
        Suppress(Literal("vn"))
        + pp.common.fnumber
        + pp.common.fnumber
        + pp.common.fnumber
    ).set_parse_action(lambda r: ("vn", *r))

    vertex_parameter = (
        Suppress(Literal("vp"))
        + pp.common.fnumber
        + Optional(pp.common.fnumber)
        + Optional(pp.common.fnumber)
    ).set_parse_action(lambda r: ("vp", *r))

    face_triplet = (
        pp.common.integer
        + Optional(
            (Suppress(Literal("/")) + pp.common.integer)
            | Literal("/").set_parse_action(pp.replace_with(-1))
        )
        + Optional(Suppress(Literal("/")) + pp.common.integer)
    ).set_parse_action(lambda r: tuple(r))

    face_parameter = (
        Suppress(Literal("f")) + OneOrMore(face_triplet)
    ).set_parse_action(lambda r: ("f", *r))

    comment = Suppress(Literal("#") + SkipTo(LineEnd(), include=True))

    obj_entry = (
        vertex_coordinate
        | texture_coordinate
        | vertex_normal
        | vertex_parameter
        | face_parameter
        | comment
    )

    obj_file = OneOrMore(obj_entry)

    return obj_file


class ObjFile:
    def __init__(self) -> None:
        self.vertices = []
        self.faces = set()

        self.face_to_vertices = dict()
        self.vertex_to_face = dict()

    def add_vertex(self, x, y, z):
        self.vertices.append((x, y, z))

    def add_face(self, *vertex_indicies):

        assert max(*vertex_indicies) < len(self.vertices) and min(*vertex_indicies) > 1

        for v in vertex_indicies:
            self.vertex_to_face[self.vertices[v]] = vertex_indicies

        self.face_to_vertices[vertex_indicies].append()


def parse_obj_file(obj_string: str):

    parser = build_obj_parser()

    elements = parser.parse_string(obj_string)

    verticies = []
    textures = []
    normals = []
    faces = []

    for e in elements:
        if e[0] == "v":
            verticies.append(e[1:])
        elif e[0] == "vt":
            textures.append(e[1:])
        elif e[0] == "vn":
            normals.append(e[1:])
        elif e[0] == "f":
            faces.append(e[1:])

    for f in faces:
        for vinfo in f:
            print(verticies[vinfo[0] - 1])


if __name__ == "__main__":
    with open("cube.obj", "r") as f:
        parse_obj_file(f.read())
