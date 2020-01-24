#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n)
    n is constant and there is just one loop, no nested elements

b) O(n^2)
    n is not constant and there is a nested while loop within a for loop
    ** correct answer is O(n log n)
        as the size of the input increases, the runtime used grows at a slightly faster rate

c) O(n)
    n, or 'bunnies', is constant and there is no loop

## Exercise II


n-story buildings and plenty of eggs
An egg gets broken if its thrown off floor gerater or equal to f (ie: broken)
The egg does not break if its thrown off a floor less than f (ie: not_broken)
Determin the value of f, such that the num of dropped + broken eggs is minimized

1. Find the middle floor by spliting the length of the amount of stories in the building
2. Drop an egg
    a. if it breaks, go down one floor, drop another egg
            if the egg does not break, subtract the dropped eggs(plus one) from the middle 
                floor, this will return floor f
            else if the egg does break, repeat step a
    b. else if it does not break, go up one floor, drop another egg
            if the egg breaks add number of dropped eggs to the middle floor, this will 
                retrun floor f
            else if the egg does not break, repeat step b

I think this solution would be O(n) becasue n would be constant and I dont think there 
    would be a nested loop
