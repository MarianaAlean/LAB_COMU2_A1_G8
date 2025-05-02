###ACUMULADOR
import numpy as np
from gnuradio import gr

class blk(gr.sync_block):
    def __init__(self):
        gr.sync_block.__init__(
            self,
            name='e_Acum',
            in_sig=[np.float32],
            out_sig=[np.float32]
        )
        self.state = 0  # Valor inicial del acumulador

    def work(self, input_items, output_items):
        x = input_items[0]
        y0 = output_items[0]
        
        # Calcula la suma acumulada del bloque actual y añade el estado previo.
        acc = np.cumsum(x) + self.state
        
        # Actualiza el estado para la próxima llamada.
        self.state = acc[-1]
        
        y0[:] = acc
        return len(y0)
