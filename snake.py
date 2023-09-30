import random;

class snake:
    def __init__(self):
        self.width = 500;
        self.height = 500;
        self.direction = 0;
        self.headLocation = [3,3];
        self.tailLocation = [0,3];
        self.length = 5;
        self.name = "Chewy";
    
    def grow (self):
        self.length += 1;
    def go (self):
        
    
    def turn (self, choice):
        match choice:
            case 0: 
                # do nothing
                self.direction = self.direction;
            case 1: 
                self.direction -= 1;
                self.direction %= 4;
            case 2:
                self.direction += 1;
                self.direction %= 4;


    #should we be passing all of these into the step function?
    def step (self, choice):
        fruitLocation = [random.randrange(0,255), random.randrange(0,255)]
        self.turn(choice);

        if self.headLocation == fruitLocation:
            gotFruit = True;
        if gotFruit:
            self.grow();
        

        self.go();

            
        gotFruit = False;





        # 0 direction is down, 1 direction is up, 2 direction is left, 3 direction is right

snake = snake();
snake.step(2);
print(snake.direction);