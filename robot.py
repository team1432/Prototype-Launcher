import wpilib
from oi import OI


class MyRobot(wpilib.IterativeRobot):

    def robotInit(self):
        """
        This function is called upon program startup and
        should be used for any initialization code.
        """
        # Create operator interface
        self.oi = OI(self)

    def autonomousInit(self):

    def autonomousPeriodic(self):
        """This function is called periodically during autonomous."""

    def teleopPeriodic(self):
        """This function is called periodically during operator control."""

    def testPeriodic(self):
        """This function is called periodically during test mode."""

if __name__ == "__main__":
    wpilib.run(MyRobot)
