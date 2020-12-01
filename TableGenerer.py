class TableOutput:
    def __init__(self, *args):
        self.rows = []
        self.marginLeft = 1
        self.marginRight = 1
        if len(args)>0:
            for row in args:
                if type(row)==tuple or type(row)==list:
                    self.rows.append(row)
    def get_highestRowsCount(self):
        maxOut = 0
        for row in self.rows: maxOut = max(maxOut, len(row))
        return maxOut
    def addRow(self, row):
        if type(row)==tuple:
            self.rows.append(row)
    def toString(self, borderType=0, collapse=False, other={}):
        settings = {**{
            "aligmentHeader":"center",
            "aligmentBody":"center"
        }, **other}
        spaceStr = " "
        outputStr = ""
        #Lines
        tableLine = ""
        #Memory
        centred = []
        #Visual
        tableVisual = {
        "cornerLeftTop":"+",
        "cornerRightTop":"+",
        "cornerLeftBottom":"+",
        "cornerRightBottom":"+",
        "lineHorizontal":"-",
        "lineOutsideHorizontal":"-",
        "lineVertical":"|" ,
        "lineOutsideVertical":"|",
        "lineOutsideVerticalOpening":"|",
        "lineOutsideVerticalEnclosing":"|",
        "lineCrossTop":"-",
        "lineCrossMiddle":"|",
        "lineCrossBottom":"-"
        }
        if borderType==1:
            tableVisual["cornerLeftTop"] = "╔"
            tableVisual["cornerRightTop"] = "╗"
            tableVisual["cornerLeftBottom"] = "╚"
            tableVisual["cornerRightBottom"] = "╝"
            tableVisual["lineHorizontal"] = tableVisual["lineOutsideHorizontal"] = "═"
            tableVisual["lineVertical"] = tableVisual["lineOutsideVertical"] = "║"
            tableVisual["lineOutsideVerticalOpening"] = "╠"
            tableVisual["lineOutsideVerticalEnclosing"] = "╣"
            tableVisual["lineCrossTop"] = "╦"
            tableVisual["lineCrossMiddle"] = "╬"
            tableVisual["lineCrossBottom"] = "╩"
        elif borderType==2:
            tableVisual["cornerLeftTop"] = ""
        
        for row in range(len(self.rows)):
            for r in range(len(self.rows[row])):
                if row==0:
                    centred.append(len(self.rows[row][r]))
                else:
                    centred[r] = max(centred[r], len(str(self.rows[row][r])))

        tableHeader = tableVisual["cornerLeftTop"]
        tableFooter = tableVisual["cornerLeftBottom"]
        tableSeparator = tableVisual["lineVertical"]
        for maxSize in range(len(centred)):
            rowSize = (self.marginLeft + centred[maxSize] + self.marginRight)
            tableHeader += tableVisual["lineOutsideHorizontal"]*rowSize + (maxSize<=len(centred) - 2 and tableVisual["lineCrossTop"] or "")
            tableFooter += tableVisual["lineOutsideHorizontal"]*rowSize + (maxSize<=len(centred) - 2 and tableVisual["lineCrossBottom"] or "")
            tableSeparator += tableVisual["lineHorizontal"]*rowSize + (maxSize<=len(centred) - 2 and tableVisual["lineCrossMiddle"] or "")
        tableHeader += tableVisual["cornerRightTop"] + "\n"
        tableFooter +=  tableVisual["cornerRightBottom"] + "\n"
        tableSeparator += tableVisual["lineVertical"] + "\n"
        for row in range(len(self.rows)):
            tableLine = ""
            if row==0 or collapse==True: outputStr += tableHeader
            for r in range(len(self.rows[row])):
                centredSpace = abs(centred[r] - len(str(self.rows[row][r])))/2
                lastPiece = int(isinstance(centredSpace, numbers.Integral) and centredSpace or math.ceil(centredSpace))
                if r==0: tableLine += tableVisual["lineOutsideVertical"]
                tableLine += f"{spaceStr*(round(centredSpace)+self.marginLeft)}{str(self.rows[row][r])}{spaceStr*(lastPiece + self.marginRight)}"+tableVisual["lineVertical"]
            outputStr += f'{tableLine}\n'
            if row<=(len(self.rows) - 2): outputStr += tableSeparator
            if row==len(self.rows) - 1 or collapse: outputStr += tableFooter
        print(centred)
        return outputStr
