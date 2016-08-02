import wpilib
from networktables import NetworkTable
from oi import OI
from robot_map import RobotMap


class MyRobot(wpilib.IterativeRobot):

    def robotInit(self):
        """
        This function is called upon program startup and
        should be used for any initialization code.
        """

        # self.camera = wpilib.USBCamera(name='cam1')
        # self.server = wpilib.CameraServer.getInstance()
        # self.server.setQuality(50)
        # self.server.startAutomaticCapture(self.camera)

        # Create operator interface
        self.oi = OI(self)

        self.lowerMotorSpark = wpilib.Spark(RobotMap.lowerMotor)
        self.upperMotorSpark = wpilib.Spark(RobotMap.upperMotor)

        self.sd = NetworkTable.getTable("SmartDashboard")
        self.sd.putNumber('upperMotorSpeed', 0)
        self.sd.putNumber('lowerMotorSpeed', 0)

    def autonomousInit(self):
        pass

    def autonomousPeriodic(self):
        """This function is called periodically during autonomous."""
        pass

    def teleopPeriodic(self):
        """This function is called periodically during operator control."""
        # self.lowerMotorSpark.set(self.oi.stick0.getY())
        # self.upperMotorSpark.set(self.oi.stick1.getY())
        lower = self.sd.getNumber('lowerMotorSpeed') / 100
        upper = self.sd.getNumber('upperMotorSpeed') / 100
        self.lowerMotorSpark.set(lower)
        self.upperMotorSpark.set(upper)
        print(lower)
        print(upper)

    def testPeriodic(self):
        """This function is called periodically during test mode."""
        pass

if __name__ == "__main__":
    wpilib.run(MyRobot)
