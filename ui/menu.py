from data_structure.vec_dequeue import VecDequeue


def menu(title: str, options: VecDequeue[str]) -> int:
    prompt = f"Choose 1 option from 1 to {len(options)}: "

    while True:
        print()
        print(title)
        index = 0
        for option in options:
            # 1-based list
            print(f"{index + 1}. {option}")
            index += 1
        choosen = int(input(prompt))
        if 1 <= choosen and choosen <= len(options):
            return choosen - 1
