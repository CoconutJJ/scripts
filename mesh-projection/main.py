from re import compile
from argparse import ArgumentParser
import numpy as np


def read_obj(
    obj_filename: str,
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    file_lines = open(obj_filename, "r").readlines()

    vertex_pattern = compile(r"v (-?\d+\.?\d*) (-?\d+\.?\d*) (-?\d+\.?\d*)$")
    # vertex_texture_pattern = compile(r"vt (-?\d+\.?\d*) (-?\d+\.?\d*)$")
    # vertex_normal_pattern = compile(r"vn (-?\d+\.?\d*) (-?\d+\.?\d*) (-?\d+\.?\d*)$")
    vertex_face_pattern = compile(
        r"f ((?:\d)|(?:\d*\/\d*\/\d*)){1} ((?:\d)|(?:\d*\/\d*\/\d*)){1} ((?:\d)|(?:\d*\/\d*\/\d*)){1}$"
    )

    def map_to_floats(seq: list | tuple) -> list:
        return list(map(lambda r: float(r), seq))

    verticies = []
    # textures = []
    # normals = []
    faces = []


    for l in file_lines:
        l = l.strip()
        if (match := vertex_pattern.match(l)) is not None:
            vertex = match.groups()
            verticies.append(map_to_floats(vertex))
        # elif (match := vertex_texture_pattern.match(l)) is not None:
        #     texture = match.groups()
        #     textures.append(map_to_floats(texture))
        # elif (match := vertex_normal_pattern.match(l)) is not None:
        #     normal = match.groups()
        #     normals.append(map_to_floats(normal))
        elif (match := vertex_face_pattern.match(l)) is not None:
            face = match.groups()
            face = map(lambda r: list(map(lambda t: int(t), r.split("/"))), face)
            faces.append(list(face))

    verticies = np.array(verticies)
    faces = np.array(faces)
    faces = faces[:, :, 0] - 1

    return (
        verticies,
        # np.array(textures),
        # np.array(normals),
        faces,
    )


def project_onto_plane(
    normal: np.ndarray, direction: np.ndarray, x: np.ndarray
) -> np.ndarray:
    return x - (normal.dot(x) / normal.dot(direction)) * direction


def project_onto_triangle(
    triangle: np.ndarray, direction: np.ndarray, x: np.ndarray
) -> np.ndarray | None:
    a, b, c = triangle

    normal = np.cross(b - a, c - a)

    projected_point = project_onto_plane(normal, direction, x)

    if np.linalg.norm(normal) == (
        np.linalg.norm(np.cross(projected_point - a, c - a))
        + np.linalg.norm(np.cross(projected_point - a, b - a))
        + np.linalg.norm(np.cross(projected_point - b, c - b))
    ):
        return projected_point

    return None


def center_mesh(mesh: tuple[np.ndarray, np.ndarray]):
    verts, faces = mesh

    avg_middle = np.sum(verts, axis=0) / verts.shape[0]

    return verts - avg_middle, faces


def jarvis_march(verticies: np.ndarray[np.ndarray[np.float64, np.float64]]):
    # ensure points are 2D
    assert verticies.shape[1] == 2

    start = verticies[np.argmin(verticies[:, 1], axis=0)]
    prev = np.array([-1, 0])

    hull = [start]

    head = start

    while True:
        curr = head
        for r in verticies:
            c = np.cross(prev, r - head)

            if c < 0:
                continue

            if np.cross(prev, curr - head) < c:
                curr = r

        if curr == start:
            break

        hull.append(head)
        prev = head - curr
        head = curr

    return hull

def project_onto_mesh(
    source: tuple[np.ndarray, np.ndarray],
    item: tuple[np.ndarray, np.ndarray],
    direction: tuple[np.ndarray, np.ndarray],
):
    source_verts, source_faces = source

    item_verts, item_faces = item

    direction = -direction / np.linalg.norm(direction)
    item_verts = item_verts + 100 * direction

    zbuffer = dict()
    for iv in item_verts:
        for tri_idx in source_faces:

            tri = source_verts[tri_idx]

            p = project_onto_triangle(tri, direction, iv)

            if p is None:
                continue
            
            key = tuple(iv)
            if key in zbuffer:
                
                p_dist = np.linalg.norm(iv - p)
                old_dist = np.linalg.norm(iv - zbuffer[key])

                if p_dist < old_dist:
                    zbuffer[key] = p
            else:
                zbuffer[key] = p

    



def loop_subdivision(
    verticies: np.ndarray, faces: np.ndarray
) -> tuple[np.ndarray, np.ndarray]:

    new_verticies = []
    vertex_index_map = dict()
    vertex_count = 0
    new_faces = []
    for tri in faces:
        face = verticies[tri]

        a, b, c = face

        v1 = (a + b) / 2
        v2 = (a + c) / 2
        v3 = (b + c) / 2

        new_vertex_list = [a, b, c, v1, v2, v3]

        for v in new_vertex_list:
            v = tuple(v)

            if v in vertex_index_map:
                continue

            vertex_index_map[v] = vertex_count
            vertex_count += 1
            new_verticies.append(v)

        for f in [(a, v1, v2), (b, v1, v3), (c, v2, v3), (v1, v2, v3)]:
            a, b, c = f
            a = tuple(a)
            b = tuple(b)
            c = tuple(c)
            new_faces.append(
                [
                    vertex_index_map[a] + 1,
                    vertex_index_map[b] + 1,
                    vertex_index_map[c] + 1,
                ]
            )

    return np.array(new_verticies), np.array(new_faces)


if __name__ == "__main__":
    args = ArgumentParser()

    args.add_argument("--obj", type=str, required=True)
    args.add_argument("--subdivide", action="store_true")
    args.add_argument("--convex_hull", action="store_true")
    params = args.parse_args()

    verticies, faces = read_obj(params.obj)

    if params.subdivide:
        loop_subdivision(verticies, faces)
    elif params.convex_hull:
        jarvis_march(verticies)

    # print(v1, v2, v3)
