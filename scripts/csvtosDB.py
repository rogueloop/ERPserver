import csv

# Open the input CSV file and create a new output CSV file
with open('material_list.csv', 'r') as input_file, open('output.csv', 'w', newline='') as output_file:
    # Create a CSV reader and writer objects
    reader = csv.reader(input_file)
    writer = csv.writer(output_file)

    # Iterate over each row in the input CSV file
    for row in reader:
        # Create a new row with each cell's trailing whitespace removed
        cleaned_row = [cell.strip() for cell in row]

        # Write the cleaned row to the output CSV file
        writer.writerow(cleaned_row)