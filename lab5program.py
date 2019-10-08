from lab5cst8279 import lab5Library

print("1. Make a horizontal line on gfx hat")
print("2. Make a verticle line on gfx hat")
print("3. Make a staircase on gfx hat")
print("4. Make it rain on the gfx hat")
print("5. Clear the Gfxhat screen")

choice = input("What do you want to do with your gfxhat?")
choice = int(choice)

if choice == 1:
    ycoordinate = input("Please enter the y-coordinate you want to use: ")
    ycoordinate = int(ycoordinate)
    lab5Library.horizontalLine(ycoordinate)
elif choice ==2:
    xcoordinate = input("Please enter the x-coordinate you want to use: ")
    xcoordinate = int(xcoordinate)
    lab5Library.verticleLine(xcoordinate)
elif choice ==3:
    xcoordinate = input("Please enter the x-coordinate you want to use: ")
    ycoordinate = input("Please enter the y-coordinate you want to use: ")
    ycoordinate = int(ycoordinate)
    xcoordinate = int(xcoordinate)
    lab5Library.staircase(xcoordinate, ycoordinate)
elif choice ==4:
    lab5Library.pixelrain()
else
    lab5Library.clearBacklight()


lcd.show()