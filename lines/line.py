elif d in n and len(e)==3:
            m2,n1=n2.split(".")
            m5,m7=n5.split(".")
            m52=os.path.splitext(sys.argv[1])
            m57=os.path.splitext(sys.argv[2])
            m71=[".jpg",".jpeg","png"]
            if n1[0:len(n1)-2].lower()!="jpg" and m7[0:len(m7)-2].lower()!="jpg" or n1[0:len(n1)-2]!="jpeg" and m7[0:len(m7)-2]!="jpeg" or n1[0:len(n1)-2]!="png" and m7[0:len(m7)-2]!="png":
                  sys.exit("Not a Python file")
            elif n1[0:len(n1)-2].lower()!= m7[0:len(m7)-2]:
                  sys.exit("Different")
            elif n1[0:len(n1)-2].lower()=="jpg" and m7[0:len(m7)-2].lower()=="jpg" or n1[0:len(n1)-2].lower()=="jpeg" and m7[0:len(m7)-2].lower()=="jpeg" or n1[0:len(n1)-2]=="png" and m7[0:len(m7)-2]=="png":
                  print("Empty")
                  string5(sys.argv[1],sys.argv[2])
