#include <algorithm>
#include <iostream>
#include <vector>
struct Sample {
        double ts;
        std::vector<std::string> stack;
};

struct Event {
        std::string kind;
        double ts;
        std::string name;

        void printDebug ()
        {
                std::cout << "Kind: " << kind << "\n";
                std::cout << "Timestamp: " << ts << "\n";
                std::cout << "Name: " << name << "\n";
        }
};

std::vector<Event> convertToTrace (const std::vector<Sample> &samples)
{
        std::vector<Event> events;
        std::vector<std::string> currentStack;

        for (const Sample &s : samples) {
                int N = std::max (currentStack.size (), s.stack.size ());

                for (int i = 0; i < N; i++) {
                        struct Event e;

                        if (i < currentStack.size () && i < s.stack.size ()) {
                                if (currentStack[i] == s.stack[i])
                                        continue;
                                events.push_back ({ .kind = "start", .ts = s.ts, .name = s.stack[i] });
                                events.push_back ({ .kind = "end", .ts = s.ts, .name = currentStack[i] });
                        } else if (i >= s.stack.size ()) {
                                events.push_back({ .kind = "end", .ts = s.ts, .name = currentStack[i] });
                        } else if (i >= currentStack.size ()) {
                                events.push_back({ .kind = "start", .ts = s.ts, .name = s.stack[i] });
                        }
                }

                currentStack = s.stack;
        }

        return events;
}

int main (int argc, char **argv)
{
        std::vector<Sample> samples = {
                { .ts = 1.0,          .stack = { "main" } },
                { .ts = 1.4, .stack = { "main", "hello" } },
                { .ts = 1.6, .stack = { "main", "world" } },
                { .ts = 2.0,          .stack = { "main" } }
        };

        std::vector<Event> events = convertToTrace (samples);

        for (Event &evt : events)
                evt.printDebug ();
}
