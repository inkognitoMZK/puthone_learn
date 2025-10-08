def count_protocols(file_path):
    counts = {"NEC": 0, "SHARP": 0, "SONY": 0}

    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            for protocol in counts.keys():
                if protocol in line:
                    counts[protocol] += 1
                    
    return counts

if __name__ == "__main__":
    result = count_protocols("Demo.log")

    for protocol, count in result.items():
        print(f"{protocol}: {count}")
