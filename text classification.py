import pandas as pd

# Define Keywords
keywords_nature = {''}
keywords_policy = {''}
keywords_supply = {''}
keywords_demand = {''}

def classify_sentiment(file_path, column_name, output_file):
    df = pd.read_excel(file_path, engine='openpyxl')

    if column_name not in df.columns:
        print(f"Column {column_name} does not exist in the Excel file.")
        return

    df[''] = None

    for index, row in df.iterrows():
        text = str(row[column_name])
        classification = [0, 0, 0, 0]

        if any(keyword in text for keyword in keywords_nature):
            classification[0] = 1

        if any(keyword in text for keyword in keywords_policy):
            classification[1] = 1

        if any(keyword in text for keyword in keywords_supply):
            classification[2] = 1

        if any(keyword in text for keyword in keywords_demand):
            classification[3] = 1

        df.at[index, ''] = classification

    df.to_excel(output_file, index=False)

file_path = '.xlsx'
column_name = ''
output_file = '.xlsx'
classify_sentiment(file_path, column_name, output_file)
print(f"Classification results have been saved to {output_file}")
