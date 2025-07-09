import crop_model
import os
import json

def main():
    here = os.path.dirname(__file__)
    in_path = os.path.join(here, "input_data.json")
    with open(in_path, "r") as f:
        input_data = json.load(f)

    #Run model
    results = crop_model.run_simulation(input_data)

    out_path = os.path.join(here, "output_data.json")
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2)

    print(f"Results written to {out_path}")

if __name__ == "__main__":
    main()