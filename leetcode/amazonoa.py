import math


def movieDuration(flightDuration, movieDuration):
    # WRITE YOUR CODE HERE

    timesAvailable = {}

    totalTime = flightDuration - 30

    possiblePair = None

    for i in range(len(movieDuration)):

        d = movieDuration[i]

        if (totalTime - d) in timesAvailable:
            other_movie_id = timesAvailable[totalTime - d]

            if possiblePair is None:

                possiblePair = (i, timesAvailable[totalTime - d])

            else:
                movie1_duration, movie2_duration = movieDuration[possiblePair[0]
                                                                 ], movieDuration[possiblePair[1]]

                longestMovie = max(
                    movieDuration[i], movieDuration[other_movie_id])

                if longestMovie > max(movie1_duration, movie2_duration):
                    possiblePair = (i, other_movie_id)

        else:
            timesAvailable[d] = i

    return [possiblePair[0], possiblePair[1]]


class MinHeap:

    def __init__(self):

        self.heap = []

    def bubbleUp(self):

        curr_idx = len(self.heap) - 1
        parent_idx = (curr_idx - 1) // 2

        while True:

            if curr_idx == 0:
                break

            curr_dist = self.heap[curr_idx][0]

            parent_dist = self.heap[parent_idx][0]

            if curr_dist < parent_dist:

                parent_node = self.heap[parent_idx]

                self.heap[parent_idx] = self.heap[curr_idx]
                self.heap[curr_idx] = parent_node
                curr_idx = parent_idx
                parent_idx = (parent_idx - 1) // 2
            else:
                break

    def push(self, crate_coord):

        self.heap.append(crate_coord)
        self.bubbleUp()

    def pop(self):

        popped = self.heap[0]

        # remove the first element
        self.heap = self.heap[1:]

        # take last element in heap and bubble down
        self.heap = [self.heap[-1]] + self.heap[:-1]

        curr_idx = 0
        left_child_idx = 2 * curr_idx + 1
        right_child_idx = 2 * curr_idx + 2

        while True:

            if curr_idx == len(self.heap) - 1:
                break

            if left_child_idx < len(self.heap):
                left_child_dist = self.heap[left_child_idx][0]
            else:
                left_child_dist = float('inf')

            if right_child_idx < len(self.heap):
                right_child_dist = self.heap[right_child_idx][0]
            else:
                right_child_dist = float('inf')

            curr_dist = self.heap[curr_idx][0]
            swap_idx = -1

            if curr_dist > left_child_dist:
                swap_idx = left_child_idx
            elif curr_dist > right_child_dist:
                swap_idx = right_child_idx

            if swap_idx != -1:

                child_node = self.heap[swap_idx]

                self.heap[swap_idx] = self.heap[curr_idx]

                self.heap[curr_idx] = child_node

                curr_idx = swap_idx
                left_child_idx = 2 * curr_idx + 1
                right_child_idx = 2 * curr_idx + 2
            else:
                break

        return popped


def closestLocations(totalCrates, allLocations, truckCapacity):
    # WRITE YOUR CODE HERE

    heap = MinHeap()

    for l in allLocations:

        heap.push((math.sqrt(l[0]**2 + l[1]**2), l))

    closest = []

    for i in range(truckCapacity):

        (distance, coord) = heap.pop()

        closest.append(coord)

    return closest


print(closestLocations(3, [[1, 2], [3, 4], [1, -1]], 2))
