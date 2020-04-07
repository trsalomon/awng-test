#!/usr/bin/env python3
# coding: utf-8

def fibonacci(n):
    """ suite de fibonacci """
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def main():
    for i in range(12):
        i, fibonacci(i)

if __name__ == '__main__':
    main()