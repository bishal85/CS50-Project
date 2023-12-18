def main():
    string=input('What time is it? ')
    string1=convert(string)
    if 7<=string1<=8:
        print("breakfast time")
    elif 12<=string1<=13:
        print("lunch time")
    elif 18<=string1<=19:
        print("dinner time")
def convert(time):
    Hour,Minute=time.split(':')
    time=float(Hour)+(float(Minute)/60)
    return(time)


if __name__ == "__main__":
    main()
