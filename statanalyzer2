import math

class StatsAnalyzer:
    def __init__(self, numbers):
        self.numbers = numbers

    def calculate_mean(self):
        total = 0
        for num in self.numbers:
            total += num
        return total / len(self.numbers)

    def calculate_std_dev(self):
        mean = self.calculate_mean()
        variance = 0
        for num in self.numbers:
            variance += (num - mean) ** 2
        std_dev = math.sqrt(variance / len(self.numbers))
        return std_dev

    def write_summary(self, file_path):
        try:
            file = open(file_path, "w")
            file.write(f"Mean: {self.calculate_mean()}\n")
            file.write(f"Standard Deviation: {self.calculate_std_dev()}\n")
            file.close()
        except:
            print("An error occurred during writing.")

def main():
    data = [12, 15, 12, 14, 13, 15, 14, 13]
    analyzer = StatsAnalyzer(data)
    analyzer.write_summary("summary.txt")

if __name__ == "__main__":
    main()
