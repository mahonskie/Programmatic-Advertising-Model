from Advertiser import *
from Host import *
file = open('Data.txt', 'w') # for writing data

# this is the 'runner' py file. Acts as the ad exchange or executes the code to run an auction
# from the Host and Advertiser classes
# this class will also write to a text document to save this data as a CSV
# last edited 3 / 30 / 2023
# Eamon Mahoney



# Test Model
# Advertiser(evaluation,budget, highestPrice,strategy):
#  Host(numberOfAds, auctionList):
adFirm1 = Advertiser(0.5,300, 13,"firm x",0)
adFirm2 = Advertiser(0.7,300,15,"firm y",0)
adFirm3 = Advertiser(0.4,300,12,"firm z",0)
auctionList = [adFirm1,adFirm2,adFirm3]

#print ( auctionList[0].getBudget() )
#print('hi')
host = Host(100, auctionList) #test 0
host.auction()
print("################################################################# 1")
# highest bid strat
adFirm4 = Advertiser(0.5,300, 13,"firm x",1)
adFirm5 = Advertiser(0.7,300,15,"firm y",1)
adFirm6 = Advertiser(0.4,300,12,"firm z",1)
auctionList1 = [adFirm4,adFirm5,adFirm6]

#print ( auctionList[0].getBudget() )
#print('hi')
host1 = Host(100, auctionList1) #test 0
host1.auction()
print("################################################################# 2")
adFirm7 = Advertiser(0.5,300, 13,"firm a",0)
adFirm8 = Advertiser(0.7,300,15,"firm b",0)
adFirm9 = Advertiser(0.4,300,12,"firm c",1)
adFirm10 = Advertiser(0.5,300,10,"firm c",1)
auctionList2 = [adFirm7,adFirm8,adFirm9,adFirm10]

host2 = Host(100, auctionList2) #test 0
host2.auction()

print("################################################################# 3")
adFirm11 = Advertiser(0.5,300, 10,"firm x",0)
adFirm12 = Advertiser(0.7,300,15,"firm y",0)
adFirm13 = Advertiser(0.8,300,13,"firm AVG",2)
auctionList3 = [adFirm11,adFirm12,adFirm13]

host3 = Host(100, auctionList3) #test 0
host3.auction()

print("################################################################# 3")
adFirm14 = Advertiser(0.5,300, 10,"firm x",1)
adFirm15 = Advertiser(0.7,300,15,"firm y",1)
adFirm16 = Advertiser(0.8,300,13,"firm AVG",2)
auctionList4 = [adFirm14,adFirm15,adFirm16]

host4 = Host(100, auctionList4) #test 0
host4.auction()

print("################################################################# 3")
adFirm17 = Advertiser(0.5,300, 10,"firm x",1)
adFirm18 = Advertiser(0.7,300,15,"firm y",1)
adFirm19 = Advertiser(0.8,300,13,"firm SH",3)
auctionList5 = [adFirm17,adFirm18,adFirm19]

host5 = Host(100, auctionList5) #test 0
host5.auction()
###########################################################################

def formatData(testName,host):
    winnerList = host.getWinnerList()
    names = host.getWinnerNameList()
    printData = testName + ","
    counter = 0
    for i in winnerList :
        printData += str ( winnerList[counter]) + ","
        counter = counter + 1


    printData = printData[:-1]
    printData = printData + '\n'+ "Firm Name" + ","
    #print(printData)
    counter = 0
    for i in names :
        printData += str (names[counter]) + ","
        counter = counter + 1
    printData = printData[:-1]
    printData = printData + '\n' + '\n'
    return printData

data = formatData("Test 0",host) + formatData("test 1", host1) + formatData("test 2", host2) + formatData("test 3", host3)
data = data + formatData("test 4",host4) + formatData("test 5",host5)

print (data)
file.write(data)
