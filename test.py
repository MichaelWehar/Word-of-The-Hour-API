from woth_api import WothAPI

# Get current word of the hour
woth_data = WothAPI.fetch()

# Print current word
print("----- TEST 1 -----")
print("word: " + woth_data["word"])

# Print German translation if it exists
print("----- TEST 2 -----")
if "german" in woth_data["translations"]:
    print("german: " + woth_data["translations"]["german"])

# Print all translations
print("----- TEST 3 -----")
translations = woth_data["translations"]
for field in sorted(translations):
    print(field + ": " + translations[field])

# Print all definitions
print("----- TEST 4 -----")
definitions = woth_data["definitions"]
for field in sorted(definitions):
    definitions_list = definitions[field]
    for i in range(0, len(definitions_list)):
        print(field + " " + str(i) + ": " + definitions_list[i])
