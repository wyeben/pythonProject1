import time
import sys


def draw_progress_bar(iteration, total, bar_length=50):
    percent = iteration / total
    arrow = '=' * int(round(percent * bar_length) - 1)
    spaces = ' ' * (bar_length - len(arrow))

    sys.stdout.write(f'\r[{arrow}{spaces}] {int(percent * 100)}%')
    sys.stdout.flush()


def progress_bar_animation():
    total_iterations = 25
    for i in range(total_iterations + 1):
        draw_progress_bar(i, total_iterations)
        time.sleep(0.2)


progress_bar_animation()
print()
