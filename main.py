import os
import sys

output_dir = "/output"
entry_file = os.path.join(output_dir, "entry.txt")

os.makedirs(output_dir, exist_ok=True)

strategy = "pumpfun_simple_momentum_buy_hold"
description = "Buy $PAID tokens during the first 30m window, hold 6h, sell at first 20% gain or cutoff. Pure paper-trade forward window strategy."
content = f"{strategy} | {description}"

with open(entry_file, "w") as f:
    f.write(content)