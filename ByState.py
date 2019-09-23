states = {
  'AZ':'Arizona',
  'CA':'California',
  'ID':'Idaho',
  'IN':'Indiana',
  'MA':'Massachusetts',
  'OK':'Oklahoma',
  'PA': 'Pennsylvania',
  'VA': 'Virginia'
}

def getState(inputArray):
  lastElem = inputArray[len(inputArray) - 1] 
  lastIndexElem = len(lastElem)
  return lastElem[lastIndexElem - 2:lastIndexElem]

def getName(inputArray):
  return inputArray[1]

def getCity(inputArray):
  lastElem = inputArray[len(inputArray) - 1] 
  lastIndexElem = len(lastElem)
  return lastElem[0:lastIndexElem - 3]

def resultStringCreator(inputArray, inputObj):
  lastIndex = len(inputArray) - 1
  result = ''  
  for i in inputArray:
    indexOfElem = inputArray.index(i)
    if indexOfElem - 1 >= 0 and getState(inputArray[indexOfElem]) == getState(inputArray[indexOfElem - 1]):
      result += f"..... {inputArray[indexOfElem][1]} {inputArray[indexOfElem][2]} {getCity(inputArray[indexOfElem])} {inputObj[getState(inputArray[indexOfElem])]}"
      result += '' if (indexOfElem == lastIndex) else "\r\n"
    else:
      if indexOfElem > 0:
        result += ' '
      result += f"{inputObj[getState(inputArray[indexOfElem])]}\r\n..... {inputArray[indexOfElem][1]} {inputArray[indexOfElem][2]} {getCity(inputArray[indexOfElem])} {inputObj[getState(inputArray[indexOfElem])]}"
      result += '' if (indexOfElem == lastIndex) else "\r\n"  
  return result

def by_state(inputString):
  personsArrLines = inputString.splitlines()
  lines = [ [ j.strip() for j in i.split(',')] for i in personsArrLines ] 
  linesExt = map( lambda x: (getState(x), x[0], x[1], x[2]), lines)
  sortedPersonsDataArr = sorted(linesExt)
  return resultStringCreator(sortedPersonsDataArr, states)
