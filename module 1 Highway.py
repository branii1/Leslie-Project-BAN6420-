import random

# Define a simple Worker class to hold worker details
class Worker:
    def __init__(self, worker_id, name, gender, salary):
        self.worker_id = worker_id
        self.name = name
        self.gender = gender
        self.salary = salary
        self.level = self.assign_level()
    
    # Method to assign employee level based on salary and gender
    def assign_level(self):
        try:
            if 10000 < self.salary < 20000:
                return "A1"
            elif 7500 < self.salary < 30000 and self.gender.lower() == "female":
                return "A5-F"
            else:
                return "Unknown"
        except Exception as e:
            print(f"Error in assigning level for worker {self.worker_id}: {e}")
            return "Error"

    # Method to generate payment slip for the worker
    def generate_payment_slip(self):
        try:
            slip = f"Payment Slip for {self.name} (ID: {self.worker_id}):\n"
            slip += f"Gender: {self.gender}\n"
            slip += f"Salary: ${self.salary}\n"
            slip += f"Employee Level: {self.level}\n"
            return slip
        except Exception as e:
            print(f"Error in generating payment slip for worker {self.worker_id}: {e}")
            return "Error generating payment slip"

# Function to create a list of workers dynamically
def create_workers(num_workers=400):
    workers = []
    names = ["Kwadwo", "Kwabena", "Abena", "Nana", "Yaa", "Akosua", "Obeng", "Kwasi", "Esi", "Kwaku"]
    for i in range(1, num_workers + 1):
        name = random.choice(names)
        gender = random.choice(["Male", "Female"])
        salary = random.randint(5000, 35000)
        workers.append(Worker(worker_id=i, name=name, gender=gender, salary=salary))
    return workers

# Main function to create workers and generate payment slips
def main():
    workers = create_workers()
    for worker in workers:
        print(worker.generate_payment_slip())

if __name__ == "__main__":
    main()
