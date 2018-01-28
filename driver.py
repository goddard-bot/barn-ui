import serial

class Robot_Driver():

    def __init__(self, port='/dev/ttyUSB0'):
        self.port = serial.Serial(port)

    def send(self, data):
        self.port.write(data.encode())

    def go_forward(self, color, count):
        for i in range(count):
            self.send("B" + color + "F")

    def reverse(self, color, count):
        for i in range(count):
            self.send("B" + color + "R")

    def clockwise(self, color):
        self.send("B" + color + "C")

    def counter_clockwise(self, color):
        self.send("B" + color + "W")

    def nope(self, color):
        self.send("B" + color + "N")

    def yep(self, color):
        self.send("B" + color + "Y")

    def get_mad(self, color):
        self.send("B" + color + "C")
        self.send("B" + color + "C")
        self.send("B" + color + "W")

    def update_color(self, color):
        self.send("B" + color + "Z")

    def sleep(self, color):
        self.send("B" + color + "L")


if __name__ == '__main__':
    port = input("Serial Port [/dev/ttyUSB0]: ")
    if port:
        drive = Robot_Driver(port)
    else:
        drive = Robot_Driver()

    while True:
        command = input("What do you want the robot to do? ")
        command = command.upper()
        if command == "F":
            drive.go_forward('123', 4)
        if command == "R":
            drive.reverse('234', 5)
        if command == "C":
            drive.clockwise('345')
        if command == "W":
            drive.counter_clockwise('456')
        if command == "M":
            drive.get_mad('900')
        if command == "U":
            drive.update_color('045')
        if command == "Y":
            drive.yep('093')
        if command == "N":
            drive.nope('432')
