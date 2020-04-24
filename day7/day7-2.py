"""
It's no good - in this configuration, the amplifiers can't generate a large enough output signal to produce the thrust you'll need. The Elves quickly talk you through rewiring the amplifiers into a feedback loop:

      O-------O  O-------O  O-------O  O-------O  O-------O
0 -+->| Amp A |->| Amp B |->| Amp C |->| Amp D |->| Amp E |-.
   |  O-------O  O-------O  O-------O  O-------O  O-------O |
   |                                                        |
   '--------------------------------------------------------+
                                                            |
                                                            v
                                                     (to thrusters)
Most of the amplifiers are connected as they were before; amplifier A's output is connected to amplifier B's input, and so on. However, the output from amplifier E is now connected into amplifier A's input. This creates the feedback loop: the signal will be sent through the amplifiers many times.

In feedback loop mode, the amplifiers need totally different phase settings: integers from 5 to 9, again each used exactly once. These settings will cause the Amplifier Controller Software to repeatedly take input and produce output many times before halting. Provide each amplifier its phase setting at its first input instruction; all further input/output instructions are for signals.

Don't restart the Amplifier Controller Software on any amplifier during this process. Each one should continue receiving and sending signals until it halts.

All signals sent or received in this process will be between pairs of amplifiers except the very first signal and the very last signal. To start the process, a 0 signal is sent to amplifier A's input exactly once.

Eventually, the software on the amplifiers will halt after they have processed the final loop. When this happens, the last output signal from amplifier E is sent to the thrusters. Your job is to find the largest output signal that can be sent to the thrusters using the new phase settings and feedback loop arrangement.

Here are some example programs:

Max thruster signal 139629729 (from phase setting sequence 9,8,7,6,5):

3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,
27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5
Max thruster signal 18216 (from phase setting sequence 9,7,8,5,6):

3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,
-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,
53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10
Try every combination of the new phase settings on the amplifier feedback loop. What is the highest signal that can be sent to the thrusters?
"""

values=[3,8,1001,8,10,8,105,1,0,0,21,42,67,76,89,110,191,272,353,434,99999,3,9,102,2,9,9,1001,9,2,9,1002,9,2,9,1001,9,2,9,4,9,99,3,9,1001,9,4,9,102,4,9,9,101,3,9,9,1002,9,2,9,1001,9,4,9,4,9,99,3,9,102,5,9,9,4,9,99,3,9,1001,9,3,9,1002,9,3,9,4,9,99,3,9,102,3,9,9,101,2,9,9,1002,9,3,9,101,5,9,9,4,9,99,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,99]

# Return the index we want to use depending on mode
def _idx(pos, mode, values):
    return pos if int(mode[0]) else values[pos]

def intcode_computer(values, input, phase, start_idx):
    inputs = input if phase is None else [phase] + input # phase will be used first
    idx = start_idx
    val = str(values[idx]).zfill(5) # Pad with leading zeroes until the length of the value is 5
    opcode = val[-2:]
    output = []

    while opcode != '99':
        mode = list(val[:-2])
        mode.reverse() # mode[0] is first parameter's mode etc.
        if opcode == '01':
            firstParam = _idx(idx+1, mode[0], values)
            secondParam = _idx(idx+2, mode[1], values)
            thirdParam =  _idx(idx+3, mode[2], values)
            values[thirdParam] = values[firstParam] + values[secondParam]
            idx += 4
        elif opcode == '02':
            firstParam = _idx(idx+1, mode[0], values)
            secondParam = _idx(idx+2, mode[1], values)
            thirdParam =  _idx(idx+3, mode[2], values)
            values[thirdParam] = values[firstParam] * values[secondParam]
            idx += 4
        elif opcode == '03':
            firstParam = _idx(idx+1, mode[0], values)
            if not inputs: # No input left to process, pause the amplifier and send all generated outputs
                return output, idx, values
            values[firstParam] = inputs.pop(0)
            idx += 2
        elif opcode == '04':
            firstParam = _idx(idx+1, mode[0], values)
            output.append(values[firstParam])
            idx += 2
        elif opcode == '05':
            firstParam = _idx(idx+1, mode[0], values)
            secondParam = _idx(idx+2, mode[1], values)
            if values[firstParam] != 0:
                idx = values[secondParam]
            else:
                idx += 3
        elif opcode == '06':
            firstParam = _idx(idx+1, mode[0], values)
            secondParam = _idx(idx+2, mode[1], values)
            if values[firstParam] == 0:
                idx = values[secondParam]
            else:
                idx += 3
        elif opcode == '07':
            firstParam = _idx(idx+1, mode[0], values)
            secondParam = _idx(idx+2, mode[1], values)
            thirdParam =  _idx(idx+3, mode[2], values)
            if values[firstParam] < values[secondParam]:
                values[thirdParam] = 1
            else:
                values[thirdParam] = 0
            idx += 4
        elif opcode == '08':
            firstParam = _idx(idx+1, mode[0], values)
            secondParam = _idx(idx+2, mode[1], values)
            thirdParam =  _idx(idx+3, mode[2], values)
            if values[firstParam] == values[secondParam]:
                values[thirdParam] = 1
            else:
                values[thirdParam] = 0
            idx += 4
        else:
            print("Error, invalid Opcode %s" % opcode)
            break
        if idx > len(values):
            print('index greater than max')
            break
        val = str(values[idx]).zfill(5) # Pad with leading zeroes until the length of the value is 5 
        opcode = val[-2:]
    return output, idx, values # Stop the feedback loop


# Yo dawg, I heard you like for-loops...
output = max_output = maxest_output = 0
for first in range(5,10):
    for second in set(range(5,10)) - set([first]):
        for third in set(range(5,10)) - set([first, second]):
            for fourth in set(range(5,10)) - set([first, second, third]):
                for fifth in set(range(5,10)) - set([first, second, third, fourth]):
                    phase_seq = [first, second, third, fourth, fifth]
                    currentValues = [values] * 5
                    start_idx = [0] * 5
                    output = [0]
                    stop = False
                    while not stop:
                        for idx in range(len(phase_seq)):
                            output, start_idx[idx], currentValues[idx] = intcode_computer(list(currentValues[idx]),
                                                                                          output, phase_seq[idx],
                                                                                          start_idx[idx])
                            phase_seq[idx] = None
                            if not output: # One of the amps got opcode 99 and we have no output left to process
                                stop = True
                                break
                        else: # Iteration passed without any amp getting opcode 99, save amp E's output
                            if len(output) != 1:
                                print('something wrong with output')
                                exit()
                            max_output = output[0]
                    maxest_output = max(maxest_output, max_output)

print(maxest_output)
