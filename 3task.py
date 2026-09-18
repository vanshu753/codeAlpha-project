import os
import shutil

def create_folders():
    if not os.path.exists("source"):
        os.makedirs("source")

    if not os.path.exists("destination"):
        os.makedirs("destination")


def show_files():
    files = os.listdir("source")

    if not files:
        print("Source folder is empty.")
        return

    print("\nFiles in source folder:")

    for file in files:
        print("-", file)


def move_images():
    files = os.listdir("source")
    moved = 0

    for file in files:
        if file.lower().endswith(".jpg"):
            source_path = os.path.join("source", file)
            destination_path = os.path.join("destination", file)

            if os.path.isfile(source_path):
                shutil.move(source_path, destination_path)
                print("Moved:", file)
                moved += 1

    print("\nTotal JPG files moved:", moved)


def main():
    create_folders()

    while True:
        print("\n----- JPG File Manager -----")
        print("1. Show files")
        print("2. Move JPG files")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            show_files()

        elif choice == "2":
            move_images()

        elif choice == "3":
            print("Program closed.")
            break

        else:
            print("Invalid choice.")


main()