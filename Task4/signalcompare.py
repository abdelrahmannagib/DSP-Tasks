
import math

#Use to test the Amplitude of DFT and IDFT
def SignalComapreAmplitude(SignalInput = [] ,SignalOutput= []):
    if len(SignalInput) != len(SignalInput):
        return False
    else:
        for i in range(len(SignalInput)):
            if abs(SignalInput[i]-SignalOutput[i])>0.001:
                print("faild amp, fraction error")
                return False
            elif round(SignalInput[i],5)!= round(SignalOutput[i], 5):
                print("faild amp, not equal values", round(SignalInput[i],5), round(SignalOutput[i], 5))
                return False
        print("amp passed")
        return True

def RoundPhaseShift(P):
    while P<0:
        P+=2*math.pi
    return float(P%(2*math.pi))

#Use to test the PhaseShift of DFT
def SignalComaprePhaseShift(SignalInput = [] ,SignalOutput= []):
    if len(SignalInput) != len(SignalInput):
        print("phase failed")
        return False
    else:
        for i in range(len(SignalInput)):
            A=round(SignalInput[i])
            B=round(SignalOutput[i])
            if abs(A-B)>0.0001:
                return False
            elif A!=B:
                print("phase failed")
                return False
        print("phase passed")
        return True



