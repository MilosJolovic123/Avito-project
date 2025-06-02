

def read_file_relevant( filename ):
  """Reads a file that contains only relevant IDs"""
  with open( filename ) as inFile:
     inFile.readline() #ignore header
     relevantIDs = set( [line.strip() for line in inFile] )
  return relevantIDs

def APatK ( predictedFileName, relevantIDsFileName, K ):
  """Calculates AP@k given a file with IDs
  sorted in order of relevance and a file with the 
  relevant IDs"""

  relevantIDs = read_file_relevant( relevantIDsFileName )

  with open( predictedFileName) as predictedFile:
    predictedFile.readline() #ignore header
    countRelevants = 0
    listOfPrecisions = list()
    for i, line in enumerate(predictedFile):
      currentk = i + 1.0
      if line.strip() in relevantIDs:
        countRelevants += 1
      precisionAtK = countRelevants / currentk 
      listOfPrecisions.append(precisionAtK)
      if currentk == K:
        break

  return sum( listOfPrecisions ) / K 

print APatK( "predictions.csv", "solution.csv", 32500 )