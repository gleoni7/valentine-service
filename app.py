import time
from dataclasses import dataclass

@dataclass
class CompatibilityResult:
 chemistry: bool
 shared_humor: bool
 communication: bool
 trust: bool
 conclusion: str

def run_checks():
 checks = {
     "chemistry": True,
     "shared_humor": True,
     "communication": True,
     "trust": True
 }

 for check in checks:
     print(f"Running {check.replace('_', ' ')} check...")
     time.sleep(0.7)

 return checks

def evaluate(checks):
 if all(checks.values()):
     return CompatibilityResult(
         **checks,
         conclusion="Proceed"
     )
 return CompatibilityResult(**checks, conclusion="Re-evaluate")

def main():
 print("Starting Valentine Service...\n")
 time.sleep(1)

 checks = run_checks()
 result = evaluate(checks)

 print("\nEvaluation complete.")
 print(f"Conclusion: {result.conclusion}\n")

 if result.conclusion == "Proceed":
     time.sleep(0.5)
     print("Final Action Required:")
     print(">>> Would you like to be my Valentine?\n")
     print("[1] Yes")
     print("[2] Yes (obviously)")

     choice = input("\nSelect option: ")

     if choice in ["1", "2"]:
         print("\nRequest accepted 💖")
         print("Service scheduled for February 14.")
     else:
         print("\nInvalid input.")
         print("Please restart service.")

if __name__ == "__main__":
 main()

# TODO: never refactor this relationship
