class Difference:
    def __init__(self, a):
        self.__elements = a
    def __init__(self,a):
        self.elements = a

    # Add your code here
    def computeDifference(self):
        elem_list = list(self.elements)
        min_elem = min(elem_list)
        max_elem = max(elem_list)
        max_diff = max_elem - min_elem
        self.maximumDifference = max_diff


# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
