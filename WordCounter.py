#The program receives a text file and creates a txt file containing:
#number of words, number of unique words, list of words and near them how many times they appeared on text
class WordCounter:
    myDict={}

    def __init__(self,filename):
      #global myDict

      file=open(filename)
      for x in file:
          sentence=x.split()
          for y in range(0, len(sentence)-1):
              if(sentence[y] in self.myDict):
                  self.myDict[sentence[y]]+=1
              else:
                  self.myDict[sentence[y]]=1

          #print(self.myDict.keys())
          #print("")
          #print("")
    def WriteNewFile(self,filename):
        #creating new file - the result
        result=open(filename+"-file.txt","w")
        #title
        result.write("_____________REPORT_____________________ \n")
        result.write("     made by nkprog3 October 2018 \n")
        result.write("________________________________________ \n")
        result.write("________________________________________ \n")
        result.write("\n \n")
        #writing statistics
        result.write("Number of total words in {} are: {} \n".format(filename,len(self.myDict.keys())))
        #calculating unique words
        count=0
        thekeys=self.myDict.keys()
        for x in thekeys:
            if self.myDict[x]==1:
                count+=1
        result.write("Number of unique words in {} are: {} \n".format(filename,count))
        result.write("\n")
        result.write("Words and frequencies: \n")
        #result.write("_"*30)
        result.write("\n")
        #writing appearances of words
        #print(thekeys)
        for i in thekeys:
            result.write("{}: {} \n".format(i,self.myDict[i]))

ann=WordCounter("lincoln.txt")
ann.WriteNewFile("lincoln.txt")
