import json

def load_jsonl(path):
    data = []
    with open(path, "r") as f:
        for line in f:
            data.append(json.loads(line))
    return data

if __name__ == "__main__":
    data = load_jsonl("data/annotations/annotated_data.jsonl")
    print(data[:3])
