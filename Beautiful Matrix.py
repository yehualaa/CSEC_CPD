# Step 1: Loop through all 5 rows of the input
for i in range(1, 6):
    # Read the line and split into individual numbers
    row = raw_input().split()
    
    # Step 2: Check each number in the row to find the '1'
    if '1' in row:
        # Find the column index (adding 1 because list indices start at 0)
        # .index() returns the position of the first '1' found
        j = row.index('1') + 1
        
        # Step 3: Calculate the distance from the center (3, 3)
        # Distance = |current_row - 3| + |current_column - 3|
        ans = abs(i - 3) + abs(j - 3)
        
        # Step 4: Output the result and exit the loop
        print ans
        break
