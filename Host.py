# This will be the Host Class
# This class will represent the 'ad hosts' and 'ad service' side of this project.
# In other words, it will be the controller of the number of auctions, and the value of each ad to each player
# This is where bids will be processed, declare a winner, and post the data of the winners to a text file
# Eamon Mahoney
# last edited 3 / 30 / 2023

# constructor
class Host:
    def __init__(self, numberOfAds, auctionList):
        self.numberOfAds = numberOfAds #number of ads in the auction
        self.auctionList = auctionList # the people in the auction like this :  [firm], since we can just do the getBid function
        #self.targetLevel = targetLevel # the determined targetLevel of an ad from 0 - 1
        self.auctionWinner = -1 # THE WINNER! starts with no winner  :(
        self.winningPrice = -1 # the winning price, this gets saved, no
        self.winnerList = []
        self.winnerNameList = []

    # getters / setters
    def setNumberOfAds(self,numberOfAds):
        self.numberOfAds = numberOfAds
    def setAuctionList(self, auctionList):
        self.auctionList = auctionList
    def setTargetLevel(self,targetLevel ):
        self.targetLevel = targetLevel
    def setAuctionWinner(self, auctionWinner):
        self.auctionWinners = auctionWinner
    def setWinningPrice(self, winningPrice):
        self.winningPrice = winningPrice
    def getWinnerNameList(self):
        return self.winnerNameList
    def getWinnerList(self):
        return self.winnerList
    def getNumberOfAds(self):
        return self.numberOfAds
    def getAuctionList(self):
        return self.auctionList
    def getAuctionMembers(self):
        return self.targetLevel
    def getAuctionWinner(self):
        return self.auctionWinner
    def getWinningPrice(self):
        return self.winningPrice

    def getBids(self): # puts all bids with respective bidder, usefull for printing data
        # asks the advertiser class for their bid'
        #
        temp = 0
        bidList = []
        for i in self.auctionList:
            bidList = self.auctionList[temp].getBid()
            temp = temp + 1
        return bidList

    def getWinner(self): # returns the highest bidder from the auctionList

        currentWinner = self.auctionList[0]
        counter = 0
        for i in self.auctionList:
            #print (currentWinner)
            if (self.auctionList[counter].getBid() > currentWinner.getBid()):
                    currentWinner = self.auctionList[counter]

            elif (self.auctionList[counter].getBid() == currentWinner.getBid()): #Then we check evaluations in a tie

                if (self.auctionList[counter].getEval() >= currentWinner.getEval()):
                    currentWinner = self.auctionList[counter]
            counter = counter + 1
            # so if its a tie, the person who the ad is worth more to wins. This will be in the advertisor class (score from 0 - 1)

        self.currentWinner = currentWinner
        #print(self.currentWinner)
        return self.currentWinner

    def getWinningPrice(self):# gets the second highest price, requires that bids have been placed
        priceList = []
        counter = 0

        for i in self.auctionList :
           priceList.append(self.auctionList[counter].getBid())
           counter = counter + 1
           #print(priceList)
        #length = len(priceList)
        #print(length)
        priceList.sort()
        length = len(priceList)
        #print("This is the sorted pricelist")
        #print(priceList)
        self.winningPrice = priceList[length - 2]
        #print("the price should be " + str(self.winningPrice + 0.1))

        if self.winningPrice == 0 : #no winners (everyone is out of money)
            return self.winningPrice

        return self.winningPrice + 0.01 #real

    def payUpBuddy(self, winner, price): # aks the winner for money
        #print("price")
        #print(price)

        if winner.getBudget() - price < 0:
            print("LOUD INCORRECT BUZZER : insufficient funds")

        print(winner.getName() + " wins at a price of " + str(price))
        winner.setBudget(winner.getBudget() - price)

    def auction(self):
       counter = 0
       #winnerList = []
       #self.winnerNameList = []

       for i in self.auctionList :
           if self.auctionList[counter].getStrat() == 0 :
                self.auctionList[counter].calcFirstBid()
           elif self.auctionList[counter].getStrat() == 1:
               self.auctionList[counter].highestBidStrat()
           elif self.auctionList[counter].getStrat() == 2:
               self.auctionList[counter].avgStrat(self.winnerList,self.numberOfAds)
           elif self.auctionList[counter].getStrat() == 3:
               self.auctionList[counter].secondHighest(self.winningPrice,self.auctionWinner)
           counter = counter + 1

       winner = self.getWinner()
       winningPrice = self.getWinningPrice()
       print("first winner : " + winner.getName() + " price : " + str(winningPrice) + ": eval : " + str ( winner.getEval()))
       self.auctionWinner = winner
       self.winningPrice = winningPrice

       self.payUpBuddy(winner,winningPrice)
       self.winnerList.append(winningPrice)
       self.winnerNameList.append(winner.getName()) #+" " + str(winner.getBudget()))

       #counter = 0

       while(self.numberOfAds > 0):
           counter = 0
           print(self.numberOfAds)

           for i in self.auctionList :
              if self.auctionList[counter].getStrat() == 0 :
                self.auctionList[counter].calcBid(winningPrice,winner.getBid())
              elif self.auctionList[counter].getStrat() == 1 :
                  self.auctionList[counter].highestBidStrat()
              elif self.auctionList[counter].getStrat() == 2:
                  self.auctionList[counter].avgStrat(self.winnerList[-10:],self.numberOfAds)
              elif self.auctionList[counter].getStrat() == 3:
                  self.auctionList[counter].secondHighest(self.winningPrice,self.auctionWinner)
              counter = counter + 1

           winner = self.getWinner()
           winningPrice = round ( self.getWinningPrice(),2)
           self.auctionWinner = winner
           self.winningPrice = winningPrice
           self.payUpBuddy(winner, winningPrice)

           self.winnerList.append(winningPrice)
           self.winnerNameList.append(winner.getName()) #+ " " + str(winner.getBudget()))
           self.numberOfAds = self.numberOfAds - 1
       print(self.winnerList)

       #for i in winnerList :
       print(self.winnerNameList)



