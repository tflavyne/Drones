from djitellopy import Tello

tello = Tello()

tello.connect()
print(tello.get_battery())
tello.takeoff()

tello.move_forward(50)
tello.move_up(50)
tello.move_forward(50)
tello.move_up(50)
tello.move_forward(50)

print(tello.get_battery())
tello.land()