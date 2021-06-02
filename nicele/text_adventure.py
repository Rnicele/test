from tkinter import*
import tkinter.font as tkFont


root = Tk()
frame = Frame(root)
frame.pack()


titleFont = tkFont.Font(family='Helvetica',size=20, weight='bold')
subjectFont = tkFont.Font(family='Helvetica',size=12, weight='bold')
introFont = tkFont.Font(family='Helvetica',size=11, weight='normal')
canvas_width = 600
canvas_height = 440
w = canvas_width // 2
h = canvas_height // 2

class RedRidingHood:
    global p1ca, p1cb, p2aca, p2acb, p2acc, p2bca, p2bcb

    def __init__(self):
        pass


    def start(self):
        introduction = '''
            Once upon a time,

            There's a little girl called 'Red riding hood' because of her red hood. 
            She always go to her Grandmother's house in the middle of the woods.

            One day, 
            Red riding hood's mother called her and told her that her Grandmother is sick
            and she needs to deliver some medicine and food in the basket in 
            her Grandmother's house.

            She gets her red hood, wear it and said goodbye to her mother,
            but before leaving, her mother told her 
            "Remember, don't talk to strangers".

            She took the wood's path to go to her Grandmother easily.

            She saw some beautiful flowers while walking and think that her Grandmother
            might like it, so she pick some flowers.

            after picking the flower, someone talked behind her and she saw a big wolf.
        '''

        # print(introduction)

        # root = Tk()
        

        canvas = Canvas(root, width=canvas_width, height=canvas_height)
        canvas.pack()   

        r1 = canvas.create_rectangle(30, 30, canvas_width-30, canvas_height, fill='red')
        title = canvas.create_text(w, 50, text="RED RIDING HOOD", fill='white', font=titleFont)
        intro = canvas.create_text(w-30, h+30, text=introduction, fill='white', justify='center', font=introFont)

        self.create_button_p1()

        answer = input("Pick your answer: ")
        print(answer)


    def create_button_p1(self):

        self.p1ca = Button(root, text="A. Run from the big wolf",)
        self.p1ca.bind('<Button-1>', self.p1Choice_a)
        self.p1ca.pack(side = LEFT,padx=30, pady=30, fill = BOTH, expand = True)

        self.p1cb = Button(root, text="B. Have a conversation with the big wolf")
        self.p1cb.bind('<Button-1>', self.p1Choice_b)
        self.p1cb.pack( side = RIGHT,padx=30, pady=30, fill = BOTH, expand = True)


    def p1Choice_a(self, event):
        print("You choose to run from the big wolf")
        print('hide me')
        self.p1ca.pack_forget() # Hide p1ca
        self.p1cb.pack_forget() # Hide p1cb

        canvas = Canvas(root, width=canvas_width, height=h/2)
        canvas.pack() 
        
        SecondIntro = '''
            "A stranger! Mom says don't talk to strangers." as Red riding hood thinks, 
            she run.
        '''
        r2 = canvas.create_rectangle(30, 30, canvas_width-30, h/2, fill='yellow')
        title = canvas.create_text(w+20, 40, text="You choose to run from the big wolf", fill='black', font=subjectFont, anchor=NE)
        intro = canvas.create_text(w-30, 80, text=SecondIntro, fill='black', justify='center', font=introFont)

        self.create_button_p2a()

    
    def p1Choice_b(self, event):
        print("You choose to talk the big wolf")
        print('hide me')
        self.p1cb.pack_forget() # Hide p1cb
        self.p1ca.pack_forget() # Hide p1ca

        canvas = Canvas(root, width=canvas_width, height=h/2)
        canvas.pack() 
        
        SecondIntro = '''
            "Where are you going on a fine day?" 
            asked by big wolf
        '''
        r2 = canvas.create_rectangle(30, 30, canvas_width-30, h/2, fill='yellow')
        title = canvas.create_text(w-20, 40, text="You choose to talk the big wolf", fill='black', font=subjectFont, anchor=NE)
        intro = canvas.create_text(w-30, 80, text=SecondIntro, fill='black', justify='center', font=introFont)

        self.create_button_p2b()

    
    def create_button_p2a(self):
        self.p2aca = Button(root, text="A. Run to the village and look for a hunter",)
        self.p2aca.bind('<Button-1>', self.p2aChoice_a)
        self.p2aca.pack(side = TOP,pady=5)

        self.p2acb = Button(root, text="B. Run back to their house and hide")
        self.p2acb.bind('<Button-1>', self.p2aChoice_b)
        self.p2acb.pack( side = TOP,pady=5)
        
        self.p2ccb = Button(root, text="C. Run to her grandma's house")
        self.p2ccb.bind('<Button-1>', self.p2aChoice_c)
        self.p2ccb.pack( side = TOP,pady=5)


    def p2aChoice_a(self,event):
        print("You choose to run to the village and look for a hunter")
        print('hide me')
        self.p2aca.pack_forget()
        self.p2acb.pack_forget() 
        self.p2ccb.pack_forget() 

    
    def p2aChoice_b(self,event):
        print("You choose to run back to their house and hide")
        print('hide me')
        self.p2aca.pack_forget()
        self.p2acb.pack_forget() 
        self.p2ccb.pack_forget() 


    def p2aChoice_c(self,event):
        print("You choose to run to her grandma's house")
        print('hide me')
        self.p2aca.pack_forget()
        self.p2acb.pack_forget() 
        self.p2ccb.pack_forget() 

     
    def create_button_p2b(self):
        self.p2bca = Button(root, text="A. Told the big wolf about your Grandmother",)
        self.p2bca.bind('<Button-1>', self.p2bChoice_a)
        self.p2bca.pack(side = LEFT,padx=30, pady=30, fill = BOTH, expand = True)

        self.p2bcb = Button(root, text="B. Played with the big wolf")
        self.p2bcb.bind('<Button-1>', self.p2bChoice_b)
        self.p2bcb.pack( side = RIGHT,padx=30, pady=30, fill = BOTH, expand = True)

    
    def p2bChoice_a(self,event):
        print("You choose to tell the big wolf about your Grandmother")
        print('hide me')
        self.p2bca.pack_forget() # Hide p1cb
        self.p2bcb.pack_forget() # Hide p1ca

        canvas = Canvas(root, width=canvas_width, height=h/2+80)
        canvas.pack() 
        
        SecondIntro = '''
            "I'm going to my grandma's house. She isn't feeling very well,
            so I'm bringing her this food basket and these flowers." 
            said Little red riding hood

            "what a sweet girl you are" said the big wolf

            "i had better be going. Goodbye, Mr. wolf!" 
        '''
        r2 = canvas.create_rectangle(30, 30, canvas_width-30, h+80, fill='purple')
        title = canvas.create_text(canvas_width-130, 40, text="You choose to tell the big wolf about your Grandmother", fill='white', font=subjectFont, anchor=NE)
        intro = canvas.create_text(w-30, 120, text=SecondIntro, fill='white', justify='center', font=introFont)


    def p2bChoice_b(self,event):
        print("You choose to play with the big wolf")
        print('hide me')
        self.p2bca.pack_forget() # Hide p1cb
        self.p2bcb.pack_forget() # Hide p1ca

        canvas = Canvas(root, width=canvas_width, height=h/2+80)
        canvas.pack() 
        
        SecondIntro = '''
            "I'm going into the center of the woods.
            How about you Mr. Wolf? Where are you going?" said Little red riding hood

            "I'm also going into the woods and will play there.
            Do you want to play with me?" asked by the big wolf

            "Sure! Let's go play!"
        '''

        r2 = canvas.create_rectangle(30, 30, canvas_width-30, h+80, fill='purple')
        title = canvas.create_text(canvas_width-130, 40, text="You choose to play with the big wolf", fill='white', font=subjectFont, anchor=NE)
        intro = canvas.create_text(w-30, 120, text=SecondIntro, fill='white', justify='center', font=introFont)

        print("YOU LOSE. RED RIDING HOOD GOT EATEN BY THE BIG WOLF")


rrhStart = RedRidingHood()
rrhStart.start()