class MyCalendar:

    def __init__(self):
        self.cal = None

    def insertInterval(self, root, interval):

        if root is None:

            nd = IntervalNode()

            nd.max = interval[1]
            nd.interval = interval

            return nd

        else:

            if root.interval[0] > interval[0]:

                root.left = self.insertInterval(root.left, interval)
            else:
                root.right = self.insertInterval(root.right, interval)

            if root.max < interval[1]:
                root.max = interval[1]

        return root

    def hasOverlappingInterval(self, root, interval):

        if root is None:
            return False

        if not (interval[1] < root.interval[0]
                or interval[0] > root.interval[1]):
            return True

        else:
            if root.left is not None and root.left.max < interval[0]:
                return self.hasOverlappingInterval(root.left, interval)
            else:
                return self.hasOverlappingInterval(root.right, interval)

    def book(self, start, end):
        interval = [start, end]

        if self.hasOverlappingInterval(self.cal, interval):
            return False
        else:
            self.cal = self.insertInterval(self.cal, interval)
            return True


class IntervalNode:

    def __init__(self):

        self.left = None
        self.right = None
        self.interval = None
        self.max = None


cal = MyCalendar()

print(cal.book(10, 20))
print(cal.book(15, 30))
