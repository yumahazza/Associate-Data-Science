with open("contoh.txt", "w") as file:
    file.write("Halo, namaku Yuma")

with open("contoh.txt", "r") as file:
    content = file.read()
    print(content)

with open("contoh.txt", "a") as file:
    file.write("\nAku suka belajar Python.")