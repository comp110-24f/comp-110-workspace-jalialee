"""First CQ in COMP110: Function"""

__author__ = "730489841"


def mimic(message: str) -> str:
    """Taking input and repeating it back"""
    return message


def main() -> None:
    """Pulls together your functions"""
    print(mimic(message=input("What is your message?")))


if __name__ == "__main__":
    main()
    