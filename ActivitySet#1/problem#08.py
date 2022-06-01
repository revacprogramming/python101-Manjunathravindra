def test():
    text = "X-DSPAM-Confidence:    0.8475"
    return text
def search(text):
    f=text.find("0")
    l=text.find("5")
    return f,l
def slice(txt,f,l):
    finaltxt=txt[f:l+1]
    return finaltxt
def prt(finaltxt):
    print(finaltxt)
def main():
    text=test()
    f,l=search(text)
    finaltxt=slice(text,f,l)
    prt(finaltxt)
if __name__=='__main__':
    main()



