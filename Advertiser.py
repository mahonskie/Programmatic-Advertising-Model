# this is the Advertisor class
# This class will analyze passed bids and decide how much they should bid
# Will base this off of the value of an ad and last bids
# Eamon Mahoney
# last edited 3 / 30 / 2023


class Advertiser:
    def __init__(self, evaluation,budget, highestPrice,name,strategy):
        self.evaluation = evaluation
        self.lastWinningBid = -1.0
        #self.lastWinningPrice = -1.0
        self.currentBid = 0.0
        self.budget = budget
        self.highestPrice = highestPrice
        self.won = False
        self.name = name
        self.strategy = strategy
        self.lastBid = -1
        self.found = 0 # variable for second highest strat, 0 if not found 1 if price is found

    def getEval(self):
        return self.evaluation

    def getBudget(self):
        return self.budget

    def setBudget (self,budget):
        self.budget = budget

    def lastWinningPrice(self,lastWinningPrice):
        self.lastWinningBid = lastWinningPrice

    def getName(self):
        return self.name

    def getBid(self):
        return self.currentBid

    def getStrat(self):
        return self.strategy

    def setBid(self,newBid):
        self.currentBid = newBid

    def calcFirstBid(self): # first bid in strategy 0
        if self.highestPrice * self.evaluation < self.budget : # just in case
         self.currentBid = self.highestPrice * self.evaluation
        else :
            self.currentBid = self.budget - 0.1
        print("first Bid : " + self.getName() + " : bid :" +  str (self.getBid()) + " : budget : " +str(self.getBudget()))
        return self.currentBid

    def highestBidStrat(self): # 'optimal' strategy, strategy 1
        #print('')
        if (self.highestPrice < self.budget):
            self.currentBid = self.highestPrice - 0.01
        else :
            self.currentBid = self.budget - 0.01
        print(self.getName() + " :  budget : " + str(self.budget) + " bid :" + str(self.currentBid))
        return round ( self.currentBid , 2)

    def secondHighest(self,winningAmount,winner):

        if winningAmount == -1 :
            self.currentBid = self.highestPrice * self.evaluation
            print(self.getName() + " :  budget : " + str(self.budget) + " bid :" + str(self.currentBid))
            return self.currentBid


        if(self.found == 1 and winner.getName() != self.getName()):
            print(self.getName() + " :  budget : " + str(self.budget) + " bid :" + str(self.currentBid))
            return self.currentBid

        if (winner.getName() == self.getName() and round ( self.highestPrice + (1 * self.evaluation),2)  <= self.budget ):
            if self.found == 0 :
                self.currentBid = self.currentBid - 0.5
            if winningAmount < self.currentBid and self.found == 1:
                self.currentBid = self.highestPrice * self.evaluation
            self.found = 1


        elif(winningAmount - 0.01 <= self.currentBid and self.currentBid + 0.5 < self.budget):
            if(self.found == 0):
                self.currentBid = self.currentBid + 0.5
            self.found = 0

        if (self.highestPrice * self.evaluation > self.budget):
            self.currentBid = self.budget
            self.found = 0

        print(self.getName() + " :  budget : " + str(self.budget) + " bid :" + str(self.currentBid))
        return round ( self.currentBid, 2)

    def avgStrat(self,winningBidList,turnNumber):
        #print('avg strat')
        #print(winningBidList)
        #print(turnNumber)
        if (turnNumber > 90):
            self.currentBid = 0.0
            print(self.getName() + " :  budget : " + str(self.budget) + " bid :" + str(self.currentBid))
            return round (self.currentBid, 2)
        sum = 0
        counter = 0
        print(winningBidList)
        for i in winningBidList :
            sum += winningBidList[counter]
            counter = counter + 1
        avg = round ( sum / len(winningBidList) - 1, 2)
        if (avg < self.budget and avg < self.highestPrice):
            self.currentBid = avg
        else :
            self.currentBid = self.budget

        if (avg < 1) :
            self.currentBid = 1
        print(self.getName() + " :  budget : " + str(self.budget) + " bid :" + str(self.currentBid))
        return round (self.currentBid, 2)

    def calcBid(self,winningBid,lastPrice): # standard strategy, strategy '0'
       self.lastWinningBid = winningBid
       self.lastBid = self.currentBid
       if (lastPrice == self.lastBid and lastPrice < self.budget and lastPrice < self.highestPrice) :
           print(self.getName() + " :  budget : " + str(self.budget) + " bid :" + str(self.currentBid))
           return self.lastBid
       # print("currentBid")
       # print(self.currentBid)
       #print("new Bid")
       # print(winningBid + (1 * self.evaluation))
       #print("budget")
       #print (self.budget)

       if( self.budget > 0 ) :
        if  winningBid < round ( self.highestPrice + (1 * self.evaluation),2)  and round ( self.highestPrice + (1 * self.evaluation),2)  <= self.budget :
            self.currentBid = round ( winningBid + (1 * self.evaluation), 2 )
            #if (self.budget < 0):
            #    print("WOW I AM SO DUMB HOW DID I END UP HERE 1")

        elif (self.highestPrice >= self.budget - 0.01) :
            #if (self.budget < 0):
            #    print("WOW I AM SO DUMB HOW DID I END UP HERE 2")
            self.currentBid = round ( self.budget - 0.01,2)

        elif (self.currentBid >= self.budget):
            self.currentBid = self.budget
        #else :
        #    self.currentBid = round ( self.highestPrice * self.evaluation, 2)
        #    print('hi')
            #if (self.budget < 0):
            #    print("WOW I AM SO DUMB HOW DID I END UP HERE 3")
       #print("currentBid 2")
       #print(self.currentBid)
       #print("new Bid 2")
       #print(winningBid + (1 * self.evaluation))
       else :
           self.currentBid = 0
           print(self.currentBid)

       if (self.currentBid > self.highestPrice) :
           self.currentBid = self.highestPrice - 0.01
       print(self.getName() + " :  budget : " + str(self.budget) + " bid :" + str(self.currentBid))

       return round ( self.currentBid , 2)

