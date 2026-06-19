from random import random

def sampling_fn(x):

    return x * x

if __name__ == "__main__":

    N_SAMPLES = 5000
    total = 0
    for i in range(N_SAMPLES):

        x = 2 + random()
        
        total += sampling_fn(x)


    total /= N_SAMPLES
    print(total, 1/3 * (3**3 - 2**3))
        
    

