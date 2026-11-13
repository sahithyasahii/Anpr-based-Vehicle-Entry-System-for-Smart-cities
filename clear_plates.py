import re
import pandas as pd

#Load OCR output from file
input_file = "carplates_toclear.txt"  # Make sure this file is in the same directory
with open(input_file, "r", encoding="utf-8") as f:
    ocr_lines = f.readlines()

# Extract only plate text
plates = []
for line in ocr_lines:
    match = re.search(r"→ (.+)", line)
    if match:
        text = match.group(1).strip()
        if text and text.lower() != "no text detected":
            plates.append(text)

print(f"Total Plates Detected: {len(plates)}")

# Filter noise / invalid plates
cleaned_plates = []
for plate in plates:
    if (
        4 <= len(plate) <= 10 and  # typical license plate length
        plate.isalnum() and        # remove symbols
        not plate.isdigit() and    # filter all-digit (if not needed)
        not plate.isalpha()        # filter all-letters (optional)
    ):
        cleaned_plates.append(plate.upper())  # Convert to uppercase

print(f"Cleaned Plates Count: {len(cleaned_plates)}")

# Remove duplicates
unique_plates = sorted(set(cleaned_plates))
print(f"Unique Plates Count: {len(unique_plates)}")

#Save to TXT file
with open("cleaned_plates.txt", "w", encoding="utf-8") as f:
    for plate in unique_plates:
        f.write(f"{plate}\n")

print("✅ Cleaned license plates saved to 'cleaned_plates.txt'")

# Save to CSV file 
df = pd.DataFrame(unique_plates, columns=["License_Plate"])
df.to_csv("cleaned_plates.csv", index=False)
print("✅ Cleaned license plates saved to 'cleaned_plates.csv'")
