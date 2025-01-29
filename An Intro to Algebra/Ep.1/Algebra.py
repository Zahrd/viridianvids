from manim import *
from itertools import product
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService
import manimpango, math
#manimpango is for fonts (later)
class Algebra(VoiceoverScene):
    def construct(self):
        self.camera.background_color = "#ece6e2"
        Text.set_default(color=BLACK)
        MathTex.set_default(color=BLACK)
        self.set_speech_service(GTTSService()) #switch with RecorderService() or smth later
        
        def waitScript(script, self=self):
            with self.voiceover(text=script) as tracker: self.wait(tracker.duration)
        
        def playScript(script, *args, timing=False, self=self, **kwargs): #timing==0 -> follow script, other -> run_time=timing
            if timing == True:
                with self.voiceover(text=script) as tracker: self.play(*args, **kwargs, run_time=tracker.duration)
            else:
                with self.voiceover(text=script): self.play(*args, **kwargs)
        
        skips = dict({
            "Intro": 0,
            "Preface": 0,
            "Definition": 0,
            "Motivation": 0,
            "Transcription": 0,
            "FutureExample": 0,
            "FinalRemarks": 0,
            })
        
        def Section(name, self=self, skips=skips):
            self.next_section(name,skip_animations=skips[name])
        
        
        
        Section("Intro")
        
        introGroup = Group()
        introText = Text("What is Algebra", font_size=80)
        whatKiller = Cross(introText[0:4])
        introTextPlus = Text("Why", font_size=80).next_to(introText[0:4], DOWN)
        introGroup.add(introText, whatKiller, introTextPlus)
        
        waitScript("Everyone always says")
        self.wait(0.2)
        playScript("What is Algebra? How do I use it?", Write(introText))
        waitScript("But no one asks:")
        self.wait(0.2)
        playScript("Why is Algebra? What does it really mean?", [Create(whatKiller),Write(introTextPlus)])
        self.wait(0.6)
        self.play(FadeOut(introGroup))
        
        
        
        Section("Preface")
        
        ex1 = MathTex(r"y=mx+b").shift(2*LEFT + 0.08*DOWN) #idk why i have to do this
        ex2 = MathTex(r"a^2+b^2=c^2").shift(2*RIGHT)
        ex3 = MathTex(r"5x+3=-7").shift(DOWN)
        exVars = [ex1[0][0], ex1[0][2], ex1[0][3], ex1[0][5], 
                  ex2[0][0], ex2[0][3], ex2[0][6], ex3[0][1]]
        questionMark = Text("?", font_size=120).shift(1.21*UR+1.4*RIGHT).rotate(-TAU/26)
        exGroup = Group(ex1, ex2, ex3)
        playScript("Maybe you've seen some Algebra before, and wondered", *[Write(i) for i in exGroup])
        self.play(Write(questionMark))
        playScript("why?", Wiggle(questionMark))
        playScript("Why are there letters? What are these symbols?", *[Circumscribe(i, color=BLUE, time_width=0.15) for i in exVars], timing=True)
        playScript("Or even if you haven't, that's completely okay. This series of videos will focus on the intuitions behind Algebra, and why everything is the way it is.",
                   Succession(*[ApplyWave(i) for i in exGroup]))
        exGroup.add(questionMark)
        self.play(*[Unwrite(i) for i in exGroup])
        self.wait(2)
        
        
        Section("Definition")
        
        definitionGroup = Group()
        defAlgebra = Text("Algebra")
        defArrow = MathTex(r"\Downarrow")
        defTheDef = Text("\"Reunion of Broken Parts\"") #good var naming
        defTheUnknown = Text("Unknown")
        definitionGroup.add(defAlgebra, defArrow, defTheDef).arrange(DOWN)
        defTheDef.shift(0.2*DOWN) #hmm
        defUnderline = Underline(defTheDef, color=BLACK, stroke_width=1.5)
        
        playScript("Perhaps we can start from the", FadeIn(defAlgebra))
        playScript("actual name", FocusOn(defAlgebra))
        waitScript("Algebra actually comes from Arabic")
        playScript("and it means", Write(defArrow))
        playScript("the reunion of broken parts", Write(defTheDef))
        self.play(Create(defUnderline))
        self.wait(1)
        self.play(FadeOut(definitionGroup), Uncreate(defUnderline))
        playScript("It comes up when we want to find", Write(defTheUnknown))
        playScript("the unknown.", ShowPassingFlash(defTheUnknown)) #cursed
        self.remove(defTheUnknown) #this is a useful line
        self.wait(1)
        
        
        
        Section("Motivation")
        
        pencilProb = Paragraph("Imagine you go to use the bathroom,  but when you come back,",
                            "you see your friend with two pencils in their hand.",
                            "You look back at your pile of pencils and you only see one left.",
                            "How many pencils did you originally have?",
                            font_size=35, alignment="center", line_spacing=1)
        pencilImg = ImageMobject("pencil.png")
        pencilVar =  pencilImg
        pencilQuestionMark = Text("?", font_size=144)
        
        pencilArr = Group(
            *[pencilVar.copy().to_corner(UL).shift(i*DOWN + (j+0.125)*RIGHT + 0.25*UL*math.sqrt(2))
            for i,j in product(range(8),range(14))]
        )
        pencilArr.remove(pencilArr[48],pencilArr[49],pencilArr[62],pencilArr[63])
        pencilVar.scale(2.5)
        
        defAlgebra.move_to([0,0,0])
        
        waitScript("But I think I'll just try to show you with an example:")
        self.wait(0.5)
        playScript("""Imagine you go to use the bathroom, but when you come back, you see your friend with two pencils in their hand. 
                    You look back at your pile of pencils and you only see one left. """,
                    Succession(*[FadeIn(pencilProb[i]) for i in range(0,3)]), timing=True)
        waitScript("You try to think, but forget:")
        playScript("how many pencils did you originally have?", FadeIn(pencilProb[3]), timing=True)
        self.wait(3.5)
        self.play(FadeOut(pencilProb))
        waitScript("This sounds like a simple problem. But instead of trying to do it in our heads,")
        playScript("let's use", FadeIn(defAlgebra))
        playScript("Algebra", ShowPassingFlash(Underline(defAlgebra, color=BLUE), time_width=0.2))
        self.wait(2)
        self.play(FadeOut(defAlgebra))
        playScript("Let's use a picture of the number of pencils we had like this.", FadeIn(pencilVar))
        playScript("We can think of this as some number that we currently don't know:", FadeOut(pencilVar), FadeIn(pencilQuestionMark))
        playScript("It could be 1 pencil,", FadeIn(pencilArr[0]))
        playScript("4 pencils", *[FadeIn(pencilArr[i]) for i in range(1,4)])
        self.wait(0.7)
        playScript("or even 1000!", Succession(*[FadeIn(pencilArr[i]) for i in range(4,len(pencilArr))], run_time=4))
        self.wait(1)
        self.play(FadeOut(pencilArr, pencilQuestionMark), FadeIn(pencilVar))
        
        
        
        Section("Transcription")
        
        pencilEqR = MathTex(r"-2=1", font_size=144).move_to(0.9*RIGHT) #R = right side
        pencilEq = Group()
        pencilMegaGroup = Group()
        pencilEq.add(pencilVar, pencilEqR)
        pencilMegaGroup.add(pencilProb, pencilEq)
        
        waitScript("Anyways, we know that our friend took 2 of them.")
        waitScript("So that means that our number of pencils got")
        playScript("subtracted by 2.", pencilVar.animate.shift(2.2*LEFT), Write(pencilEqR[0][0:2]))
        self.wait(0.2)
        waitScript("And lastly, we know that we saw")
        playScript("1 pencil when we got back from the bathroom.", Write(pencilEqR[0][3]))
        waitScript("That's why we can say that")
        playScript("this", Succession(Circumscribe(pencilEqR[0][0:2], color=BLUE, buff=0.4), FadeIn(pencilEqR[0][2])))
        playScript("is equal", Wiggle(pencilEqR[0][2]))
        playScript("to this.", Indicate(pencilEqR[0][3], color=BLUE))
        self.play(pencilEq.animate.center())
        self.wait(2)
        playScript("So we can write our equation like this. Overall, ", Circumscribe(pencilEq, color=BLUE, buff=0.5), timing=True)
        playScript("the number of pencils we had was subtracted by two", Circumscribe(pencilVar, color=BLUE, buff=0.4))
        playScript("represented by this minus two", Circumscribe(pencilEqR[0][0:2], color=BLUE, buff=0.4), timing=True)
        waitScript("and now, this is")
        playScript("equal to 1 pencil remaining.", Circumscribe(pencilEqR[0][2:4], color=BLUE, buff=0.4), timing=True)
        self.wait(1)
        waitScript("Think for a moment and try to understand")
        playScript("how we converted our word problem into Algebra.", FadeIn(pencilProb), pencilMegaGroup.animate.arrange(DOWN))
        waitScript("Really, try and pause the video to contemplate.")
        self.wait(2)
        waitScript("Now, I know this doesn't seem like a lot, and it really isn't.")
        self.play(FadeOut(pencilProb), pencilEq.animate.center())
        waitScript("But the beauty with Algebra is that we can use it")
        playScript("to solve problems like this:", FadeOut(pencilEq))
        self.wait(1.5)
        
        
        Section("FutureExample")
        
        siblingWordProblem = Paragraph(
        "Lukas and Anna are siblings.",
        "Lukas is 3 years old.",
        "Anna is 16 years old.",
        "How old will they be when",
        "Anna is twice as old as Lukas?",
        alignment="center", line_spacing=1.2)
        
        playScript("""Lukas and Anna are siblings.
        Lukas is 3 years old.
        Anna is 16 years old.
        How old will they be when
        Anna is twice as old as Lukas?""", Write(siblingWordProblem), timing=True)
        waitScript("""Really take a look at it, and pause the video if you want to try it out yourself.
                        If you try to guess, finding the answer might take a long time!
                        Yet, we can methodically and easily solve it using algebra.
                        Think of it as a sneak peek for what's to come.""")
        self.play(FadeOut(siblingWordProblem))
        self.wait(2)
        
        
        Section("FinalRemarks")
        
        pencilP = MathTex("p", font_size=144).move_to(pencilVar).shift(0.35*DR+0.1*LEFT)
        
        playScript("Now, back to our equation, there's one last thing I want to quickly address:", FadeIn(pencilEq))
        playScript("In our equation, we used a picture of a pencil to show how many pencils we had in the first place.", FocusOn(pencilVar))
        waitScript("But a little secret I'll tell you right now is that mathematicians are lazy.")
        waitScript("We wouldn't want to draw pictures every single time we did math,")
        playScript("so let's use a letter instead like this.", FadeOut(pencilVar), FadeIn(pencilP))
        waitScript("I think p makes the most sense,")
        playScript("because p can stand for pencils - the amount of pencils we had.", Indicate(pencilP, color=BLUE))
        
        waitScript("Finally, the last thing I want to touch on is the significance of")
        playScript("this equals sign.", Circumscribe(pencilEqR[0][2:3], color=BLUE, buff=0.4))
        self.wait(1)
        playScript("Algebra is all about trying to put back together broken parts, which can be hard - I mean, think about trying to put back together a broken window!", 
                   Succession(FadeOut(pencilEqR, pencilP), FadeIn(definitionGroup.arrange(DOWN))))
        playScript("That's why we're going to be using", Succession(FadeOut(definitionGroup), FadeIn(pencilP, pencilEqR)))
        playScript("this, as much as we can.", FocusOn(pencilEqR[0][2:3]), FadeToColor(pencilEqR[0][2:3], color=BLUE))
        self.wait(0.5)
        self.play(FadeToColor(pencilEqR[0][2:3], color=BLACK))
        waitScript("Later, we'll delve into how exactly we can do that, but I hope this served as a little intro into the wonderful world of Algebra.")
        self.wait(2)



"""
draft

What is Algebra -> Why is Algebra

Comes from Arabic, meaning 'reunion of broken parts'

Start with example:

Imagine you go to use the bathroom, but when you come back, you see your friend with two pencils in their hand. You look back at your pile and you only see one left. You try to think, but forget: how many pencils did you have originally have
Can be easy w/ just add, but we can use algebra
Would be represented like: [anim] {explain}

Doesn't seem like much but can do problems like this [anim] 
    (Lukas and Anna are siblings. Lukas 3yo and Anna 16yo. How old will they be when Anna is double Lukas' age)
If try to guess, get nowhere, but *algebra* can solve - but later

Back to example: can write with equation
3 - (pencil drawing) = 1


Mathmeticians lazy so use letter


Algebra is all about equals sign
In future vids: how to navigate around it


"""