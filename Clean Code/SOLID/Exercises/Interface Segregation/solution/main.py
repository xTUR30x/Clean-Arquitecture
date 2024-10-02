from employee import Employee
from robot import Robot

if __name__ == '__name__':
    robot = Robot()
    employee = Employee()

    lista_humanos: Human = [ employee]
    lista_robots: Robot = [robot]

    for humano in lista_humanos:
        humano.sleep()

    for robot in lista_robots:
        robot.work()