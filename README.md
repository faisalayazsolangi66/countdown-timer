# countdown-timer

Count down to a date and time.

Give a target date/time (`YYYY-MM-DD HH:MM`), a date alone, or a
number of seconds from now. The timer refreshes every second until
the target is reached. Press Ctrl+C to stop early.

## Requirements

- Python 3
- No third-party packages

## How to run

```bash
python3 main.py "2026-12-04 18:00" [--label "Mehndi"] [--once]
python3 main.py 10
```

## Example

```bash
python3 main.py 2 --label "Test"
```

Sample output:

```
Test to in a few seconds: 00:00:02
Test: 00:00:01
Test reached! Time's up.
```

## License

MIT — see `LICENSE`.
