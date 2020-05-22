import re
class pokerdoc():
    def __init__(self,hand,time,seats,otherinfos):
        self.hand = hand
        self.time = time
        self.seats = seats
        self.otherinfos = otherinfos
#
def read_poker(filepath):
    with open(file=filepath,mode='r',encoding='utf-8') as f:
        lines = f.readlines()
        docs = []
        i=0
        hand = ''
        temps = ''
        while i < len(lines):
            if lines[i]=='\n' and lines[i+1] == '\n':
                # next data
                i = i + 2
                docs.append(pokerdoc(hand,temps,temps,temps))
                continue
            if lines[i].find('PokerStars')==0:
                hand = re.split(r'[#:]',lines[i])[1]
            if lines[i].find('Seat')==0:
                temps = re.split(r'\s*[\s|:|(|)]\s*',lines[i])
        print(hand)
        print(temps)

# file_path = "./out/pluribus_30.txt"
# with open(file=file_path,mode='r',encoding='utf-8') as f:
#     lines = f.readlines()
#     print(lines)
lines = 'Seat 1: MrWhite (10000 in chips)'
temps = re.split(r'\s*[\s|:|(|)]\s*',lines)
print(temps)
['Seat', '1', 'MrWhite', '10000', 'in', 'chips', '']

for i in range(30,118):
    print(i)





