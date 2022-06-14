from djitellopy import Tello

tello = Tello()

tello.connect()
print(tello.get_battery())
tello.takeoff()
#One angle
tello.rotate_clockwise(60)
tello.move_forward(50)
tello.rotate_clockwise(60)
tello.move_forward(50)
tello.rotate_clockwise(60);
tello.move_forward(50)
tello.rotate_clockwise(60)
tello.move_forward(50)
tello.rotate_clockwise(60)
tello.move_forward(50)
tello.rotate_clockwise(60)
tello.move_forward(50)

print(tello.get_battery())
tello.land()
