# Simple example of nested loops.
for row in range(100,0,-10):
    print("row=", row)
    for col in range(100,120,10):
        print("col=", col)
        print("(row=", row, ", col=", col, ")")
        if (row >100):
            print("100")
        else:
            print("0")
        
    
        
