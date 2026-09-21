import json
from pathlib import Path


def main() -> None:
    events_path = Path(__file__).with_name("events.json")
    events = json.loads(events_path.read_text(encoding="utf-8"))
    critical_events = [event for event in events if event.get("level") == "critical"]

    for event in critical_events:
        print(json.dumps(event, ensure_ascii=False))
    print(f"критичных {len(critical_events)}")


if __name__ == "__main__":
    main()