def TowerOfHanoi(n, first, last, mid):
    """
    This function prints the moves required to solve the Tower of Hanoi puzzle.
    
    Parameters:
    n (int): The number of disks.
    first (str): The name of the initial rod.
    last (str): The name of the destination rod.
    mid (str): The name of the auxiliary rod.
    """
    # If there is only one disk, move it to the destination rod.
    if n == 1: 
        print("Move disk 1 from rod", first, "to rod", last) 
        return
    
    # Move n-1 disks from the initial rod to the auxiliary rod.
    TowerOfHanoi(n-1, first, mid, last) 
    
    # Move the remaining disk from the initial rod to the destination rod.
    print("Move disk", n, "from rod", first, "to rod", last)
    
    # Move n-1 disks from the auxiliary rod to the destination rod.
    TowerOfHanoi(n-1, mid, last, first) 

n=int(input())
TowerOfHanoi(n, 'F', 'M', 'L')   # First Rod-> F, Middle rod -> M, Last Rod -> L

"""
Complexity of the code

-Time Complexity - O(2^n)
-Space Complexity - O(2^n)

"""