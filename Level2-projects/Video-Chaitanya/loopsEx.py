# Simple example of nested loops.
for floor in range(100,120,10):
    print("floor=", floor)
    for room in range(100,120,10):
        print("room=", room)
        print("(floor=", floor, ", room=", room, ")")
        if (floor >100):
            print("100")
        else:
            print("0")
        
    
        
