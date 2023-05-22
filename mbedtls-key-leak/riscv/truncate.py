#! /usr/bin/env python3




def main():
    new_lines = []
    with open("./key_leak.log", "r") as fd:
        for line in fd:
            idx, bit, one, zero = line.split(",")
            if int(one) > 11500:
                continue
            else:
                new_lines.append(line)
    with open("./key_leak.trunc", "w") as fd:
        for line in new_lines:
            fd.write(line)
    



if __name__ == "__main__":
    main()
