# Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language

# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end
#   now append three random characters at the starting and the end
# else:
#   simply reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
#   remove 3 random characters from start and end. Now remove the last letter and append it to the beginning

# Your program should ask whether you want to code or decode

import random

st = input("Enter message:\n")
code = int(input("Enter 1 for coding and 2 for decoding: "))
words = st.split(" ")
if (code == 1):
    coding = True
    print(coding)
    if(coding):
        nwords = []
        for word in words:
            if (len(word) >= 3):
                txt = ("abc", "def", "ghi", "jkl", "mno", "pqr", "stu", "vwx", "yza", "bcd", "efg", "hij", "klm", "nop", "qrs", "tuv", "wxy", "zab", "cde", "fgh", "ijk", "lmn", "opq", "rst", "uvw", "xyz", "abj", "ced", "fgi", "hnl", "jop", "qru", "stv", "wyx", "yab", "acd", "ehf", "gij", "klp", "mnq", "opr", "stx", "uzv", "wxs", "yib", "cfg", "djh", "flk", "gmj", "hpi", "jtk", "kln", "mqo", "npr", "qst", "ruv", "swx", "bca", "edf", "gih", "kjl", "mnp", "pqf", "sut", "vqw", "xya", "azb", "bdc", "efg", "hif", "jik", "lmp", "nqf", "pgr", "qts", "uxw", "vuz", "yax", "bza", "ced", "fhg", "gij", "jlp", "kmq", "omr", "prq", "rsy", "stv", "wxz",
            "afg", "bhj", "cnk", "dol", "epm", "fqn", "gor", "hpt", "iqv", "jrw", "ksy", "ltz", "mua", "nvb", "owc", "pxd", "qye", "rzf", "sab", "tbc", "ucd", "vde", "wfg", "xgh", "yhi", "zij", "akc", "blg", "cmh", "dnj", "epk", "fql", "gpm", "hqn", "jro", "ksr", "ltu", "muv", "nuw", "owx", "pxy", "qyz", "rab", "sac", "tad", "ube", "vcf", "wdf", "xeg", "yfh", "zgi", "ahj", "bik", "cjl", "dkm", "eln", "fmo", "gnp", "hoq", "ipr", "jqs", "krt", "lus", "mvf", "nwh", "oxo", "pyb", "qzc", "rye", "sfd", "tge", "uif", "vjh", "wkq", "xlr", "ymt", "znu", "aox", "bqa", "crb", "dsc", "etd", "fuf", "gvg", "hwh", "ixi", "jyk", "kzl", "lam", "mbn", "nco", "odq", "pfr", "qgs", "rhu", "siv", "tjk", "ukl", "vlm", "wmn", "xno", "yop", "zqr", "asf", "btg", "cuh", "dvi", "ewj", "fxk", "gyl", "hzm", "ian", "jbo", "kcp", "ldq", "men", "nfo", "ogp", "phq", "qir", "rjs", "stk", "utl", "vum", "wvn", "xwo", "yxp", "zyr", "azf", "bah", "cbi", "dgj", "efk", "flm", "gnp", "hoq", "ipr", "jqs", "krs", "ltu", "muv", "nuw", "owx", "pxy", "qyz", "rab", "sac", "tad", "ube", "vcf", "wdf", "xeg", "yfh", "zgi", "ahj", "bik", "cjl", "dkm", "eln", "fmo", "gnp", "hoq", "ipr", "jqs", "krt", "lus", "mvf", "nwh", "oxo", "pyb", "qzc", "rye", "sfd", "tge", "uif", "vjh", "wkq", "xlr", "ymt", "znu", "aox", "bqa", "crb", "dsc", "etd", "fuf", "gvg", "hwh", "ixi", "jyk", "kzl", "lam", "mbn", "nco", "odq", "pfr", "qgs", "rhu")
                txt2 = random.choice(txt)
                stnew = txt2 + word[1:] + word [0] + txt2
                nwords.append(stnew)
            else:
                nwords.append(word[::-1])
        print(" ".join(nwords))

if (code == 2):
    nwords = []
    for word in words:
        if(len(word)>=3): 
            stnew = word[3:-3]
            stnew = stnew[-1] + stnew[:-1]
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))
