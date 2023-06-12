#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4

    for s in sorted(dir(hidden_4)):
        if s[0] != '_':
            print(s)
