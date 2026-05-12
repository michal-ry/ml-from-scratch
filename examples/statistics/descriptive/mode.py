import pandas as pd
from ml_from_scratch.statistics.descriptive.mode import mode as fs_mode

def mode_example():

    '''
    Compare mode from scratch vs Pandas.
    '''

    names = ["Michael", "Natalia", "Agata", "Daniel", "Michael",
             "Sophia", "Lucas", "Agata", "Olivia", "Jacob"]
    
    from_scratch_mode = fs_mode(names)
    pd_mode = pd.Series(names).mode().tolist()
    
    print(f'Mode using function from scratch: {from_scratch_mode}')
    print(f'Mode using Pandas: {pd_mode}')

if __name__ == '__main__':
    mode_example()