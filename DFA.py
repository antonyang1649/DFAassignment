def runDFA(start, accepted, delta, alphabet, inputs):
    #set position
    position = start
    #transitions from state to state based on every character of input
    for char in inputs:
        position = delta[(position, char)]
    return "Accepted" if position in accepted else "Rejected"

def main():
    #input DFA
    states = input().split()
    alphabet = input().split()
    start = input().strip()
    accepted = set(input().split())

    #expected transitions
    transitions = len(states) * len(alphabet)

    #initiates positions and actions set
    delta = {}
    #asks for possible inputs -> outputs
    for i in range(transitions):
        line = input().strip()
        if line:
            s, a, t = line.split()
            delta[(s, a)] = t
    
    #loops for user inputs
    while True:
        inputs = input().strip()
        if inputs != "":
            print(runDFA(start, accepted, delta, alphabet, inputs.strip()))

if __name__ == "__main__":
    main()
