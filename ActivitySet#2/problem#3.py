def get_cs():
    return input()


def cs_to_lot(cs):
    lis=[]
    pos1=cs.find("=")
    first=cs[0:pos1]
    second=cs[pos1+1]
    final=(first,second)
    lis.append(final)
    cs[0:second]

def main():
    cs = get_cs()

    lot = cs_to_lot(cs)
    print(lot)


if __name__ == '__main__':
    main()
