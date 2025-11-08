import re
from colorama import init, Fore
import os

# Initialize colorama for Windows PowerShell/Terminal
init(autoreset=True)

# File to save URL history
history_file = "url_history.txt"

# Load history from file if exists
tested_urls = []
if os.path.exists(history_file):
    with open(history_file, "r") as f:
        for line in f:
            line = line.strip()
            if line:
                url, prediction, prob = line.split(" | ")
                tested_urls.append((url, prediction, float(prob)))


def save_to_file(url, prediction, probability):
    # Save in UTF-8 encoding and remove any special characters like arrows
    with open(history_file, "a", encoding="utf-8") as f:
        f.write(f"{url} | {prediction} | {probability:.2f}\n")


def predict_url(url):
    """
    Simple phishing detector simulation
    """
    legit_domains = ["google.com", "github.com", "microsoft.com", "facebook.com", "linkedin.com"]
    phishing_keywords = ["login", "verify", "update", "secure", "banking", "account", "appleid"]

    if any(domain in url for domain in legit_domains):
        prediction = "LEGITIMATE"
        probability = 0.95
        print(Fore.GREEN + f"\n[✔] RESULT: {prediction} (Confidence: {probability:.2f})\n")
    elif any(word in url.lower() for word in phishing_keywords):
        prediction = "PHISHING"
        probability = 0.87
        print(Fore.RED + f"\n[✘] RESULT: {prediction} (Confidence: {probability:.2f})\n")
    else:
        prediction = "LEGITIMATE"
        probability = 0.80
        print(Fore.GREEN + f"\n[✔] RESULT: {prediction} (Confidence: {probability:.2f})\n")
    
    # Save the result to file and history
    save_to_file(url, prediction, probability)
    tested_urls.append((url, prediction, probability))


def show_history():
    """
    Show all tested URLs in this session
    """
    print(Fore.CYAN + "\n===== URL TEST HISTORY =====")
    if not tested_urls:
        print("No URLs tested yet.")
    else:
        for idx, (url, prediction, prob) in enumerate(tested_urls, start=1):
            color = Fore.GREEN if prediction == "LEGITIMATE" else Fore.RED
            print(color + f"{idx}. {url} → {prediction} (Conf: {prob:.2f})")
    print(Fore.CYAN + "============================\n")


if __name__ == "__main__":
    print(Fore.YELLOW + "🚀 Simple Phishing Detector with Persistent History 🚀\n")
    print("Type a URL to test, 'history' to see tested URLs, or 'exit' to quit.\n")

    while True:
        url = input(Fore.YELLOW + "Enter a URL: ").strip()

        if url.lower() == "exit":
            print(Fore.MAGENTA + "\n👋 Exiting... Stay safe online!")
            break
        elif url.lower() == "history":
            show_history()
        elif url:
            predict_url(url)