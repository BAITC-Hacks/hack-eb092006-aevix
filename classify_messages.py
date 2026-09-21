from pathlib import Path


def classify(message: str) -> tuple[str, str]:
    text = message.lower()

    if any(word in text for word in ("жалоб", "очередь", "холодн", "пропал")):
        return "жалоба", "Спасибо за сообщение. Мы передадим информацию ответственным сотрудникам."
    if any(word in text for word in ("как", "где", "справк")):
        return "справка", "Подскажите, пожалуйста, дополнительные детали, и мы поможем сориентироваться."
    return "другое", "Спасибо за обращение. Мы уточним возможность и вернёмся с ответом."


def main() -> None:
    messages_path = Path(__file__).with_name("messages.txt")
    for message in messages_path.read_text(encoding="utf-8").splitlines():
        if message.strip():
            category, reply = classify(message)
            print(f"Обращение: {message}")
            print(f"Категория: {category}")
            print(f"Ответ: {reply}\n")


if __name__ == "__main__":
    main()