import wpilib
from oi import OI
from robot_map import RobotMap


class MyRobot(wpilib.IterativeRobot):

    def robotInit(self):
        """
        This function is called upon program startup and
        should be used for any initialization code.
        """
        # Create operator interface
        self.oi = OI(self)

        lowerMotorSpark = Spark(RobotMap.lowerMotor)
        upperMotorSpark = Spark(RobotMap.upperMotor)

    def autonomousInit(self):
        pass

    def autonomousPeriodic(self):
        """This function is called periodically during autonomous."""
        pass

    def teleopPeriodic(self):
        """This function is called periodically during operator control."""
        lowerMotorSpark.set(stick0.getY())
        upperMotorSpark.set(stick1.getY())

    def testPeriodic(self):
        """This function is called periodically during test mode."""
        pass

if __name__ == "__main__":
    wpilib.run(MyRobot)
