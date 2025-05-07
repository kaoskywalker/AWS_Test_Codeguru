import time

class DataProcessor:
    def __init__(self, data):
        self.data = data
        self.cleaned_data = []

    def remove_duplicates(self):
        temp = []
        for item in self.data:
            if item not in temp:
                temp.append(item)
        self.cleaned_data = temp

    def sort_data(self):
        self.cleaned_data.sort()

    def save_to_file(self, filename):
        try:
            f = open(filename, 'w')
            for item in self.cleaned_data:
                f.write(str(item) + '\n')
            f.close()
        except Exception as e:
            print("Error writing to file:", e)

    def simulate_heavy_processing(self):
        print("Starting heavy processing...")
        for i in range(5):
            time.sleep(1)  # Simulate time-consuming task
            print(f"Processing step {i+1} complete")

    def run(self, output_file):
        print("Running data processor...")
        self.remove_duplicates()
        self.sort_data()
        self.simulate_heavy_processing()
        self.save_to_file(output_file)
        print("Data processing complete.")

def main():
    sample_data = ["apple", "banana", "apple", "cherry", "banana", "date", "fig", "grape", "fig"]
    processor = DataProcessor(sample_data)
    processor.run("output.txt")

if __name__ == "__main__":
    main()
