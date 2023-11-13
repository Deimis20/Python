codes = []
for i in range(10):
    for j in range(10):
        for k in range(10):
            for l in range(10):
                    code = str(i) + str(j) + str(k) + str(l)
                    codes.append(code)
codes_str = '\n'.join(codes)
with open('4DigitCodes.txt', 'w') as f:
    f.write(codes_str)