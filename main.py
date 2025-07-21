
from module.speech_to_text import convert_speech_to_text
from module.image_describer import describe_image
from module.doc_reader import read_text_from_image



def main():
    print("\n=== One For All: AI Accessibility Assistant ===")
    print("1. Convert Speech to Text")
    print("2. Describe Image")
    print("3. Read Document")
    print("0. Exit")

    while True:
        choice = input("\nEnter your choice (0-3): ")

        if choice == '1':
            path = input("Enter path to audio file (default: assets/sample_inputs/sample.wav): ")
            if not path.strip():
                path = "assets/sample_inputs/"
            convert_speech_to_text(path)

        elif choice == '2':
            path = input("Enter path to image file (default: assets/sample_inputs/sampleimg.jpg): ")
            if not path.strip():
                path = "assets/sample_inputs/sampleimg.jpg"
            describe_image(path)

        elif choice == '3':
            path = input("Enter path to image (default: assets/sample_inputs/sample_doc.png): ")
            if not (path.endswith(".png") or path.endswith(".jpg") or path.endswith(".jpeg")):
                print("Unsupported format. Please use PNG or JPG images.")
            else:
                read_text_from_image(path)
          #  if not path.strip():
           #     path = "assets/sample_inputs/sample_doc.jpeg"
           # read_text_from_image(path)

        elif choice == '0':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
