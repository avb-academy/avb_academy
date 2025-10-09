from collections import OrderedDict

def smart_title(s):
    """
    Convert words to title case only if they are not already fully uppercase.
    """
    return " ".join(word if word.isupper() else word.capitalize() for word in s.split())

# Function to read a simple YAML file
def read_yaml(filepath):
    data = {}
    with open(filepath, "r", encoding="utf-8") as f:
        current_key = None
        for line in f:
            line = line.rstrip()
            if not line or line.startswith("#"):
                continue
            if not line.startswith(" "):  # Top-level key
                current_key = line.rstrip(":")
                data[current_key] = {}
            else:  # Nested key
                if current_key:
                    nested_key, nested_value = line.strip().split(":", 1)
                    data[current_key][nested_key.strip()] = nested_value.strip().strip('"')
    return data

# Function to write a simple YAML file
def write_yaml(filepath, data):
    with open(filepath, "w", encoding="utf-8") as f:
        for key, subdict in data.items():
            f.write(f"{key}:\n")
            for subkey, value in subdict.items():
                f.write(f"  {subkey}: \"{value}\"\n")
            f.write("\n")

# Load YAML
filepath = "data/termbase.yaml"
termbase = read_yaml(filepath)

# Apply smart title-casing to top-level keys and sort alphabetically
sorted_termbase = OrderedDict(
    sorted(((smart_title(k), v) for k, v in termbase.items()), key=lambda item: item[0])
)

# Write back to YAML
write_yaml(filepath, sorted_termbase)
