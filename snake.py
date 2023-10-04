import random;

class snake:
    def __init__(self):
        self.width = 500;
        self.height = 500;
        self.direction = 0;
        self.tailDirection = 0;
        self.headLocation = [3,3];
        self.tailLocation = [0,3];
        self.changed = False;
        self.length = 5;
        self.name = "Chewy";
        self.bendPoints = [self.headLocation, self.tailLocation];
        self.isDead = False;
        self.gotFruit = False;
        self.fruitLocation = [random.randrange(0,255), random.randrange(0,255)]

    def line (self, x1, y1, x2, y2, y, x):
        m = (y1-y2)/(x1-x2);
        b = (x1*y2 - x2*y1)/(x1-x2);
        if y == m*x + b:
            return True;

    def dead (self, testPointX, testPointY) :
        for x in range(len(self.bendPoints)) :
            if self.line(self, self.bendPoints[x][0], self.bendPoints[x][1], self.bendPoints[x+1][0], self.bendPoints[x+1][1], testPointX, testPointY):
                self.isDead = True;
    
    def grow (self):
        self.length += 1;

    def go (self):
        if self.tailLocation == self.bendPoints(len(self.bendPoints)):
            self.bendPoints.pop(len(self.bendPoints));
        
        if self.bendPoints[len(self.bendPoints)][0]-self.tailLocation[0] > 0: 
            tailDirection = 1;
        elif self.bendPoints[len(self.bendPoints)][1]-self.tailLocation[1] > 0:
            tailDirection = 0;
        elif self.bendPoints[len(self.bendPoints)][0]-self.tailLocation[0] < 0: 
            tailDirection = 3;
        else:
            tailDirection = 2;

        match self.direction:
            case 0:
                self.headLocation[1] += 1;
            case 1:
                self.headLocation[0] += 1;
            case 2: 
                self.headLocation[1] -= 1;
            case 3:
                self.headLocation[0] -= 1;
        match self.tailDirection:
            
            case 0:
                self.tailLocation[1] += 1;
            case 1:
                self.tailLocation[0] += 1;
            case 2: 
                self.tailLocation[1] -= 1;
            case 3:
                self.tailLocation[0] -= 1;
        self.dead(self, self.headLocation[0], self.headLocation[1])

    def turn (self, choice):
        match choice:
            case 0: 
                # do nothing
                self.direction = self.direction;
            case 1: 
                self.direction -= 1;
                self.direction %= 4;
                self.bendPoints.insert(1, self.headLocation);

            case 2:
                self.direction += 1;
                self.direction %= 4;
                self.bendPoints.insert(1, self.headLocation);
        self.changed = True;

    def step (self, choice):

        self.turn(choice);

        if self.headLocation == self.fruitLocation:
            self.gotFruit = True;
            self.fruitLocation = [random.randrange(0,255), random.randrange(0,255)]
        if self.gotFruit:
            self.grow();


        self.go();


        self.gotFruit = False;





        # 0 direction is down, 1 direction is up, 2 direction is left, 3 direction is right

snake = snake();
snake.step(2);
print(snake.direction);