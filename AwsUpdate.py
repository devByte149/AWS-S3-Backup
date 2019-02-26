import os, time, datetime

folders = []

def getFolders():
    for entry in os.scandir('/Enter/Local/Path/Here/'):
        if entry.is_dir():
            folders.append(entry.name)          #Records folder name if it is a folder

def syncFolder(folder, command):
    try:
        print("Syncing folder: " + folder)
        os.system(command)
        print("Folder sync for " + folder + " done!\n")
    except Exception as e:              #Logs error if error occurred
        print("Error occured during sync for folder: " + folder + "\n")
        currentDate = datetime.datetime.now()
        filePath = "/Enter/Local/Path/Here/" + currentDate.strftime("%Y-%m-%d") + ".txt"
        f = open(filePath, "a")
        f.write("Error at " + currentDate.strftime("%Y-%m-%d %H:%M:%S") + ": " + e + "\n")


def prepareSync():
    for folder in folders:

        #Variable below is for syncing Workflow on Server
        cmd = "aws s3 sync \"/Enter/Local/Path/Here/" + folder + "/\" \"s3://AWS-BUCKET-NAME/" + folder + "/\""
        
        #Variable below is for testing purposes
        #cmd = "aws s3 sync \"/Enter/Local/Path/Here/" + folder + "/\" \"s3://AWS-BUCKET-NAME/" + folder + "/\""

        #Sends folder name and command to execute
        syncFolder(folder, cmd)

if __name__ == "__main__":
    getFolders()
    prepareSync()
