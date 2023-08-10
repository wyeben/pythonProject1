import time
import sys


def rotating_circle_animation():
    animation_frames = ["🇨🇦", "🇳🇬", "🇺🇸", "🏴󠁧󠁢󠁥󠁮󠁧󠁿"]

    iterations = 15
    for i in range(iterations):
        sys.stdout.write("\r" + animation_frames[i % len(animation_frames)])
        sys.stdout.flush()
        time.sleep(1)


def main():
    print("Loading ")
    rotating_circle_animation()


if __name__ == "__main__":
    main()
