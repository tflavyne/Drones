from djitellopy import Tello

tello = Tello()

tello.connect()
print(tello.get_battery())
tello.takeoff()

tello.move_forward(30)
tello.rotate_clockwise(72)
tello.move_forward(30)
tello.rotate_counter_clockwise(144)
tello.move_forward(30)
tello.rotate_clockwise(72)
tello.move_forward(30)
tello.rotate_counter_clockwise(144)
tello.move_forward(30)
tello.rotate_clockwise(72)
tello.move_forward(30)
tello.rotate_counter_clockwise(144)
tello.move_forward(30)
tello.rotate_clockwise(72)
tello.move_forward(30)
tello.rotate_counter_clockwise(144)
tello.move_forward(30)
tello.rotate_clockwise(72)
tello.move_forward(30)

print(tello.get_battery())
tello.land()

