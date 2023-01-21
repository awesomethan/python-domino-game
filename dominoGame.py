#Author: Ethan Wang
#Date: April 21, 2020
#Purpose: OOP Composition of Classes - Domino Hand Class
#-------------------------------------------------------

from tkinter import *
import random

#Author: Ethan Wang
#Date: April 11, 2020
#Purpose: A domino object
#DATA ELEMENTS:
# value - 0 <= value <= 66
# size - 30 <= size <= 100
# diameter - size // 5
# gap - diameter // 2
# orientation - "H" (Horizontal) or "V" (Vertical)
# face - face up (True) or face down (False)
#METHODS:
# __init__() - Constructor
# __str__() - Returns the value of the domino as a String
# validate() - To check whether the data elements of a domino are valid or not and change invalid fields
# getValue() - To get a valid value of the domino from the user with editing and prompting and set the value of the domino
# setValue(value) - To set the value of the domino to a valid value obtained via parameters
# getInteger(prompt,low,high) - To get a valid positive integer in a specified range
# flip() - To flip the two digits of the value of the domino
# setOrientation(orientation) - To set the orientation of the domino via parameters
# setSize(size) - To set the size of the domino via parameters
# setFace(face) - To set the face of the domino via parameters
# randomizeValue() - To randomly set the value of the domino to a new valid value
# draw(canvas, x, y) - To draw the domino
# drawHalf(canvas, x, y, value, orientation) - To draw one half of the domino
class Domino:

    #constructor
    def __init__ (self, value = 0, size = 30, orientation = "H", face = True):
        self.value = value
        self.size = size
        self.diameter = self.size // 5
        self.gap = self.diameter // 2
        self.orientation = orientation
        self.face = face
        self.validate()

    #Author: Ethan Wang
    #Date: April 11, 2020
    #Purpose: To get the value of a domino as a String
    #Parameters: None
    #Return: String conversion
    def __str__ (self):
        return "The value of your domino is " + str(self.value)

    #Author: Ethan Wang
    #Date: April 22, 2020
    #Purpose: To check whether the data elements of a domino are valid or not and change invalid fields
    #Parameters: None
    #Return: None
    def validate (self):
        if str(self.value).isdigit():
            if self.value//10 > 6 or self.value%10 > 6:
                self.value = 0
        else:
            self.value = 0
        if str(self.size).isdigit():
            if self.size < 30 or self.size > 100:
                self.size = 60
        else:
            self.size = 60
        self.diameter = self.size // 5
        self.gap = self.diameter // 2
        if self.orientation != "H" and self.orientation != "V":
            self.orientation = "H"
        if type(self.face) != bool:
            self.face = True

    #Author: Ethan Wang
    #Date: April 11, 2020
    #Purpose: To get a valid value of the domino from the user with editing and prompting and set the value of the domino
    #Parameters: None
    #Return: An integer representing the value of the domino
    #Dependencies: getInteger(prompt,low,high) and setValue(self,value)
    def getValue (self):
        firstDigit = self.getInteger("Please enter an integer x, where 0 <= x <= 6, representing the first digit of your domino value: ")
        secondDigit = self.getInteger("Please enter an integer y, where 0 <= y <= 6, representing the second digit of your domino value: ")
        self.setValue(int(str(firstDigit) + str(secondDigit)))

    #Author: Ethan Wang
    #Date: April 11, 2020
    #Purpose: To set the value of the domino to a valid value obtained via parameters
    #Parameters: An integer x, representing the value of the domino
    #Return: None
    def setValue (self,x=0):
        if intValue >= 0 and intValue // 10 <= 6 and intValue % 6 <= 6:
            self.value = intValue
        else:
            self.value = 0

    #Author: Ethan Wang
    #Date: April 11, 2020
    #Purpose: To get a valid positive integer in a specified range
    #Parameters: None
    #Return: A valid positive integer
    def getInteger (self,prompt="Please Enter a Positive Integer: ",low=0,high=6):
        strInput = " "
        intInput = -1
        isValid = False
        while (not strInput.isdigit() or not isValid):
            strInput = input(prompt)
            if strInput.isdigit():
                intInput = int(strInput)
                if (intInput >= low and intInput <= high):
                    isValid = True
                else:
                    print("ERROR: Please make sure that 0 <= N <= 6, where N is the integer you enter. Please try again.")
            else:
                print("ERROR: You did not enter a valid integer. Please try again.")
        return intInput

    #Author: Ethan Wang
    #Date: April 11, 2020
    #Purpose: To flip the two digits of the value of the domino
    #Parameters: None
    #Return: None
    def flip (self):
        firstDigit = self.value // 10
        secondDigit = self.value % 10
        self.value = int(str(secondDigit) + str(firstDigit))

    #Author: Ethan Wang
    #Date: April 11, 2020
    #Purpose: To set the orientation of the domino via parameters
    #Parameters: "H" or "V", where "H" represents a horizontal orientation and "V" represents a vertical orientation
    #Return: None
    def setOrientation (self, orientation="H"):
        if orientation == "H" or orientation == "V":
            self.orientation = orientation
        else:
            self.orientation = "H"

    #Author: Ethan Wang
    #Date: April 11, 2020
    #Purpose: To set the size of the domino via parameters
    #Parameters: The integer size of the domino
    #Return: None
    def setSize (self, size=30):
        if size >= 30 and size <= 100:
            self.size = size
        else:
            self.size = 30

    #Author: Ethan Wang
    #Date: April 11, 2020
    #Purpose: To set the face of the domino via parameters
    #Parameters: True or False, where True represents a 'face up' status and False represents a 'face down' one
    #Return: None
    def setFace (self, face=True):
        if face == True or face == False:
            self.face = face
        else:
            self.face = True

    #Author: Ethan Wang
    #Date: April 14, 2020
    #Purpose: To randomly set the value of the domino to a new valid value
    #Parameters: None
    #Return: None
    def randomizeValue (self):
        self.value = random.randint(0,6) * 10 + random.randint(0,6)

    #Author: Ethan Wang
    #Date: April 14, 2020
    #Purpose: To draw the domino
    #Parameters: A canvas 'c' to draw the domino and x and y, where P(x,y) represents the top left corner of the domino
    #Return: None
    #Dependency: drawHalf(self,c,x,y)
    def draw (self, c, x=0, y=0):
        self.diameter = self.size // 5
        self.gap = self.diameter // 2
        #first half of domino
        self.drawHalf(c, x, y, self.value//10,"H")
        #second half of domino
        self.drawHalf(c, x+self.size, y, self.value%10, "H")

    #Author: Ethan Wang
    #Date: April 15, 2020
    #Purpose: To draw one half of the domino
    #Parameters: A canvas 'c' to draw the domino, x and y, where P(x,y) represents the top left corner of the domino, a value representing
            #the value of this half of the domino, and the orientation of the domino to determine how to place the dots
    #Return: None
    def drawHalf (self, c, x=0, y=0, value=0, orientation="H"):
        c.create_rectangle(x, y, x+self.size, y+self.size, outline = "black", fill = "white")
        #SERIES OF IF STATEMENTS TO DETERMINE WHICH DOTS TO OUTPUT
        #TOP LEFT
        if value == 4 or value == 5 or value == 6:
            c.create_oval(x+self.gap, y+self.gap, x+self.gap+self.diameter, y+self.gap+self.diameter, fill = "black")
        #MIDDLE TOP
        if value == 6:
            c.create_oval(x+2*self.gap+self.diameter, y+self.gap, x+2*self.gap+2*self.diameter, y+self.gap+self.diameter, fill = "black")
        #BOTTOM LEFT
        if value == 2 or value == 3 or value == 4 or value == 5 or value == 6:
            c.create_oval(x+self.gap, y+7*self.gap, x+self.gap+self.diameter, y+3*self.gap+3*self.diameter, fill = "black")
        #MIDDLE
        if value == 1 or value == 3 or value == 5:
            c.create_oval(x+2*self.gap+self.diameter, y+2*self.gap+self.diameter, x+2*self.gap+2*self.diameter, \
                          y+2*self.gap+2*self.diameter, fill = "black")
        #TOP RIGHT
        if value == 2 or value == 3 or value == 4 or value == 5 or value == 6:
            c.create_oval(x+3*self.gap+2*self.diameter, y+self.gap, x+3*self.gap+3*self.diameter, y+self.gap+self.diameter, fill = "black")
        #MIDDLE BOTTOM
        if value == 6:
            c.create_oval(x+2*self.gap+self.diameter, y+3*self.gap+2*self.diameter, x+2*self.gap+2*self.diameter, \
                          y+3*self.gap+3*self.diameter, fill = "black")
        #BOTTOM RIGHT
        if value == 4 or value == 5 or value == 6:
            c.create_oval(x+3*self.gap+2*self.diameter, y+3*self.gap+2*self.diameter, x+3*self.gap+3*self.diameter, \
                          y+3*self.gap+3*self.diameter, fill = "black")


#Author: Ethan Wang
#Date: April 22, 2020
#Purpose: A domino hand object
#DATA ELEMENTS:
# firstDomino - instance of the Domino class
# secondDomino - instance of the Domino class
# thirdDomino - instance of the Domino class
# size - size of the three Domino objects
#METHODS:
# __init__ () - Constructor
# __str__ () - Returns the value of the domino as a String
# setSize (size) - To set the sizes of the 3 dominos in the hand via parameters
# sort () - To sort the three dominos in the domino hand from smallest to largest, based on their 'lesser' values
# roll () - To randomize each of the hand's 3 dominos
# draw (c, x, y) - To draw the 3 dominos in a line
# getRun () - To determine the largest 'run' of the hand of dominos
class DominoHand:
    #constructor
    def __init__ (self, first = Domino(), second = Domino(), third = Domino(), size = 60):
        self.firstDomino = first
        self.secondDomino = second
        self.thirdDomino = third
        self.setSize(size)

    #Author: Ethan Wang
    #Date: April 22, 2020
    #Purpose: To get the value of the domino hand as a String
    #Parameters: None
    #Return: String conversion
    def __str__ (self):
        return str(self.firstDomino.value) + " - " + str(self.secondDomino.value) + str(self.thirdDomino.value)

    #Author: Ethan Wang
    #Date: April 22, 2020
    #Purpose: To set the sizes of the 3 dominos in the hand via parameters
    #Parameters: The integer size of the dominos
    #Return: None
    def setSize (self, size = 60):
        if size >= 30 and size <= 100:
            self.firstDomino.setSize(size)
            self.secondDomino.setSize(size)
            self.thirdDomino.setSize(size)
        else:
            self.firstDomino.setSize(60)
            self.secondDomino.setSize(60)
            self.thirdDomino.setSize(60)

    #Author: Ethan Wang
    #Date: April 22, 2020
    #Purpose: To sort the three dominos in the domino hand from smallest to largest, based on their 'lesser' values
    #Parameters: None
    #Return: None
    #Dependency: The flip() method of the Domino objects which are data elements of the DominoHand object
    def sort (self):
        #make all values their 'lesser' values
        value1 = self.firstDomino.value
        flipped1 = False
        if value1//10 > value1%10:
            self.firstDomino.flip()
            value1 = self.firstDomino.value
            flipped1 = True
        value2 = self.secondDomino.value
        flipped2 = False
        if value2//10 > value2%10:
            self.secondDomino.flip()
            value2 = self.secondDomino.value
            flipped2 = True
        value3 = self.thirdDomino.value
        flipped3 = False
        if value3//10 > value3%10:
            self.thirdDomino.flip()
            value3 = self.thirdDomino.value
            flipped3 = True
        #sort
        if value1 > value2:
            temp = value1
            value1 = value2
            value2 = temp
            temp2 = flipped1
            flipped1 = flipped2
            flipped2 = temp2
        if value2 > value3:
            temp = value2
            value2 = value3
            value3 = temp
            temp2 = flipped2
            flipped2 = flipped3
            flipped3 = temp2
        if value1 > value2:
            temp = value1
            value1 = value2
            value2 = temp
            temp2 = flipped1
            flipped1 = flipped2
            flipped2 = temp2
        #update domino values
        self.firstDomino.value = value1
        if flipped1 == True:
            self.firstDomino.flip()
        self.secondDomino.value = value2
        if flipped2 == True:
            self.secondDomino.flip()
        self.thirdDomino.value = value3
        if flipped3 == True:
            self.thirdDomino.flip()
        
    #Author: Ethan Wang
    #Date: April 22, 2020
    #Purpose: To randomize each of the hand's 3 dominos
    #Parameters: None
    #Return: None
    #Dependency: The randomizeValue() method of the Domino objects which are data elements of the DominoHand object
    def roll (self):
        self.firstDomino.randomizeValue()
        self.secondDomino.randomizeValue()
        self.thirdDomino.randomizeValue()

    #Author: Ethan Wang
    #Date: April 22, 2020
    #Purpose: To draw the 3 dominos in a line
    #Parameters: A canvas 'c' to draw the domino and x and y, where P(x,y) represents the top left corner of the first domino
    #Return: None
    #Dependency: The draw() method of the Domino objects which are data elements of the DominoHand object
    def draw (self, c, x, y):
        self.firstDomino.draw(c, x, y)
        self.secondDomino.draw(c, x+2*self.firstDomino.size+10, y)
        self.thirdDomino.draw(c, x+4*self.firstDomino.size+20, y)

    #Author: Ethan Wang
    #Date: April 22, 2020
    #Purpose: To determine the largest 'run' of the hand of dominos
    #Parameters: None
    #Return: The largest 'run,' which is a value of 0, 2, or 3
    def getRun (self):
        run = 0
        value1 = self.firstDomino.value//10
        value2 = self.firstDomino.value%10
        value3 = self.secondDomino.value//10
        value4 = self.secondDomino.value%10
        value5 = self.thirdDomino.value//10
        value6 = self.thirdDomino.value%10

        if value1 == value3:
            if value2 == value5 or value2 == value6 or value4 == value5 or value4 == value6:
                run = 3
            else:
                run = 2
        elif value1 == value4:
            if value2 == value5 or value2 == value6 or value3 == value5 or value3 == value6:
                run = 3
            else:
                run = 2
        elif value2 == value3:
            if value1 == value5 or value1 == value6 or value4 == value5 or value4 == value6:
                run = 3
            else:
                run = 2
        elif value2 == value4:
            if value1 == value5 or value1 == value6 or value3 == value5 or value3 == value6:
                run = 3
            else:
                run = 2
        elif value1 == value5:
            if value2 == value3 or value2 == value4 or value6 == value3 or value6 == value4:
                run = 3
            else:
                run = 2
        elif value1 == value6:
            if value2 == value3 or value2 == value4 or value5 == value3 or value5 == value4:
                run = 3
            else:
                run = 2
        elif value2 == value5:
            if value1 == value3 or value1 == value4 or value6 == value3 or value6 == value4:
                run = 3
            else:
                run = 2
        elif value2 == value6:
            if value1 == value3 or value1 == value4 or value5 == value3 or value5 == value4:
                run = 3
            else:
                run = 2
        elif value3 == value5:
            if value4 == value1 or value4 == value2 or value6 == value1 or value6 == value2:
                run = 3
            else:
                run = 2
        elif value3 == value6:
            if value4 == value1 or value4 == value2 or value5 == value1 or value5 == value2:
                run = 3
            else:
                run = 2
        elif value4 == value5:
            if value3 == value1 or value3 == value2 or value6 == value1 or value6 == value2:
                run = 3
            else:
                run = 2
        elif value4 == value6:
            if value3 == value1 or value3 == value2 or value5 == value1 or value5 == value2:
                run = 3
            else:
                run = 2
        return run

#SUBPROGRAMS

#Author: Ethan Wang
#Date: April 23, 2020
#Purpose: To inform users of how the game works
#Parameters: None
#Return: None
def showInstructions():
    messagebox.showinfo("Instructions","Use the scales to set the sizes and values of your 3 dominos. Please make sure that both your tens digit and ones digit of your value are less than or equal to 6. Afterwards, click the '1', '2', or '3' key to draw the first, second, or third domino, respectively. Furthermore, you may click 'h' to draw your hand of dominos where all 3 dominos are the same size. Your original hand will be drawn, followed by the sorted hand. Lastly, you may click 'g' to perform a simulation by creating 10,000 random hands of dominos. Have fun!")

#Author: Ethan Wang
#Date: April 23, 2020
#Purpose: To show the 'about' message box for the program
#Parameters: None
#Return: None
def showAbout():
    messagebox.showinfo("About", "PY7 - Domino Hand Class by Ethan Wang.")

#Author: Ethan Wang
#Date: April 23, 2020
#Purpose: To clear the canvas displaying the various dominos
#Parameters: None
#Return: None
def clearCanvasBoard():
    canvas.delete(ALL)

#Author: Ethan Wang
#Date: April 28, 2020
#Purpose: To clear the text box displaying the simulation results
#Parameters: None
#Return: None
def clearSimulationBoard():
    widTextBox.config(state=NORMAL)
    widTextBox.delete(2.0,END)
    widTextBox.config(state=DISABLED)

#Author: Ethan Wang
#Date: April 27, 2020
#Purpose: To restore all domino values and sizes to their default values
#Parameters: None
#Return: None
def restoreDefaults():
    objValue1.set(0)
    objValue2.set(0)
    objValue3.set(0)
    objSize1.set(30)
    objSize2.set(30)
    objSize3.set(30)
    
#Author: Ethan Wang
#Date: April 22, 2020
#Purpose: To allow users to give commands via the click of a key
#Parameters: the key event
#Return: None
def keyPressed(event):
    if event.char == "1":
        if objValue1.get()%10 > 6:
            messagebox.showerror("Error","Please make sure that both digits of the value of your 1st domino are less than or equal to six. Your input is invalid because the second digit of your value is "+str(objValue1.get()%10)+", which is greater than 6.")
        else:
            canvas.delete(ALL)
            myDomino = Domino(objValue1.get(), objSize1.get())
            myDomino.draw(canvas, 10, 10)
    elif event.char == "2":
        if objValue2.get()%10 > 6:
            messagebox.showerror("Error","Please make sure that both digits of the value of your 2nd domino are less than or equal to six. Your input is invalid because the second digit of your value is "+str(objValue2.get()%10)+", which is greater than 6.")
        else:
            canvas.delete(ALL)
            myDomino = Domino(objValue2.get(), objSize2.get())
            myDomino.draw(canvas, 10, 10)
    elif event.char == "3":
        if objValue3.get()%10 > 6:
            messagebox.showerror("Error","Please make sure that both digits of the value of your 3rd domino are less than or equal to six. Your input is invalid because the second digit of your value is "+str(objValue3.get()%10)+", which is greater than 6.")
        else:
            canvas.delete(ALL)
            myDomino = Domino(objValue3.get(), objSize3.get())
            myDomino.draw(canvas, 10, 10)
    elif event.char == "h" or event.char == "H":
        isValid = True
        if objValue1.get()%10 > 6:
            messagebox.showerror("Error","Please make sure that both digits of the value of your 1st domino are less than or equal to six. Your input is invalid because the second digit of your value is "+str(objValue1.get()%10)+", which is greater than 6.")
            isValid = False
        if objValue2.get()%10 > 6:
            messagebox.showerror("Error","Please make sure that both digits of the value of your 2nd domino are less than or equal to six. Your input is invalid because the second digit of your value is "+str(objValue2.get()%10)+", which is greater than 6.")
            isValid = False
        if objValue3.get()%10 > 6:
            messagebox.showerror("Error","Please make sure that both digits of the value of your 3rd domino are less than or equal to six. Your input is invalid because the second digit of your value is "+str(objValue3.get()%10)+", which is greater than 6.")
            isValid = False
        if isValid:
            canvas.delete(ALL)
            myDominoHand = DominoHand()
            myDominoHand.setSize(objHandSize.get())
            myDominoHand.firstDomino.value = objValue1.get()
            myDominoHand.secondDomino.value = objValue2.get()
            myDominoHand.thirdDomino.value = objValue3.get()
            myDominoHand.draw(canvas, 10, 10)
            myDominoHand.sort()
            myDominoHand.draw(canvas, 10, 140)
            
            objRun.set(myDominoHand.getRun())
            widTextRun.config(state=NORMAL)
            widTextRun.delete(1.26,END)
            widTextRun.insert(INSERT, objRun.get())
    elif event.char == "g" or event.char == "G":
        runZero = 0
        runTwo = 0
        runThree = 0
        for i in range (10000):
            myDominoHand = DominoHand()
            myDominoHand.roll()
            run = myDominoHand.getRun()
            if run == 0:
                runZero += 1
            elif run == 2:
                runTwo += 1
            elif run == 3:
                runThree += 1
        widTextBox.config(state=NORMAL)
        widTextBox.delete(2.0,END)
        widTextBox.insert(INSERT,"\n\nNumber of runs of 0: " + str(runZero) + "\n")
        widTextBox.insert(INSERT,"Number of runs of 2: " + str(runTwo) + "\n")
        widTextBox.insert(INSERT,"Number of runs of 3: " + str(runThree) + "\n")
        widTextBox.insert(INSERT,"\nPercentage of runs of 0: " + str("%0.2f"%(runZero/100)) + "%\n")
        widTextBox.insert(INSERT,"Percentage of runs of 2: " + str("%0.2f"%(runTwo/100)) + "%\n")
        widTextBox.insert(INSERT,"Percentage of runs of 3: " + str("%0.2f"%(runThree/100)) + "%\n")
        widTextBox.config(state=DISABLED)
#MAIN
myWindow = Tk()
myWindow.title("Domino")
myWindow.resizable(0,0)
canvas = Canvas(myWindow, width = 640, height = 260)
canvas.config(background = "white")
canvas.bind("<Key>", keyPressed)
canvas.focus_set()
canvas.grid(row=1,rowspan=3,column=4,pady=5)

objValue1 = IntVar()
objValue2 = IntVar()
objValue3 = IntVar()
objSize1 = IntVar()
objSize2 = IntVar()
objSize3 = IntVar()
objHandSize = IntVar()
objRun = IntVar()

widSizeFrame1 = LabelFrame(myWindow,text="Size of 1st Domino")
widScaleSize1 = Scale(widSizeFrame1,from_=30,to=100,orient=HORIZONTAL,variable=objSize1)
widValueFrame1 = LabelFrame(myWindow,text="Value of 1st Domino")
widScaleValue1 = Scale(widValueFrame1,from_=0,to=66,orient=HORIZONTAL,variable=objValue1)

widSizeFrame2 = LabelFrame(myWindow,text="Size of 2nd Domino")
widScaleSize2 = Scale(widSizeFrame2,from_=30,to=100,orient=HORIZONTAL,variable=objSize2)
widValueFrame2 = LabelFrame(myWindow,text="Value of 2nd Domino")
widScaleValue2 = Scale(widValueFrame2,from_=0,to=66,orient=HORIZONTAL,variable=objValue2)

widSizeFrame3 = LabelFrame(myWindow,text="Size of 3rd Domino")
widScaleSize3 = Scale(widSizeFrame3,from_=30,to=100,orient=HORIZONTAL,variable=objSize3)
widValueFrame3 = LabelFrame(myWindow,text="Value of 3rd Domino")
widScaleValue3 = Scale(widValueFrame3,from_=0,to=66,orient=HORIZONTAL,variable=objValue3)

widHandSizeFrame = LabelFrame(myWindow,text="Size of Hand")
widScaleHandSize = Scale(widHandSizeFrame,from_=30,to=100,orient=VERTICAL,variable=objHandSize,length=230)

widLabelInstructions = Label(myWindow,text="Press 1, 2, or 3 to draw your first, second, or third domino, respectively. Press h to draw your hand of cards or g to perform a simulation." \
                            ,relief = "groove",width=100,font=("Times",16,"bold"))
widTextBox = Text(myWindow,height=11,width=32,relief="groove")
widTextBox.insert(INSERT, "STATISTICS OF SIMULATION")
widTextBox.config(state=DISABLED)
widTextRun = Text(myWindow,height=2,width=32,relief="groove")
widTextRun.insert(INSERT, "Largest run of your hand: ")
widTextRun.config(state=DISABLED)

widMenu = Menu(myWindow)
filemenu = Menu(widMenu, tearoff=0)
filemenu.add_separator()
filemenu.add_command(label = "Clear Canvas Board", command = lambda:clearCanvasBoard())
filemenu.add_command(label = "Restore Default Values", command = lambda:restoreDefaults())
filemenu.add_command(label = "Clear Simulation Board", command = lambda:clearSimulationBoard())
filemenu.add_command(label = "Exit", command = lambda:myWindow.destroy())
widMenu.add_cascade(label = "File", menu = filemenu)

helpmenu = Menu(widMenu, tearoff=0)
helpmenu.add_separator()
helpmenu.add_command(label = "Instructions", command = lambda:showInstructions())
helpmenu.add_command(label = "About", command = lambda:showAbout())
widMenu.add_cascade(label = "Help", menu = helpmenu)

myWindow.config(menu = widMenu)

widSizeFrame1.grid(row=1,column=2, sticky=W,padx=5,pady=5)
widScaleSize1.grid(row=1,padx=5,pady=5)
widValueFrame1.grid(row=1,column=1,sticky=E,padx=5,pady=5)
widScaleValue1.grid(row=1,padx=5,pady=5)

widSizeFrame2.grid(row=2,column=2, sticky=W,padx=5,pady=5)
widScaleSize2.grid(row=1,padx=5,pady=5)
widValueFrame2.grid(row=2,column=1,sticky=E,padx=5,pady=5)
widScaleValue2.grid(row=1,padx=5,pady=5)

widSizeFrame3.grid(row=3,column=2, sticky=W,padx=5,pady=5)
widScaleSize3.grid(row=1,padx=5,pady=5)
widValueFrame3.grid(row=3,column=1,sticky=E,padx=5,pady=5)
widScaleValue3.grid(row=1,padx=5,pady=5)

widHandSizeFrame.grid(row=1,rowspan=3,column=3,padx=5,pady=5)
widScaleHandSize.grid(row=1,rowspan=3,padx=5,pady=5)

widTextBox.grid(row=1,rowspan=2,column=5,padx=5,pady=5,sticky=S)
widTextRun.grid(row=3,column=5,padx=5,pady=5)
widLabelInstructions.grid(row=4,column=1,columnspan=5,padx=10,pady=10)

messagebox.showinfo("About","Welcome to the Domino Hand Game!")
showInstructions()
mainloop()
