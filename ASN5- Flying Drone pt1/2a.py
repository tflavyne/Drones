from djitellopy import Tello

tello = Tello()

tello.connect()
print(tello.get_battery())
tello.takeoff()

tello.move_forward(100)
print(tello.get_battery())
tello.land()