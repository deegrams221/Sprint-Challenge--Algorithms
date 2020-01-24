class SortingRobot:
    def __init__(self, l):
        """
        SortingRobot takes a list and sorts it.
        """
        self._list = l          # The list the robot is tasked with sorting
        self._item = None       # The item the robot is holding
        self._position = 0      # The list position the robot is at
        self._light = "OFF"     # The state of the robot's light
        self._time = 0          # A time counter (stretch)

    def can_move_right(self):
        """
        Returns True if the robot can move right or False if it's
        at the end of the list.
        """
        return self._position < len(self._list) - 1

    def can_move_left(self):
        """
        Returns True if the robot can move left or False if it's
        at the start of the list.
        """
        return self._position > 0

    def move_right(self):
        """
        If the robot can move to the right, it moves to the right and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position < len(self._list) - 1:
            self._position += 1
            return True
        else:
            return False

    def move_left(self):
        """
        If the robot can move to the left, it moves to the left and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position > 0:
            self._position -= 1
            return True
        else:
            return False

    def swap_item(self):
        """
        The robot swaps its currently held item with the list item in front
        of it.
        This will increment the time counter by 1.
        """
        self._time += 1
        # Swap the held item with the list item at the robot's position
        self._item, self._list[self._position] = self._list[self._position], self._item

    def compare_item(self):
        """
        Compare the held item with the item in front of the robot:
        If the held item's value is greater, return 1.
        If the held item's value is less, return -1.
        If the held item's value is equal, return 0.
        If either item is None, return None.
        """
        if self._item is None or self._list[self._position] is None:
            return None
        elif self._item > self._list[self._position]:
            return 1
        elif self._item < self._list[self._position]:
            return -1
        else:
            return 0

    def set_light_on(self):
        """
        Turn on the robot's light
        """
        self._light = "ON"
    def set_light_off(self):
        """
        Turn off the robot's light
        """
        self._light = "OFF"
    def light_is_on(self):
        """
        Returns True if the robot's light is on and False otherwise.
        """
        return self._light == "ON"

    def sort(self):
        """
        Sort the robot's list.
        """
        # Fill this out

    # Rules:
        # You may use any pre-defined robot methods.
        # You may NOT modify any pre-defined robot methods.
        # You may use logical operators. (if, and, or, not, etc.)
        # You may use comparison operators. (>, >=, <, <=, ==, is, etc.)
        # You may use iterators. (while, for, break, continue)
        # You may NOT store any variables. (=)
        # You may NOT access any instance variables directly. (self._anything)
        # You may NOT use any Python libraries or class methods. (sorted(), etc.)
        # You may define robot helper methods, as long as they follow all the rules.
    # Notes:
        # Robots functions are moving left/right, swap items, turning it's light on/off
        # Tests should run in far less than 1 second.
        # The robot has exactly one bit of memory: its light. I think this can be used to indicate
            # when the robot has started and ended sorting.
        # At first I thought bubble sort bc only movement is left/right but the robot is limited on
            # memory so I'm going to try selection sort
        # when an item is picked up it will leave 'none' at that postiton in the list

        # While true - set the light as ON to begin sort loop
        while self.light_is_on() == True:

            # start at 1st position of the list, use the self.swap_item() to pickup
            # move to the right to find smallest item in the list
                # compare the item being held to the item in the list, if it is greater than the item in the list,
                    # then swap_item() for the smaller item, repeat until moved all the way to the end of the right side of the list
                # if get to the end of the right of the list without finding a smaller item, then put the picked up item back in it's position (swap with 'none') by moving left
                # move right again, set the 2nd position as the new 'pivot' picking up the second item and leaving 'none' in 2nd position
                    # repeat the same process moving right until finding the next smallest item in the list

        # Else: to end the loop set the light as OFF

if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python robot_sort.py`

    l = [15, 41, 58, 49, 26, 4, 28, 8, 61, 60, 65, 21, 78, 14, 35, 90, 54, 5, 0, 87, 82, 96, 43, 92, 62, 97, 69, 94, 99, 93, 76, 47, 2, 88, 51, 40, 95, 6, 23, 81, 30, 19, 25, 91, 18, 68, 71, 9, 66, 1, 45, 33, 3, 72, 16, 85, 27, 59, 64, 39, 32, 24, 38, 84, 44, 80, 11, 73, 42, 20, 10, 29, 22, 98, 17, 48, 52, 67, 53, 74, 77, 37, 63, 31, 7, 75, 36, 89, 70, 34, 79, 83, 13, 57, 86, 12, 56, 50, 55, 46]

    robot = SortingRobot(l)

    robot.sort()
    print(robot._list)