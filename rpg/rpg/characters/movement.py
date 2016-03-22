#handling the arithmetic for north south east west movement.
# Y + 1 = north
# Y - 1 = South
# X + 1 = East
# X - 1 = West

#Creating a list for the x/y co-ords of the map.
x,y,z = 0, 0, 0
a,b,c = "1", "2" , "3"


home = [0,0,0]
coords = [x,y,z]
scenery = [a,b,c]      
mapArray = [home,coords,scenery]   #abc can hold room item information?

class Movement(object):
    
    def north(self, x ,y):
            print "You have gone North"
            return y + 1;
    def south(self, x, y):
            print "You have gone South"
            y =  y - 1
            print y
            return y;
    def east(self, x, y):
            print "You have gone East"
            x =x + 1
            print x
            return x;
    def west(self,x ,y):
            print "You have gone West"
            x = x - 1
            print x
            return x;

