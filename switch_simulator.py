import tkinter as tk
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)

class ButtonModel:
    __value = 0

    def toggle(self):
        if self.__value == 0:
            self.__value = 1
        else:
            self.__value = 0

    def get_value(self):
        return self.__value
    
class Switch:
    __position = 0
         
    def get_position(self):
        obj1 = ButtonModel()
        self.bt = ButtonModel.get_value(obj1)
        self.bt = self.__position
        return self.__position
    
    def turn_on(self):
        if self.__position == 1:
            self.handleSwitchOnCommand()
    
    def turn_off(self):
        if self.__position == 0:
            self.handleSwitchOffCommand()
      
    
class LED:
    
    __status = 0
    __switch_on_handler = None
    __switch_off_handler = None

    def __init__(self, status=0, on_switch_on=None, on_switch_off=None):
        self.__status = status
        self.__switch_on_handler = on_switch_on
        self.__switch_off_handler = on_switch_off

    def switch_on(self):
        self.__status = 1
        if self.__switch_on_handler is not None:
            self.__switch_on_handler()

    def switch_off(self):
        self.__status == 0
        if self.__switch_off_handler is not None:
            self.__switch_off_handler()
            
    def led1(self):
        obj2 = Switch()
        self.sw = Switch.get_position(obj2)
        self.__status = self.sw
        if self.sw == 1:
            on_switch_on = self.switch_on_led1()
        else:
            on_switch_off = self.switch_off_led2()
            
    def led2(self):
        obj2 = Switch()
        self.sw = Switch.get_position(obj2)
        if self.sw == 0:
            on_switch_on = self.switch_on_led2()
        else:
            on_switch_off = self.switch_off_led1()
            
    def switch_on_led1(self):
    # код для включения светодиода 1
        GPIO.output(24, GPIO.HIGH)
        
    def switch_off_led1(self):
    # код для выключения светодиода 1
        GPIO.output(24, GPIO.LOW)
        
    def switch_on_led2(self):
    # код для включения светодиода 2
        GPIO.output(12, GPIO.HIGH)
        
    def switch_off_led2(self):
    # код для выключения светодиода 2
        GPIO.output(12, GPIO.LOW)



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
        self.__clickHandler.handleClick()
    
class SwitchController:
    # TODO: дописать этот класс до конца
    __buttonModel = None
    __positionOnLed = None
    __positionOffLed = None
    __switchModel = None

    def __init__(self, model, led1, led2, switch):
        self.__buttonModel = model
        self.__positionOn = led1
        self.__positionOff = led2
        self.__switchModel = switch

    def handleClick(self):
        self.__buttonModel.toggle()
        self.__buttonModel.get_value()
        self.__switchModel.get_position()
    
    def handleSwitchOnCommand(self):
        self.__positionOn.led1()
       
    def handleSwitchOffCommand(self):
        self.__positionOff.led2()
        
  #  def handleSwitch(self):
  #      self.__switchModel.get_position()
        
if __name__ == "__main__":
    
    l1 = LED ()
    
    l2 = LED ()
    
    object_model = ButtonModel()
    
    sw = Switch ()

    object_command = SwitchController(model = object_model, led1 = l1, led2 = l2, switch = sw)
    bt = ButtonView("Toggle", command = object_command)
    bt.mainloop()
 

