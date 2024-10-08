import random
import sys
import time
# copy 1 - 50 for average tests
stocks = ["lemonade stand","thiefs","activism","books","drug dealers","sea travel","birth control","happiness","tourism","assasins","prisons","guns","poopsi","cooky cola","vaccines","birth rate","death rate","cars","renewable energy","corruption","AI","food","nuclear weapons","illumanti","weapon dealers","government","coal","gas","oil","rich people"]
stockowned = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
stockprice = [50,100,200,500,600,700,800,1000,1500,2000,3000,4000,5000,5000,7000,8000,8000,10000,15000,20000,25000,30000,40000,45000,50000,60000,70000,75000,80000,100000]
hunger = random.randint(2, 4)
exercise = random.randint(1,2)
health = random.randint(80,100)
onloan = 0
setrate = 0
dorwhold = 0
loanamount = 0
stockchosen = 0
sleeptime = 0
numhold2 = 0
i = 0
usethis = 0
death = 0
alarm = 0
alive = 1
numhold3 = 0
answerhold = "a"
eatchoice = "a"
sleepamount = 0
checkupend = 1
exercisetotal = 0
attentionspan = random.randint(1,2)
charisma = random.randint(1,20)
fear = random.randint(1,5)
sleep = random.randint(8,12)
sleepiness = random.randint(0,5)
deathchance = random.randint(0,10)
lovetimer = -1
wakechance = 0
wake = 0
loanowe = 0
cash = 100
exercisecounter = 0
sleepcounter = 0
eatcounter = 0
numhold = 0
maxsleep = 0
monthdays = [31,28,31,30,31,30,31,31,30,31,30,31]
rizz = ["'did you know elden ring is getting a dlc'","'do you like anime'","'can i have your number'creepily","'wanna go out sometime'","'do you wanna be my fortnite duo'","'i have alot of money in my bank account right now'","'want to be my fortnite trio'","'if you were an angle you would be acute one'","'can i have your number'with a confidence of a god","nothing you just look at her and she falls to her knees and begs you to go out with her "]
dreamselect = ["you just stabbed your teacher its a murder mystery"," you are naked in art school ill let you paint the picture","your in a clown car waving to the audience","you are falling from the sky watch the planes fly by","you are in a field but all the flowers are people"," you started a buisness your a zillionare X Æ A-12","your hanging from a building your spiderman"," you cant stop falling","a meteor is coming you need to run","your entire family shot by a gun"]
minutes = random.randint(0,59)
hour = random.randint(6,18)
day = random.randint(1,6)
week = random.randint(1,3)
month = random.randint(1,12)
year = random.randint(2000,2030)


   
sleepinesslist = ['you are currently very awake', 'you are currently very awake', 'you are currently decently awake', 'you are currently a tad tired be careful on the roads', 'you are currently rather tired be careful on the roads','you are very tired avoid the roads']
# make sure to # line 9 - 14 if playing and 42 - print(f"Hunger: {hunger}")
print(f"Exercise: {exercise}")
print(f"Attention Span: {attentionspan}")
print(f"Charisma: {charisma}")
print(f"Fear: {fear}")
print(f"Sleep: {sleep}")
print(f"sleepiness: {sleepiness}")
def adjustvalue():
    global health
    global charisma
    while health > 100:
        health = health - 1
    while charisma > 20:
        charisma = charisma - 1
    while charisma < 1:
        charisma = charisma + 1
   
   
   
   
