import numpy as np
import pandas as pd
def np_exercise1():
    heights = [189, 170, 189, 163, 183, 171, 185, 168, 
                173, 183, 173, 173, 175, 178, 183, 193,
                178, 173, 174, 183, 183, 180, 168, 180, 
                170, 178, 182, 180, 183, 178, 182, 188, 
                175, 179, 183, 193, 182, 183, 177, 185, 188, 188, 182, 185, 191]
    ages = [57, 61, 57, 57, 58, 57, 61, 54, 68, 51, 49, 
            64, 50, 48, 65, 52, 56, 46, 54, 49, 51, 47,
            55, 55, 54, 42, 51, 56, 55, 51, 54, 51, 60, 
            62, 43, 55, 56, 61, 52, 69, 64, 46, 54, 47, 70]
    heights_trats = np.array(heights)
    ages_trats = np.array(ages)
        
    presidents = np.concatenate((heights_trats.reshape((45,1)), ages_trats.reshape((45,1))), axis=1)
    mask = presidents[:,0] >= 182
    tall_presidents = presidents[mask,]
    mask_age = presidents[:, 1] < 50
    young_presidents = presidents[mask_age,]
    mask_total = (presidents[:,0] >=182) & (presidents[:,1] <50)
    especific_presidents = presidents[mask_total,]
    print(especific_presidents)




def main():
    np_exercise1()

if __name__ == '__main__':
    main()
    