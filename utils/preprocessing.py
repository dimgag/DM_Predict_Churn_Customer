import pandas as pd
import argparse


parser = argparse.ArgumentParser(description='Preprocess data')
parser.add_argument('--data', type=str, default='data.csv', help='path to data')
parser.add_argument('--output', type=str, default='data_processed.csv', help='path to output')
args = parser.parse_args()


def main():
    # Read data
    df = pd.read_csv(args.data)

    # Data Preprocessing:
    # Fix datatypes
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'],errors='coerce')
    # Convert Churn values and datatype from categorical to binary. Replacing Yes with 1 and No with 0.
    df['Churn'] = df['Churn'].replace({'Yes':1,'No':0})
    df['SeniorCitizen'] = df['SeniorCitizen'].replace({0:'No',1:'Yes'})
    df['SeniorCitizen'] = df['SeniorCitizen'].astype('object')
    # Drop empty columns
    df.dropna(inplace = True)

    # Export data
    df.to_csv(args.output, index=False)


if __name__ == '__main__':
    main()

# Example usage:
# python utils/preprocessing.py --data data.csv --output data_processed.csv