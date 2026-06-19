#include <cstddef>
#include <vector>
#define TINYOBJLOADER_IMPLEMENTATION // define this in only *one* .cc
#include "mesh.hpp"
#include "tiny_obj_loader.hpp"

int main (int argc, char **argv)
{
        tinyobj::attrib_t attrib;
        std::vector<tinyobj::shape_t> shapes;
        std::vector<tinyobj::material_t> materials;
        std::string warn, err;

        tinyobj::LoadObj (&attrib, &shapes, &materials, &warn, &err, "assets/cube.obj", NULL, true);

        Mesh mesh;

        for (size_t i = 0; i < attrib.vertices.size () / 3; i++) {
                double x = attrib.vertices[3 * i], y = attrib.vertices[3 * i + 1], z = attrib.vertices[3 * i + 2];
                mesh.addVertex (x, y, z);
        }

        for (size_t i = 0; i < shapes.size (); i++) {
                assert (shapes[i].mesh.indices.size () == 3);
                Mesh::Vertex *v1 = mesh.getVertexByIndex (shapes[i].mesh.indices[0].vertex_index);
                Mesh::Vertex *v2 = mesh.getVertexByIndex (shapes[i].mesh.indices[1].vertex_index);
                Mesh::Vertex *v3 = mesh.getVertexByIndex (shapes[i].mesh.indices[2].vertex_index);
                mesh.addTriangle (v1, v2, v3);
        }


        



}
