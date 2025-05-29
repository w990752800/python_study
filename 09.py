
# 彩票

import random

from rich.console import Console
from rich.table import Table




console = Console()

n = int(input("生成几注号码："))
red_balls = [i for i in range(1, 34)]
blue_balls = [i for i in range(1, 17)]

# 创建表格并添加表头
table = Table(show_header=True)
for col_name in ("序号", "红球", "篮球"):
    table.add_column(col_name)

for i in range(n):
    selected_balls = random.sample(red_balls, 6)
    selected_balls.sort()
    blue_ball = random.choice(blue_balls)
    table.add_row(
        str(i + 1),
        f'[red]{" ".join([f"{ball:0>2d}" for ball in selected_balls])}[/red]',
        f'[blue]{blue_ball:0>2d}[/blue]'
    )

console.print(table)