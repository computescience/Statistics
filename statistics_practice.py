import math
import os
import random
import re
import sys

class stats():
    def median(data):
        n = len(data)

        if n % 2 == 0:
            f = round((data[n // 2] + data[n // 2 - 1]) / 2, 1)
        else:
            f = float(data[n // 2])
        return f


    def quartiles(arr):
        # Write your code here
        arr = sorted(arr)
        print(arr)

        x = len(arr)
        mid = x // 2

        if x % 2 != 0:
            q2 = arr[mid]
            l = arr[0:mid]
            r = arr[mid + 1:x]
            q1 = median(l)
            q3 = median(r)

        else:

            m = arr[mid - 1:mid + 1]
            q2 = round(sum(m) / 2, )
            l = arr[0:mid]
            r = arr[mid:x]
            q1 = median(l)
            q3 = median(r)
        return q1, q2, q3


    def interQuartile(values, freqs):
        # Print your answer to 1 decimal place within this function
        data = []
        for i, j in zip(values, freqs):
            for k in range(j):
                data.append(i)

        q1, q2, q3 = quartiles(data)
        inter = q3 - q1
        print(inter)
        return inter

    def conditionProb(observed_prob,pred_accuracy):
        Pa = observed_prob
        Pac = 1 - observed_prob
        Pb = pred_accuracy
        Pbc = 1 - pred_accuracy

        P = Pa * Pb/(Pa*Pb + Pac * Pbc)
        print(P)
        return P

####
#values=[10, 40 ,30, 50 ,20 ,10, 40 ,30, 50 ,20 ,1, 2 ,3 ,4 ,5, 6 ,7 ,8 ,9 ,10 ,20 ,10 ,40 ,30 ,50, 20 ,10, 40, 30, 50]
#freqs = [1 ,2, 3, 4 ,5, 6 ,7, 8, 9 ,10 ,1 ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9, 10 ,10 ,40, 30, 50, 20 ,10, 40 ,30 ,50 ,20]
#interQuartile(values, freqs)
###

#conditionProb(5/365,9/10)
