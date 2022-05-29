import os, sys, re, argparse, csv

def readCategories(categoriesFile):
    categoryLookup = {}
    with open(categoriesFile, newline='') as csvFile:
        csvReader = csv.reader((l.lower() for l in csvFile), delimiter=',')
        for row in csvReader:
            categoryVal = row.pop(0)
            for element in row:
                categoryLookup[element] = categoryVal
                print (f"{element}: {categoryVal} -> {categoryLookup[element]}")
    return categoryLookup

def updateData(dataFile, categoryLookup):
    updatedData = []
    with open(dataFile, newline='', encoding="utf-8-sig") as csvFile:
        csvReader = csv.DictReader((l.lower() for l in csvFile), delimiter=',')
        for rowDict in csvReader:
            if rowDict["subjects"] in categoryLookup:
                rowDict["subjects_category"] = categoryLookup[rowDict["subjects"]]
            else:
                 rowDict["subjects_category"] = ""
            updatedData.append(rowDict)   
    return updatedData
      
def printData(outFile, header, updatedData):
    with open (outFile, "w", newline = "") as outFH:
        dictWriter = csv.DictWriter(outFH, header)
        dictWriter.writeheader()
        dictWriter.writerows(updatedData)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--datafile", required = True,  help = "Input data csv file (with col header line)")
    parser.add_argument("--outfile", required = True,  help = "Output csv file")
    parser.add_argument("--categories", required = True, help = "Categories csv file (without col header line)")

    args = parser.parse_args()
    
    header = ["percent_terms","terms","negations","subjects","subjects_category", "predicates"]

    categoryLookup = readCategories (args.categories)
    updatedData = updateData(args.datafile, categoryLookup)
    printData (args.outfile, header, updatedData)
