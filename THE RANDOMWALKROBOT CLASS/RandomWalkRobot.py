class Robot(RectangularRoom):
    def __init__(self, room, speed):
        self.room=room
        self.speed=speed
        self.direction=int(random.uniform(0,360))
        self.position=room.getRandomPosition()

    def getRobotPosition(self):
        return self.position
        
    def getRobotDirection(self):
        return self.direction
        

    def setRobotPosition(self, position):
        self.position=position
            

    def setRobotDirection(self, direction):
        self.direction=direction
        
    def updatePositionAndClean(self):
        """
        Simulate the raise passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        raise NotImplementedError


class RandomWalkRobot(Robot):
    def __init__(self, room, speed):
        Robot.__init__(self, room, speed)
        self.room.cleanTileAtPosition(self.getRobotPosition())
       
    def updatePositionAndClean(self):
        self.direction = random.randint(0,359)
        pos = self.getRobotPosition().getNewPosition(self.getRobotDirection(), self.speed)
        if self.room.isPositionInRoom(pos)== True:
            self.setRobotPosition(pos)
            self.room.cleanTileAtPosition(pos)
            
