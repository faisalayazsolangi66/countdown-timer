#!/usr/bin/env python3
"""Count down to a date and time."""
import argparse
import sys
import time
from datetime import datetime


def parse_target(value):
    """Accept 'YYYY-MM-DD HH:MM', 'YYYY-MM-DD', or a number of seconds."""
    value = value.strip()
    for fmt in ("%Y-%m-%d %H:%M:%S", "%Y-%m-%d %H:%M", "%Y-%m-%d"):
        try:
            return datetime.strptime(value, fmt)
        except ValueError:
            continue
    try:
        seconds = float(value)
    except ValueError:
        raise argparse.ArgumentTypeError(
            "target must be 'YYYY-MM-DD HH:MM', 'YYYY-MM-DD', or seconds")
    if seconds < 0:
        raise argparse.ArgumentTypeError("seconds must not be negative")
    return datetime.now().timestamp() + seconds


def fmt_delta(seconds):
    seconds = max(0, int(seconds))
    days, rem = divmod(seconds, 86400)
    hours, rem = divmod(rem, 3600)
    mins, secs = divmod(rem, 60)
    parts = []
    if days:
        parts.append(f"{days}d")
    parts.append(f"{hours:02d}:{mins:02d}:{secs:02d}")
    return " ".join(parts)


def main():
    parser = argparse.ArgumentParser(description="Count down to a date and time.")
    parser.add_argument("target", type=parse_target,
                        help="Target: 'YYYY-MM-DD HH:MM', 'YYYY-MM-DD', "
                             "or seconds from now (e.g. 10)")
    parser.add_argument("--label", default="Countdown",
                        help="Label shown while counting down")
    parser.add_argument("--interval", type=float, default=1.0,
                        help="Refresh interval in seconds (default: 1)")
    parser.add_argument("--once", action="store_true",
                        help="Print the remaining time once and exit")
    args = parser.parse_args()

    if isinstance(args.target, datetime):
        end = args.target.timestamp()
        target_str = args.target.strftime("%Y-%m-%d %H:%M:%S")
    else:
        end = args.target
        target_str = "in a few seconds"
    remaining = end - time.time()
    if remaining <= 0:
        print("That time is already in the past.")
        sys.exit(1)
    print(f"{args.label} to {target_str}: {fmt_delta(remaining)}")
    if args.once:
        return
    try:
        while True:
            remaining = end - time.time()
            if remaining <= 0:
                break
            print(f"\r{args.label}: {fmt_delta(remaining)}",
                  end="", flush=True)
            time.sleep(args.interval)
    except KeyboardInterrupt:
        print("\nCountdown stopped.")
        sys.exit(130)
    print(f"\n{args.label} reached! Time's up.")


if __name__ == "__main__":
    main()
