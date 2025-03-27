import os
from deep_translator import GoogleTranslator

input_folder = "Document Collection Original Language"
output_folder = "Document Collection Translated"

translator = GoogleTranslator(source="de", target="en")

os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    if filename.endswith(".txt"):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename.replace(".txt", "_en.txt"))

        with open(input_path, "r", encoding="utf-8") as file:
            text = file.read()

        translated_text = translator.translate(text)

        with open(output_path, "w", encoding="utf-8") as file:
            file.write(translated_text)

        print(f"✅ Translated: {filename} → {output_path}")

print("🎉 All txt files were translated successfully!!!")