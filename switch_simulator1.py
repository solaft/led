import tkinter as tk
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
# 
# class ButtonModel:
#     __value = 0
# 
#     def toggle(self):
#         if self.__value == 0:
#             self.__value = 1
#         else:
#             self.__value = 0
# # меняет состояние кнопки при нажатии
#     def get_value(self):
#         return self.__value
# # возвращает состояние кнопки    
# 
class Switch:
    __position = None
    pos_enum = ["0", "1", "2", "3"]
    def __init__(self, position=None):
        self.__position = position
         
    def get_position(self):
        return self.__position
 #   def turn_on(self):
 #        self.__position == 1
        
 #   def turn_off(self):
 #       self.__position = 0
        
    def toggle(self):
        if self.__position == "0":
            self.__position = "1"
        else:
            self.__position = "0"
    def cycle(self):
        if self.position == self.pos_enum.index(self.pos_enum[-1]):
            self.position = 0
        else:
            self.position += 1
    
class LED:
    
    __status = 0
    __switch_on_handler = None
    __switch_off_handler = None
    __gpio_pin = None

    def __init__(self, gpio_pin, status=0, on_switch_on=None, on_switch_off=None):
        self.__gpio_pin = gpio_pin
        self.__status = status
        self.__switch_on_handler = on_switch_on
        self.__switch_off_handler = on_switch_off
        GPIO.setup(gpio_pin, GPIO.OUT)
        if status == 1:
            self.switch_on()
        else:
            self.switch_off()

    def switch_on(self):
        GPIO.output(self.__gpio_pin, GPIO.HIGH)
        self.__status = 1
#         if self.sw == self.__status:
#         # if self.__switch_on_handler is not None:
#             self.__switch_on_handler() 

    # функция, которая применяется позже для изменения состояния лампочек(включает)
    def switch_off(self):
        GPIO.output(self.__gpio_pin, GPIO.LOW)
        self.__status = 0
#         if self.sw == self.__status:
#         # if self.__switch_off_handler is not None:
#             self.__switch_off_handler()
#     # функция, которая применяется позже для изменения состояния лампочек(выключает)

    def toggle(self):
        if self.__status == 0:
            self.switch_on()
            
        else:
            self.switch_off()
        
        



class ButtonView(tk.Tk):

    __caption = "Toggle"
    __clickHandler = None

    def __init__(self, text, command):
        super().__init__()
        self.__caption = text
        self.__clickHandler = command
        self.btn = tk.Button(self, text="Toggle", command=self.click)
        self.btn.pack(padx=120, pady=30)
    def click(self):
        self.__clickHandler()
    
class SwitchController:
    # TODO: дописать этот класс до конца
    __positionOnLed = None
    __positionOffLed = None
    __switchModel = None

    def __init__(self, switch, ledOn, ledOff):
        self.__switchModel = switch
        self.__positionOnLed = switch
        self.__positionOffLed = switch
        self.__positionOnLed = ledOn
        self.__positionOffLed = ledOff
        if self.__switchModel.get_position() == 1:
            self.__positionOnLed.switch_on()
            self.__positionOffLed.switch_off()
        else:
            self.__positionOffLed.switch_on()
            self.__positionOnLed.switch_off()
    
    def handleClick(self):
        self.__switchModel.toggle()
        if self.__switchModel.get_position() == 1:
            self.__positionOnLed.switch_on()
            self.__positionOffLed.switch_off()
        else:
            self.__positionOffLed.switch_on()
            self.__positionOnLed.switch_off()



    
    
  #  def handleSwitchOnCommand(self):
        
       
 #   def handleSwitchOffCommand(self):
        
        
  #  def handleSwitch(self):
  #      self.__switchModel.get_position()
        
if __name__ == "__main__":
    
    l1 = LED (12, 1)
    
    l2 = LED (24, 0)
    
    time.sleep(.1)
    l1.toggle()
    l2.toggle()
    
    def toggle_leds():
        l1.toggle()
        l2.toggle()        
    
    
    
    #object_model = ButtonModel()
    
    sw = Switch (0)

    sw_ctl = SwitchController(switch = sw, ledOn = l1, ledOff = l2)
    
    bt = ButtonView("Toggle", command = sw_ctl.handleClick)
    bt.mainloop()
 

