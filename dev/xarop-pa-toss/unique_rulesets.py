import os
import ast

ruleset_names = set()

for filename in os.listdir("."):
    if filename.endswith(".txt"):
        try:
            with open(filename, "r", encoding="utf-8") as f:
                content = f.read()
                data = ast.literal_eval(content)
                ruleset = data.get("ruleset")
                if ruleset and "name" in ruleset:
                    ruleset_names.add(str(ruleset["id"]) + ": " + ruleset["name"])
        except Exception as e:
            print(f"Error in {filename}: {e}")

with open("unique_rulesets.txt", "w", encoding="utf-8") as out_file:
    for name in sorted(ruleset_names):
        out_file.write(name + "\n")
