def get_word_count(text: str):
    return len(text.split())

def get_character_counts(text: str) -> dict[str,int]:
    text = text.lower()
    character_counts = {}

    for char in text:
        if char in character_counts:
            character_counts[char] += 1
        else:
            character_counts[char] = 1

    return character_counts

def get_sorted_character_counts(raw_counts: dict[str,int]):
    sorted_counts = []

    for char,count in raw_counts.items():
        sorted_counts.append({
            "character": char,
            "count": count,
        })

    def sort_on(dict):
        return dict['count']

    sorted_counts.sort(reverse=True, key=sort_on)

    return sorted_counts


