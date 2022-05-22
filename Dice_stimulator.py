
import random
import tkinter

window = tkinter.Tk()
window.geometry('600x600')
window.title('Roll Dice Stimulator')

label = tkinter.Label(window, text='', font='arial 260 bold')


#label to introduce
welcome_text = tkinter.Label(window, text='Dice Rolling Game', font=('arial',20, 'bold'))
welcome_text.place(x=200,y=400)

welcome_text.pack()

#creating dice
def roll_dice():
    value = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
    result=random.choice(value)
    label.configure(text=result)
    label.pack()
    if(result=='\u2680'):
        label3=tkinter.Label(window,text='You rolled a one!',fg = 'grey', font=('arial',15,'bold'))
        label3.place(x=200,y=500)
    elif(result=='\u2681'):
        label3=tkinter.Label(window,text='You rolled a two!',fg = 'grey', font=('arial',15,'bold'))
        label3.place(x=200,y=500)
    elif(result=='\u2682'):
        label3=tkinter.Label(window,text='You rolled a three!',fg = 'grey',font=('arial',15,'bold'))
        label3.place(x=200,y=500)
    elif(result=='\u2683'):
        label3=tkinter.Label(window,text='You rolled a four!',fg = 'grey', font=('arial',15,'bold'))
        label3.place(x=200,y=500)
    elif(result=='\u2684'):
        label3=tkinter.Label(window,text='You rolled a five!',fg = 'grey', font=('arial',15,'bold'))
        label3.place(x=200,y=500)
    elif(result=='\u2685'):
        label3=tkinter.Label(window,text='You rolled a six!',fg = 'grey',font=('arial',15,'bold'))
        label3.place(x=200,y=500)


# play button
button = tkinter.Button(window, text='roll dice', font=('arial',12), command=roll_dice)
button.pack()

# create exit
def close():
   window.quit()

# exit button
exit= tkinter.Button(window, text= 'exit', font=('arial',12), command=close).pack()

window.mainloop()