def adjusttime(minutes, hour, day, week, month, year):
    global health  # Declare health as global to modify the global variable within the function
    global deathchance
    global sleepcounter
    global charisma
    global sleepiness
    global cash
    global loanamount
    global loanowe
   
   
   
    if minutes >= 60:
        minutes = minutes - 60
        hour = hour + 1
       
    if hour >= 24:
        hour = hour - 24
        i = 1
        while i <= 30:
            numhold = random.randint(-5,5)
            stockprice[i - 1] = ((stockprice[i - 1]*((numhold/100)+1)//0.001))/1000 + 0.001
            i = i + 1
        cash = (cash//0.001)/1000 + 0.001
        loanamount = (loanamount//0.001)/1000 + 0.001
        loanowe = (loanowe//0.001)/1000 + 0.001
        if loanowe <= 0:
            onloan = 0
            loanowe = 0
        if exercise >= exercisecounter:
            health = health - (exercise - exercisecounter)*5
            charisma = charisma - (exercise - exercisecounter)
        health = health - (sleep - sleepcounter)
        if sleep < sleepcounter:
            sleepiness = sleepiness - 1
            if sleepiness < 0:
                sleepiness = sleepiness + 1
        elif sleep > sleepcounter:
            sleepiness = sleepiness + 1
            if sleepiness > 5:
                sleepiness = sleepiness - 1
       
       
       
        deathchance = ((100 - health) // 10)
        numhold = random.randint(1,100)
        if numhold < deathchance//2:
            time.sleep(3)
            print("there is a feeling in your chest")
            time.sleep(2)
            print("is it love?")
            time.sleep(2)
            print("no its a heart attack")
            quit()
        sleepcounter = 0
        day = day + 1
    if day >= 7:
        day = day - 7
        week = week + 1
    if week >= 4:
        if 28 + day > monthdays[month - 1]:# Assuming a month is 4 weeks for simplicity
            week = week - 4
            day = 1
            month = month + 1
            if cash < 0:
                print("uh oh your poor and die")
                quit()
       
       
            loanowe = loanowe + loanowe * ((55 - ((setrate+1)//2)*5)/100)
            numhold = loanowe
            loanowe = 9*(loanowe//10)
            setloan = numhold - loanowe
            cash = cash - setloan
            if loanowe <= 0:
                onloan = 0
            if loanamount < 0:
                cash = cash + loanamount
    if month >= 13:
        month = month - 12
        year = year + 1
    adjustvalue()
    return minutes, hour, day, week, month, year

minutes, hour, day, week, month, year = adjusttime(minutes, hour, day, week, month, year)

#print("Minutes:", minutes)
#print("Hour:", hour)
#print("Day:", day)
#print("Week:", week)
#print("Month:", month)
#print("year:",year)
#print("its",str((week*7)+day)+"/"+str(month)+"/"+str(year))

print("Hello investor! What should I call you?")
UserName = input()
print("So",UserName,"you have 100 pounds to your name. Try to increase that to a million.")
chosen = 1
alive = 1
while alive == 1:
    print("its",str((week*7)+day)+"/"+str(month)+"/"+str(year))
    print("it is now",str(hour)+":"+str(minutes))
    print("you currently have a £"+str(loanamount),"loan and owe the bank £"+str(loanowe))
    print("Choose an option:")
    print("------------------")
    print("A - Watch the news")
    print("------------------")
    print("B - Go to the investing page")
    print("----------------------------")
    print("C - Go to health improvement")
    print("----------------------------")
    print("D - Go to bank")
    print("--------------")
    print("E - Check your balance")
    print("----------------------")

    place = input().lower()
    chosen = 1
    if place == "a":
        print("You chose option A.")
        hour = hour + 23
        minutes, hour, day, week, month, year = adjusttime(minutes, hour, day, week, month, year)
        chosen = 0
    elif place == "b":
        numhold = 0
        numhold2 = 0
        numhold3 = 0
        i = 1
        answerhold = input("do you want to\nA-buy stocks\nB-sell stocks")
        if answerhold == "a":
            while i <= 30:
                if stockprice[i-1] <= loanamount+cash:
                    print(str(i)+")"+str(stocks[i - 1])+"--"+str(stockprice[i-1])+"-you own",str(stockowned[i-1]),"of this stock")
                i = i + 1
            numhold = int(input("type the number of the stock you wish to buy"))
            if stockprice[numhold-1] > (cash+loanamount):
                print("not enough money for that bucko")
                time.sleep(2)
                minutes = minutes + 10
                minutes, hour, day, week, month, year = adjusttime(minutes, hour, day, week, month, year)
            else:
                numhold2 = int(input("how many do you want to buy"))
                if isinstance(numhold2, int) == "false":
                    print("not an integer buddy")
                    time.sleep(2)
                    minutes = minutes + 10
                    minutes, hour, day, week, month, year = adjusttime(minutes, hour, day, week, month, year)
                else:
                    numhold3 = numhold2*stockprice[numhold-1]
                    if numhold3 > cash+loanamount:
                        print("not enough money for that back to the start with 10 mins wasted")
                        time.sleep(2)
                        minutes = minutes + 10
                        minutes, hour, day, week, month, year = adjusttime(minutes, hour, day, week, month, year)
                    else:
                        if (numhold3 > cash) and (numhold3 > loanamount):
                            numhold3 = numhold3 - loanamount
                            loanamount = 0
                            cash = cash - numhold3
                            stockowned[numhold - 1] = stockowned[numhold - 1] + numhold2
                        elif numhold3 > cash:
                            loanamount = loanamount - numhold3
                            stockowned[numhold - 1] = stockowned[numhold - 1] + numhold2
                        elif numhold3 > loanamount:
                            cash = cash - numhold3
                            stockowned[numhold - 1] = stockowned[numhold - 1] + numhold2
                        else:
                            answerhold = input("do you want to pay with cash or loan")
                            if answerhold == cash:
                                cash = cash - numhold3
                                stockowned[numhold - 1] = stockowned[numhold - 1] + numhold2
                            else:
                                loanamount = loanamount - numhold3
                                stockowned[numhold - 1] = stockowned[numhold - 1] + numhold2
                        time.sleep(1)
                        print("you now own",str(stockowned[numhold - 1]),str(stocks[numhold - 1]),"stocks")
                        time.sleep(2)
                        minutes = minutes + 30
                        minutes, hour, day, week, month, year = adjusttime(minutes, hour, day, week, month, year)
        if answerhold == "b":
            numhold = 0
            while i <= 30:
                if stockowned[i-1] > 0:
                    print(str(i)+")"+str(stocks[i - 1])+"--"+str(stockprice[i-1])+"-you own",str(stockowned[i-1]),"of this stock")
                    numhold = numhold + 1
                i = i + 1
            if numhold == 0:
                print("you dont own any stocks")
                minutes = minutes + 10
                minutes, hour, day, week, month, year = adjusttime(minutes, hour, day, week, month, year)
            else:
                numhold = int(input("type the number of the stock you wish to sell"))
                if stockowned[numhold - 1] == 0:
                    print(stocks[numhold+1])
                    print(stockowned[numhold +1])
                    print("you dont have any of that stock buddy")
                    minutes = minutes + 10
                    minutes, hour, day, week, month, year = adjusttime(minutes, hour, day, week, month, year)
                else:
                    print("how many do you want to sell(maximum",str(stockowned[numhold - 1]),"at the price of",str(stockprice[numhold - 1])+")")
                    numhold2 = int(input())
                    if numhold2 > stockowned[numhold - 1]:
                        print("you dont have that many")
                        minutes = minutes + 10
                        minutes, hour, day, week, month, year = adjusttime(minutes, hour, day, week, month, year)
                    else:
                        numhold3 = numhold2*stockprice[numhold-1]
                        cash = cash + numhold3
                        print("added £"+str(numhold3),"to your cash")
                   
           
           
               
                           
                       
                       
                   
           
           
        chosen = 0
    elif place == "c":
        chosen = 0
        print("You chose option C.")
#health section        
       
        print("Choose an option:")
        print("A - have a check up")
        print("B - exercise (1 hours)("+str(exercisecounter)+"/"+str(exercise)+")")
        print("C - sleep ("+str(sleepcounter)+"/"+str(sleep)," hours)")
        print("D - eat ("+str(eatcounter)+"/"+str(hunger)+")")

        option = input().lower()

        if option == "a":
            print("You chose option A - have a check up (1 hour).")
            while checkupend == 1:
                print("choose an option")
                print("A drive to the doctors")
                print("B walk to the doctors")
               
                optioncheckup = input().lower()

                   
                if optioncheckup == "a":
                    print("you get into the car")
                    50
                    crashchance = sleepiness*2
                    crash = random.randint(1,100)
                    print(crash)
                    if crash <= crashchance:
                        print("you drift of slightly as you round a corner and slam into incoming traffic")
                        print("you die")
                        sys.exit
                       
                    #death
                    else:
                        print("you drove to the doctors it took",25 + (5*attentionspan),"minutes")
                        time.sleep(2)
                        minutes = minutes + 25 + (5*attentionspan)
                        minutes, hour, day, week, month, year = adjusttime(minutes, hour, day, week, month, year)
                        time.sleep(2)
                        dorwhold = 1
                        checkupend = 0

                   
                elif optioncheckup == "b":
                    print("you walk to the doctors")
                    print("it takes",40 + (5*exercise) + (5*attentionspan),"minutes")
                    minutes, hour, day, week, month, year = adjusttime(minutes, hour, day, week, month, year)
                    time.sleep(2)
                    dorwhold = 0
                    checkupend = 0
                else:
                    print("not an option")
            else:
                print("the doctor says:")
                time.sleep(1)
                print("you are quite healthy with a score of",str(health)+"/100")
                time.sleep(1)
                print("you will need to eat",hunger,"times a day ")
                time.sleep(1)
                print(sleepinesslist[sleepiness],"but it seems you will need to sleep",sleep,"hours mininum")
                time.sleep(2)
                if attentionspan == 2:
                    print("your attention span is also pretty bad so it will take a bit longer to do stuff")
                    time.sleep(1)
                print("you will need to exercise",exercise,"times a day")
                time.sleep(1)
                if charisma >= 11:
                    print("the doctor gazes into your eyes like you have a rizzsma stat of",charisma,)
                else:
                    print("the doctor trys to avoid eye contact like your someone with a charisma score of",charisma,)
                time.sleep(2)
#chekup exit choice
                checkupend = 1
                while checkupend == 1:
                    print("do you want medicine (y/n)")
                   
                    optioncheckup = input().lower()
                   
                    if optioncheckup == "y":
                        print("this will be available in the future")
#fix this later
                        break
                    elif optioncheckup == "n":
                        time.sleep(1)
                        print("oh")
                        time.sleep(1)
                        print("ok")
                        time.sleep(1)
                   
                    else:
                        print("not an option")
                    if dorwhold == 1:
                        print("you drive back home")
                        25 + (5*attentionspan)
                    elif dorwhold == 0:
                        print("you walk back home")
                   
           
        elif option == "b":
            print("you chose B - exercise (1 hours)("+str(exercisecounter)+"/"+str(exercise)+")")
            time.sleep(1)
            death = random.randint(0,100)
            if death <= deathchance:
                print("uh oh heart attack you die")
                sys.exit
                quit()
            else:
                print("you have a great jog")
                print("you feel the health benefits flow through you")
                time.sleep(1)
                health = health + 3
                while health > 100:
                    health = health - 1
                charisma = charisma + 1
                while charisma > 20:
                    charisma = charisma - 1
                print("it took you",str(5*attentionspan),"extra minutes due to your ATTENTION SPAN")
                time.sleep(1)
                hour = hour + 1
                minutes, hour, day, week, month, year = adjusttime(minutes, hour, day, week, month, year)
                minutes = minutes + 5*attentionspan
                minutes, hour, day, week, month, year = adjusttime(minutes, hour, day, week, month, year)
                exercisecounter = exercisecounter + 1
                exercisetotal = exercisetotal + 1
                deathchance = deathchance - 1
           
        elif option == "c":
            if hour < 18:
                print("not sleepy enough\nget back to work blud")
                time.sleep(1)
            else:
                print("you chose option C - sleep ("+str(sleepcounter)+"/"+str(sleep)," hours)")
                time.sleep(1)
                digitaltime = str(hour)+":"+str(minutes)
                print("what should you set your alarm to (am),bearing in mind it is",digitaltime,"4 hours sleep minimum or there may be negative affects")
                alarm = int(input())
                print("you drift off into sleep")
                death = random.randint(0,100)
                if death <= deathchance:
                    print("wow look at the light you walk to it")
                    sys.exit()
                else:
                    if year == 2001 and month == 11 and day == 11:
                        print("you wake up your alarm didnt go off")
                        print("")
                    else:
                        sleepamount = random.randint(1,10)
                        time.sleep(1)
                        print("you feel a dream coming\n",dreamselect[sleepamount-1])
                        maxsleep = 24 - hour + alarm
                        sleeptime = random.randint(maxsleep - 1,maxsleep+1)
                        sleepcounter = sleeptime
                        hour = hour + sleeptime
                        minutes, hour, day, week, month, year = adjusttime(minutes, hour, day, week, month, year)
                        if sleeptime > maxsleep:
                            numhold = hour - alarm
                            time.sleep(1)
                            print("you awaken like a princess who has had their beauty-sleep")
                            time.sleep(1)
                            print("shoot you overslept by", numhold, "hours, your alpha grindset will be affected by this minute change in sleep schedule")
                            time.sleep(2)
                        elif sleeptime < maxsleep:
                            numhold = alarm - hour
                            time.sleep(1)
                            print("you rub your eyes still tired as you sit up")
                            time.sleep(1)
                            print("shoot you underslept by", numhold, "hours, guess you need to hop on the g-fuel")
                            time.sleep(2)
                        else:
                            time.sleep(1)
                            print("beep beep beep you are awake")
                            time.sleep(1)
                            print("yes your alpha grindset has kept you on schedule")
                            time.sleep(2)
                        sleeptime = 0
           
           
        elif option == "d":
            print("D - eat (0/"+str(hunger)+")")
            print("where do you want to go\nA-mcdonalds   £8,1/10 health score,"+str(6 + attentionspan*2),"minutes eat time")
            print("B-homecook   £20,7/10 health score,"+str(55 + attentionspan*2),"minutes eat time")
            print("C-chinese    £30,8/10 health score,"+str(30 + attentionspan*2),"minutes eat time")
            print("D-wagyu beef £80,6/10 health score,"+str(48 + attentionspan*2),"minutes eat time")
            print("E-michelin meal")
            eatcounter = eatcounter + 1
            eatchoice = input()
           
            if eatchoice == "a":
                print("you chomp down on a glorius fillet o fish(yeah your THAT guy)")
                time.sleep(1)
                health = health - 5
                if onloan == 1:
                    answerhold = input("do you want to pay with cash or use the money from your loan(cash/loan)")
                    if answerhold == "loan":
                        if loanamount < 7:
                            print("you dont have enough in your loan so it has been subtracted from your cash")
                            cash = cash - 7
                        else:
                            loanamount = loanamount - 7
                    else:
                        cash = cash - 7
                else:
                    cash = cash - 7
                minutes = minutes + 6 + attentionspan*2
                charisma = charisma - 1
                if charisma == 0:
                    charisma = charisma + 1
                minutes, hour, day, week, month, year = adjusttime(minutes, hour, day, week, month, year)
            elif eatchoice == "b":
                health = health + 2
                if onloan == 1:
                    answerhold = input("do you want to pay with cash or subtract the money from your loan(cash/loan)")
                    if answerhold == "loan":
                        if loanamount < 20:
                            print("you dont have enough in your loan so it has been subtracted from your cash")
                            cash = cash - 20
                        else:
                            loanamount = loanamount - 20
                    else:
                        cash = cash - 20
                else:
                    cash = cash - 20
                minutes = minutes + 55 + attentionspan*2
                print("you settle down for a long session of cooking")
                time.sleep(2)
                print("you boil water to the perfect tempreture")
                time.sleep(2)
                print("you open the lid pouring the stream of water in")
                time.sleep(2)
                print("the steam rises as the instant ramen floats to the top")
                time.sleep(2)
                print("you slurp them down sorta looking like cuthulu about halfway through")
                minutes, hour, day, week, month, year = adjusttime(minutes, hour, day, week, month, year)
            elif eatchoice == "c":
                health = health + 3
                if onloan == 1:
                    answerhold = input("do you want to pay with cash or subtract the money from your loan(cash/loan)")
                    if answerhold == "loan":
                        if loanamount < 30:
                            print("you dont have enough in your loan so it has been subtracted from your cash")
                            cash = cash - 30
                        else:
                            loanamount = loanamount - 30
                    else:
                        cash = cash - 30
                else:
                    cash = cash - 30
                minutes = minutes + 30 + attentionspan*2
                minutes, hour, day, week, month, year = adjusttime(minutes, hour, day, week, month, year)
                print("you call your fav chinese place '胖子的食物' and place your order,the usual ")
                time.sleep(2)
                print("a knock on your door")
                time.sleep(2)
                print("you answer the door")
                time.sleep(2)
                print("its a cute girl holding your food")
                time.sleep(2)
                answerhold = input("would you like to puruse romantic relations")
                time.sleep(2)
                if answerhold == "no" and lovetimer > 0:
                    print("you wrench your self away from the woman take your food and eat the chicken nuggets you ordered which are very chinese")
                    time.sleep(2)
                elif answerhold == "no" and lovetimer <= 0:
                    print("you attempt to take the food but your deperation for conversation stops you")
                    time.sleep(2)
                   
                if lovetimer <= 0 or answerhold == "yes":
                   
                    lovetimer = 7
                    charisma = charisma - 1
                    print("you say",rizz[(charisma//2)])
                    time.sleep(3)
                    if charisma == 11:
                        print("she hits you on the head with your food")
                        time.sleep(2)
                        print("she grabs a knife from a draw")
                        time.sleep(2)
                        print("she grabs your neck")
                        time.sleep(2)
                        print("she says if you dont give her all your money she will slit you throat")
                        time.sleep(2)
                        answerhold = input("do you give her the money")
                        if answerhold == "yes":
                            print("you enter the password on you phone")
                            time.sleep(1.5)
                            print("0001")
                            time.sleep(1.5)
                            print("the number of people that love you")
                            time.sleep(1.5)
                            print("you send her all your money")
                            time.sleep(1.5)
                            cash = 8
                            print("lucky you keep 8 pounds in your sofa")
                            time.sleep(1.5)
                        else:
                            print("she runs the knife across your throat")
                            sys.exit
                            quit()
                    if charisma < 11:
                        print("she is disgusted by your attempt at romance and asks for financial compensation")
                        time.sleep(2)
                        numhold = int(input("what percentage of your money will you give her"))
                        if numhold < random.randint(3,15):
                             print(str(numhold)+"!"+str(numhold)+"! thats way to low for the amount of mental damage you have done")
                             print("she hits you on the head with your food")
                             time.sleep(2)
                             print("she grabs a knife from a draw")
                             time.sleep(2)
                             print("she grabs your neck")
                             time.sleep(2)
                             print("she says if you dont give her all your money she will slit you throat")
                             time.sleep(2)
                             answerhold = input("do you give her the money")
                             if answerhold == "yes":
                                 print("you enter the password on you phone")
                                 time.sleep(1.5)
                                 print("0001")
                                 time.sleep(1.5)
                                 print("the number of people that love you")
                                 time.sleep(1.5)
                                 print("you send her all your money")
                                 time.sleep(1.5)
                                 cash = 8
                                 print("lucky you keep 8 pounds in your sofa")
                                 time.sleep(1.5)
                         
                             else:
                                 print("she runs the knife across your throat")
                                 sys.exit
                                 quit()
                        else:
                             cash = cash - (cash//100)*numhold
                             print("she accepts the money and leaves")
                    elif charisma > 11:
                        print("she looks at you like your her saviour and begs to go out with you")
                        time.sleep(2)
                        print("but the sigma grind is to much you close the door and eat your food")
                        time.sleep(2)
            elif eatchoice == "d":
                if onloan == 1:
                    answerhold = input("do you want to pay with cash or subtract the money from your loan(cash/loan)")
                    if answerhold == "loan":
                        if loanamount < 80:
                            print("you dont have enough in your loan so it has been subtracted from your cash")
                            cash = cash - 80
                        else:
                            loanamount = loanamount - 80
                    else:
                        cash = cash - 80
                else:
                    cash = cash - 80
                health = health + 1
                minutes = minutes + 48 + attentionspan*2
                minutes, hour, day, week, month, year = adjusttime(minutes, hour, day, week, month, year)
                print("you go to your favourite japenese wagyu place '太った人のための食べ物'")
                time.sleep(2)
                print("the waiter secretly spits on your food as he brings it over")
                time.sleep(2)
                print("you gobble it down")
                time.sleep(2)
                print("yum yum")
                time.sleep(2)
                           
                   
               
               
               
               
           
           
           
        else:
            print("Invalid option. Please choose from A, B, C, or D.")
           
    elif place == "d":
        chosen = 0
        print("You chose option D.")
        numhold = 0
        while numhold == 0:
            print("do you \n A - Drive to the bank \n B - Walk to the bank")
            optioncheckup = input()
            if optioncheckup == "a":
                print("you get into the car")
                50
                crashchance = sleepiness*2
                crash = random.randint(1,100)
                print(crash)
                if crash <= crashchance:
                    print("you drift of slightly as you round a corner and slam into incoming traffic")
                    print("you die")
                    sys.exit
                    quit()
                #death
                else:
                    print("you drove to the bank it took",25 + (5*attentionspan),"minutes")
                   
                    minutes = minutes + 25 + (5*attentionspan)
                    minutes, hour, day, week, month, year = adjusttime(minutes, hour, day, week, month, year)
                    time.sleep(2)
                    numhold = 1
                    dorwhold = 1
           

               
            elif optioncheckup == "b":
                print("you walk to the bank")
                print("it takes",40 + (5*exercise) + (5*attentionspan),"minutes")
                minutes = minutes + 40 + (5*exercise) + (5*attentionspan)
                minutes, hour, day, week, month, year = adjusttime(minutes, hour, day, week, month, year)
                time.sleep(2)
                numhold = 1
                dorwhold = 0
            else:
                print("not an option")
               
        print("you walk up the steps to the bank")
        time.sleep(1)
        answerhold = input("do you pull on your mask and rob the bank")
        if answerhold == "yes":
            print("not done yet")
        else:
            print("ok chicken")
            time.sleep(1)
            print("you walk through the doors and talk to the desk lady")
            time.sleep(1)
            print("can i talk to robby bankquoa")
            time.sleep(1)
            print("she dials the phone and says that they are ready to see you")
            time.sleep(1)
            print("you walk up to the doors to there office")
            time.sleep(1)
            answerhold = input("last chance, do you pull out a gun as you walk in")
            if answerhold == "yes":
                print("not done yet")
            else:
                print("once a chicken always a chicken")
               
                if onloan == 1:
               
                    print("robby says:")
                    print("since you are already on loan and i cant give two loans at once i must assume you are here to pay your loan off")
                    print("how much do you want to pay back you can go into debt")
                    print("you have £"+str(cash),"and you have £"+str(loanowe),"left to pay back")
                    numhold = float(input())
                    loanowe = loanowe - numhold
                    cash = cash - numhold
                    print("you payed £"+str(numhold),"and now owe them £"+str(loanowe),)
                    hour = hour + 1
                else:
                    print("you say:")
                    print("hey robby i need a loan")
                    print(charisma)
                    try:
                        numhold = int(input("how much do you want to take\nit will gain "+str(55 - ((charisma+1)//2)*5)+"% monthly interest\nyou will automatically have 10% of remaining loan subtracted from account upon interest\nWARNING you cannont win while on loan\ntype 123456789 to not recieve a loan"))
                        if numhold < 0 :
                            print("what!?!? a negative loan i never thought of that!")
                            time.sleep(3)
                            print("robbies head starts violently shaking")
                            time.sleep(2)
                            print("it explodes sending bone shrapnel everywhere killing you")
                            quit()
                        elif numhold == 123456789 :
                            print("damn thats alot of money but if you say so")
                            time.sleep(3)
                            print("joking! joking, calm down, i get it no money")
                            time.sleep(1)
                            print("but i still got an hour of your time")
                            time.sleep(1)
                            hour = hour + 1
                            minutes, hour, day, week, month, year = adjusttime(minutes, hour, day, week, month, year)
                        else:
                            loanamount = numhold // 1
                            print("you now have a",loanamount,"dollar loan")
                            loanowe = loanamount
                            hour = hour + 1
                            onloan = 1
                            minutes, hour, day, week, month, year = adjusttime(minutes, hour, day, week, month, year)
                            setrate = charisma
                            time.sleep(1)
                    except ValueError:
                        print("do you think im a idiot? do you? i know thats not a number\nif you are going to waste my time then i will waste yours\nback to the start dont pass go")
                        hour = hour + 1
                        minutes, hour, day, week, month, year = adjusttime(minutes, hour, day, week, month, year)
                        time.sleep(1)
                if dorwhold == 0:
                    minutes = minutes + 40 + (5*exercise) + (5*attentionspan)
                if dorwhold == 1:
                    minutes = minutes + 25 + (5*attentionspan)
                minutes, hour, day, week, month, year = adjusttime(minutes, hour, day, week, month, year)
    elif place == "e":
        time.sleep(0.5)
        print("you currently have £"+str(cash+loanamount),"total to your name",UserName,"but £"+str(cash),"in non-loaned money")
        time.sleep(1)
    else:
        print("Invalid option. Please choose from A, B, C, or D.")
        minutes = minutes + 15
        minutes, hour, day, week, month, year = adjusttime(minutes, hour, day, week, month, year)
        print("the time is",str(hour )+":"+str(minutes))