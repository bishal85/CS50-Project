import re
def main():
    print(parse(input("HTML: ")))


def parse(string1):
    string1=string1.strip()
    k=""
    d="https"
    b=""
    a1=re.search("^(\<iframe).+h.+(\<\/iframe\>)$",string1)
    if a1:

       b1=re.search(r"(.+)htt(ps|p)?\:\/\/(www)?(\.)?youtube\.com\/+[a-z]+\/+([a-zA-Z0-7]+)+(.+)$",string1)
       if b1:
           k=re.sub(b1.group(1),"",string1)
           k=re.sub(b1.group(6),"",k)
           k=k.replace("youtube.com","youtu.be")
           k=k.replace("www.","")
           k=k.replace("/embed","")
           if d not in string1:
               k=k.replace("http","https")

           return k
    else:
       return None
if __name__ == "__main__":
    main()

