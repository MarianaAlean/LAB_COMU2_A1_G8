###### DIFERENCIADOR

import numpy as np
from gnuradio import gr

class blk(gr.sync_block): 
    def __init__(self):  
        gr.sync_block.__init__(
            self,
            name='e_Diff', 
            in_sig=[np.float32],
            out_sig=[np.float32]
        )

    def work(self, input_items, output_items):
        x = input_items[0]
        y0 = output_items[0]

        diff = np.empty_like(x)
        diff[0] = 0          # Inicializamos el primer elemento
        diff[1:] = x[1:] - x[:-1]  # Diferencia entre cada muestra y su predecesora
        
        y0[:] = diff
        return len(y0)

