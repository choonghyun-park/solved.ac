import sys
import heapq
import itertools
from collections import deque

class Conference:
    def __init__(self):
        self.uoConfs = {}       # S:E
        self.olConfs = {}       # S:E
        self.uoTimeTable = {}   # time : (S,E) 
        self.olTimeTable = {}   # time : overlapID
        self.overlapIDs = {}    # overlapID : (S1,E1),(S2,E2),...
        self.overlapID = 0

    def reserve(self,S,E):
        self.uoConfs[S]=E
        for i in range(S,E):
            self.uoTimeTable[i]=(S,E)

    def cancel(self,S,E):
        del(self.uoConfs[S])
        for i in range(S,E):
            del(self.uoTimeTable[i])
    
    def isReserved(self,T):
        if T in self.uoTimeTable:
            return True
        else: 
            return False
    
    def newOverlap(self,S1,E1,S2,E2): # NOTE : s1 < s2
        self.olConfs[S1]=E1
        self.olConfs[S2]=E2
        self.overlapIDs[self.overlapID]=[(S1,E1),(S2,E2)]
        for t in range(S1,E2):
            self.olTimeTable[t] = self.overlapID
        self.overlapID += 1

    def addOverlap(self,overlapID,S,E):
        self.olConfs[S]=E
        self.overlapIDs[overlapID].append((S,E))
        for t in range(S,E):
            if t not in self.olTimeTable:
                self.olTimeTable[t]=overlapID
    
    def isOverlaped(self,T):
        if T in self.olTimeTable:
            return True
        else:
            return False

    def addConf(self,S,E):
        state,conf = self.checkState(S,E)
        if state=="DELETE_EXISTING":
            self.cancel(conf[0],conf[1])
            self.reserve(S,E)
        elif state=="OVERLAP_FRONT":
            self.cancel(conf[0],conf[1])
            self.newOverlap(conf[0],conf[1],S,E)
        elif state=="OVERLAP_BACK":
            self.cancel(conf[0],conf[1])
            self.newOverlap(S,E,conf[0],conf[1])
        elif state=="ADD_OVERLAP":
            self.addOverlap(conf,S,E)
        elif state=="UNUSED":
            pass
        elif state=="USED":
            self.reserve(S,E)
        return

    def checkState(self,S,E):
        for t in range(S,E):
            if self.isReserved(t):
                s = self.uoTimeTable[t][0]
                e = self.uoTimeTable[t][1]
                if s<=S and e>=E:
                    return ("DELETE_EXISTING",(s,e))
                elif s<=S and e<E:
                    return ("OVERLAP_FRONT",(s,e))
                elif s>S and e>=E:
                    return ("OVERLAP_BACK",(s,e))
                else:
                    return ("UNUSED",-1)
            elif self.isOverlaped(t):
                overlapID = self.olTimeTable[t]
                return ("ADD_OVERLAP",overlapID)
        return ("USED",-1)

    def calMaxConfs(self):
        n_uo = len(self.uoConfs.keys())
        n_ol = self.calOverlapConfs()
        n = n_uo + n_ol
        print(n_uo)
        print(n_ol)
        return n

    def calOverlapConfs(self):
        n_ol = 0
        ID_keys = self.overlapIDs.keys()
        for ID_key in ID_keys:
            ol_confs = self.overlapIDs[ID_key]
            n_ol += self.calOverlapMax(ol_confs)
        return n_ol

    def calOverlapMax(self,ol_confs):
        # TODO
        flag = False
        for i in range(len(ol_confs)):
            n_confs = len(ol_confs)-i
            flag = True
            nCr = itertools.combinations(ol_confs,n_confs)
            tt = {}
            for case in nCr:
                tt[case[0]]="S"
                tt[case[1]]="E"
            tt_keys = list(tt.keys())
            for j in range(len(tt_keys)-1):
                if tt[tt_keys[j]]==tt[tt_keys[j+1]]:
                    flag = False
                    break
            if flag:
                return n_confs
        return 0

    def printSchedule(self):
        print("========================")
        print("unoverlaped conferences")
        print(self.uoTimeTable)
        print("overlaped conferences")
        print(self.olTimeTable)
        print(self.overlapIDs)
        print("========================")
        print()


def calConfs(overlap):
    # 모든 조합을 (가장 긴 길이-1)부터 계산
    flag = False
    for i in range(1,len(overlap)):
        n_confs = len(overlap)-i
        # print("n_confs",n_confs)
        nCr = itertools.combinations(overlap,n_confs)
        for case in nCr:
            flag = True
            for j in range(len(case)-1):
                end = case[j][1]
                next_start = case[j+1][0]
                if end>next_start:
                    flag=False
                    break
            if flag:
                # result.append(case)
                return n_confs 
    return 0

N = int(sys.stdin.readline())

inputs = {}

conf = Conference()

for _ in range(N):
    S,E = map(int,sys.stdin.readline().split())
    dur = E-S
    if dur in inputs:
        inputs[dur].append((S,E))
    else:
        inputs[dur]=[(S,E)]

for values in inputs.values():
    for value in values:
        conf.addConf(value[0],value[1])
        # conf.printSchedule()
    

# for input in inputs:
#     conf.addConf(input[0],input[1])
#     conf.printSchedule()

print(conf.calMaxConfs())

