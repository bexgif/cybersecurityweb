import itertools


def load_terms(path: str = "terms.txt", max_terms: int = 35) -> list[str]:
    terms = []
    seen = set()

    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            term = line.strip().lower()
            if not term:
                continue
            if term in seen:
                continue
            seen.add(term)
            terms.append(term)
            if len(terms) >= max_terms:
                break

    if not terms:
        raise ValueError("terms.txt is empty or missing")

    return terms


def starts_with_letter(term: str) -> bool:
    return term and term[0].isalpha()

def generate_usernames(terms: list[str]) -> list[str]:
    return sorted(t for t in terms if starts_with_letter(t))


def generate_passwords_level1(terms: list[str]) -> list[str]:
    letter_terms = [t for t in terms if starts_with_letter(t)]
    return [a + b for a, b in itertools.permutations(letter_terms, 2)]


def generate_passwords_level2(terms: list[str]) -> list[str]:
    return [a + b for a, b in itertools.permutations(terms, 2)]

def write_list(path: str, items: list[str]) -> None:
    with open(path, "w", encoding="utf-8") as f:
        for item in items:
            f.write(item + "\n")

if __name__ == "__main__":
    terms = load_terms("terms.txt", max_terms=35)

    usernames_l1 = generate_usernames(terms)
    passwords_l1 = generate_passwords_level1(terms)

    usernames_l2 = usernames_l1[:]
    passwords_l2 = generate_passwords_level2(terms)

    print(f"Terms loaded: {len(terms)}")
    print(f"Level 1 usernames: {len(usernames_l1)}")
    print(f"Level 1 passwords: {len(passwords_l1)}")
    print(f"Level 2 usernames: {len(usernames_l2)}")
    print(f"Level 2 passwords: {len(passwords_l2)}")

    write_list("usernames_level1.txt", usernames_l1)
    write_list("passwords_level1.txt", passwords_l1)
    write_list("usernames_level2.txt", usernames_l2)
    write_list("passwords_level2.txt", passwords_l2)

    print("\nOutput files written:")
    print("  usernames_level1.txt")
    print("  passwords_level1.txt")
    print("  usernames_level2.txt")
    print("  passwords_level2.txt")
