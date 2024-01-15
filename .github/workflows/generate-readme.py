import os
import json


def read_file_tree(path: str) -> dict:
    dic = {}
    dic[path] = []

    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isdir(item_path):
            dic[path].append(read_file_tree(item_path))
        else:
            dic[path].append(item_path)

    # sort: alphabetical order
    dic[path].sort(key=lambda x: x if type(x) == str else list(x.keys())[0])

    # sort: directories first
    dic[path].sort(key=lambda x: type(x) == str)
    return dic


def filter_file_tree(dic: dict) -> dict:
    is_valid_file = lambda x: type(x) == str and x.endswith(".md") or x.endswith(".pdf")

    output = {}

    for key, value in dic.items():
        assert type(value) == list
        new_value = []

        for v in value:
            if type(v) == dict:
                subdic = filter_file_tree(v)
                new_value.append(subdic) if subdic else None
            elif is_valid_file(v):
                new_value.append(v)

        if new_value:
            output[key] = new_value

    return output


def dic_to_markdown(dic: dict, indent: int = 0) -> str:
    output = ""
    get_filename = lambda x: x.split("/")[-1].split(".")[0]

    for _, value in dic.items():
        assert type(value) == list
        for v in value:
            if type(v) == dict:
                dictname = list(v.keys())[0]
                output += "\t" * indent + "- " + get_filename(dictname) + "\n"
                output += dic_to_markdown(v, indent + 1)
            else:
                output += "\t" * indent + f"- [{get_filename(v)}](<{v}>)\n"

    return output


def main():
    if os.path.isfile("README.md"):
        os.remove("README.md")

    dic = read_file_tree(".")
    dic = filter_file_tree(dic)
    print(json.dumps(dic, indent=1))
    toc = dic_to_markdown(dic)

    with open("README.md", "w") as f:
        f.write("## sueszli's blog")
        f.write("\n\n")
        f.write(
            "welcome to my minimalist blog, built with nothing but markdown and github actions."
        )
        f.write("\n\n")
        f.write(
            "to stay up to date with new posts subscribe via github: [https://github.com/sueszli/blog/subscription](https://github.com/sueszli/blog/subscription)"
        )
        f.write("\n\n")
        f.write("<br>")
        f.write("\n\n")
        f.write("_file tree:_")
        f.write("\n\n")
        f.write(toc)


if __name__ == "__main__":
    main()
