"""
During the second Go / No Go poll, the Elf in charge of the Rocket Equation Double-Checker stops the launch sequence. Apparently, you forgot to include additional fuel for the fuel you just added.

Fuel itself requires fuel just like a module - take its mass, divide by three, round down, and subtract 2. However, that fuel also requires fuel, and that fuel requires fuel, and so on. Any mass that would require negative fuel should instead be treated as if it requires zero fuel; the remaining mass, if any, is instead handled by wishing really hard, which has no mass and is outside the scope of this calculation.

So, for each module mass, calculate its fuel and add it to the total. Then, treat the fuel amount you just calculated as the input mass and repeat the process, continuing until a fuel requirement is zero or negative. For example:

A module of mass 14 requires 2 fuel. This fuel requires no further fuel (2 divided by 3 and rounded down is 0, which would call for a negative fuel), so the total fuel required is still just 2.
At first, a module of mass 1969 requires 654 fuel. Then, this fuel requires 216 more fuel (654 / 3 - 2). 216 then requires 70 more fuel, which requires 21 fuel, which requires 5 fuel, which requires no further fuel. So, the total fuel required for a module of mass 1969 is 654 + 216 + 70 + 21 + 5 = 966.
The fuel required by a module of mass 100756 and its fuel is: 33583 + 11192 + 3728 + 1240 + 411 + 135 + 43 + 12 + 2 = 50346.
What is the sum of the fuel requirements for all of the modules on your spacecraft when also taking into account the mass of the added fuel? (Calculate the fuel requirements for each module separately, then add them all up at the end.)
"""

masses=[137503,
60363,
103031,
141000,
101650,
76081,
139069,
63717,
135021,
66034,
53912,
83417,
125978,
73206,
77497,
108822,
133339,
113618,
91973,
88741,
109942,
96523,
95973,
56595,
118638,
63936,
101635,
149154,
85522,
140962,
108196,
105804,
148464,
68429,
146808,
82541,
85581,
117253,
117900,
83457,
103354,
123875,
88412,
108573,
140651,
103774,
95291,
91290,
98690,
87761,
122907,
91499,
141746,
127300,
114866,
75472,
65369,
50978,
119756,
144115,
92483,
146317,
100770,
124156,
109933,
138037,
101126,
58517,
83653,
135656,
111483,
82784,
107459,
106641,
138030,
53599,
123886,
74425,
96919,
65410,
63823,
148278,
133753,
106661,
51147,
120571,
77900,
131827,
107882,
149359,
127565,
67109,
131547,
114874,
130493,
94905,
138654,
58504,
79591,
133856]

total=0
for i in masses:
  res = total_i = int(i/3) - 2
  while res > 0:
    res = int(res/3) - 2
    if res > 0:
      total_i += res
  total += total_i
print(total)
