#include <set>
#include <vector>

class Mesh {
    private:


    public:

        class Vertex {
            public:
                double x, y, z;
                std::set<Vertex *> neighbours;
                Vertex (double x, double y, double z) : x (x), y (y), z (z) {};

                void addNeighbour (Vertex *n)
                {
                        this->neighbours.insert (n);
                }
        };

        std::vector<Vertex *> verticies;

        Mesh () {

        };

        Vertex *getVertexByIndex(size_t index) {
            return verticies[index];
        }

        void addVertex (double x, double y, double z)
        {
            this->verticies.push_back(new Vertex(x,y,z));
        }

        void addEdge (Vertex *a, Vertex *b)
        {
                a->addNeighbour (b);
                b->addNeighbour (a);
        };

        void addTriangle (Vertex *a, Vertex *b, Vertex *c)
        {
                this->addEdge (a, b);
                this->addEdge (b, c);
                this->addEdge (c, a);
        };

        

};
