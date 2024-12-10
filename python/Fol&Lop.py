TheFile = None
TheTries = 3
while TheTries > 0 :
    try:
        print("Enter the file name with absolute path to open")
        print("Example: D:\MyFiles\MyFile.txt")
        print("Input here: ", end="")
        TheTheFile = open(input().strip())
        print(TheTheFile.read())
        break
    except FileNotFoundError:
        print(f"File not found please try again You have {TheTries} left try")
        TheTries -= 1
    except Exception as e:
        print("Error: ", e)
        TheTries -= 1
    finally:
        if TheFile is not None:
            TheFile.close()
            print("File closed")
        else:
            if TheTries == 0:
                print("You have no more tries")