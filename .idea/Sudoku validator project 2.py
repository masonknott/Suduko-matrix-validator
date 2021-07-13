def is_duplicates(list):
    for item in list:
        # by creating a Set() from our item - which removes duplicates -
        # we can just compare the lengths to see if any duplicates existed
        if not(len(set(item)) != len(item)):#sets to take out duplicates -i need reference here!
            return True
    return False

def parseSudoku(data):
    matrixRows = []
    # build our matrix of rows
    for index, line in enumerate(data):#i need to reference this!
        try:
            if index > 8:
                # This ensures theres only 9 rows
                raise ValueError('Row n is over 9')
            rowList = line.split()
            rowArrayOfInts = []
            for indexCol, char in enumerate(rowList):
                if indexCol > 8:
                    # This ensures theres only 9 columns
                    # Combined with the rows - this ensures its a 9x9 grid
                    raise ValueError('Col n is over 9')
                
                intToAppend = int(char)
                if intToAppend > 9:
                    # Cant have a number over 9
                    raise ValueError('Int is over 9')
                rowArrayOfInts.append(intToAppend)
        except ValueError:
            # found an error above
            print("Invalid sudoku - format invalid")
            exit();
        matrixRows.append(rowArrayOfInts)

    # already have the rows now so this is a good assign
    rows = matrixRows

    # columns - this is grouping each X num together from each row
    #using 9 predfined arrays and the index here
    # we will have 9 sub-arrays here because of the line check above
    matrixCol = [[],[],[],[],[],[],[],[],[]]
    for index, row in enumerate(rows):
        for indexRow, num in enumerate(row):
            matrixCol[indexRow].append(num);

    cols = matrixCol;

    #lastly the 3x3 grids...
    matrixGrids = [[],[],[],[],[],[],[],[],[]]
    for index, row in enumerate(rows):
        for col, num in enumerate(row):
            # first - i get an estimate grid based on the row
            possibleGrid = None
            gridToInsert = None
            if index == 0 or index == 1 or index == 2:
                possibleGrid = [0,1,2]
            if index == 3 or index == 4 or index == 5:
                possibleGrid = [3,4,5]
            if index == 6 or index == 7 or index == 8:
                possibleGrid = [6,7,8]

            # then use the column to decide!
            if col == 0 or col == 1 or col == 2:
                gridToInsert = possibleGrid[0]
            if col == 3 or col == 4 or col == 5:
                gridToInsert = possibleGrid[1]
            if col == 6 or col == 7 or col == 8:
                gridToInsert = possibleGrid[2]

            matrixGrids[gridToInsert].append(num);

    grids = matrixGrids
    return [rows, cols,grids]

def writedata(fileContents, filename): #writes the checked_ file
    f = open("CHECKED_"+filename, "w")#after the code is valid
    f.write(fileContents)
    f.close()

def readdata():#reads the file input by user if the file name is valid, else returns error asking to try again
    while True:
        try:
            filename = input("Enter the filename of the data you wish to import: ")
            ioWrapper = open(filename, 'r')
            return [ioWrapper, filename]
        except FileNotFoundError:
            print("File Not found, please try again")

if __name__ == "__main__":

    # readdata returns our data and filename in the form of [ioWrapper, filename]
    arrReadData = readdata()
    ioWrapper = arrReadData[0]
    filename = arrReadData[1]

    fileContents = ioWrapper.read()
    ioWrapper.close()

    #parseSudoku returns our rows, columns and grids in the form of [rows,cols,grids]
    arrParsedData = parseSudoku(fileContents.splitlines())

    # now check for any duplicates!
    rows = arrParsedData[0]
    cols = arrParsedData[1]
    grids = arrParsedData[2]
    validRows = is_duplicates(rows)
    validCols = is_duplicates(cols)
    validGrids = is_duplicates(grids)

    if (validRows and validCols and validGrids):
        writedata(fileContents, filename)
    else:
        print("Invalid sudoku - duplicate found")
    exit()


