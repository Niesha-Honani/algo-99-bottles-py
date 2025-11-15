"""Function to countdown the"""
def bottle_song(bottles):
    """function counts down bottles and returns a final statement"""
    count = int(bottles)
    
    for __ in range(bottles):
    
        if count == 2:
            print(f"{count} bottles of beer on the wall, {count} bottles of beer.")
            count -=1
            print(f"Take one down and pass it around, {count} bottle of beer on the wall.\n")
    
        
        
        elif count > 2:
            print(f"{count} bottles of beer on the wall, {count} bottles of beer.")
            count -=1
            print(f"Take one down and pass it around, {count} bottles of beer on the wall.\n")
    
        else:
            print(f"{count} bottle of beer on the wall, {count} bottle of beer.")
            
            print("Take one down pass it around, no more bottles of beer on the wall.")
            print("No more bottles of beer on the wall, no more bottles of beer.\n")
            
    return(f"Go to the store and buy some more, {bottles} bottles of beer on the wall.")
