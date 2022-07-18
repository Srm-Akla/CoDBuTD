#!/usr/bin/env python

try:
    from GPIO import gpio
except ImportError:
    print("Trouble importing, did you install the packages or do files exist?")
    exit(1)

if __name__ == "__main__":
    gpio().listen()
