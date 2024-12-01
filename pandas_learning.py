import pandas as pd
import numpy as np
from datetime import date

promodataframe = pd.DataFrame(
    {
        #"ID" : 1,
        "Due Date" : date(2024, 11, 28),
        "Monthly Payment" : float(21.32)
    }
    , index=[1]
)

new_promo = pd.Series ({
    "Due Date" : date(2024, 12, 28),
    "Monthly Payment" : float(21.58)
})

pd.concat([promodataframe, new_promo.to_frame().T], ignore_index=True)

print(promodataframe)

