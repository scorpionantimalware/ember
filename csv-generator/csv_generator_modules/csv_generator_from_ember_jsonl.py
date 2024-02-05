import os
import json
import csv
from typing import List, Any

class CSVGeneratorFromEmberJSONL:
    def __init__(self, features: List[str]):
        """
        EMBER dataset consists of Json Lines (.jsonl) files. Each line in the file is a JSON object.
        This class is used to extract the required features from the JSON object and generate a CSV file.

        Args:
        features (List[str]): List of features to be extracted from the JSON object.
        """
        # Add the target feature to the list of features
        # Remove the target feature from the list of features if it is already present
        # Add the target feature to the end of the list
        target = "label"
        if target in features:
            features.remove(target)

        features.append(target)

        self._features = features

    def extract_and_generate(self, file_path) -> None:
        """
        Extract the features from the JSON object and generate a CSV file.

        Args:
        file_path (str): Path to the JSONL file.
        """
        if not self.check_file_path(file_path):
            print("File not found")
            return
        
        csv_file_path = os.path.splitext(file_path)[0] + '.csv'
        print(f"CSV file will be generated at {csv_file_path}")

        # Remove the CSV file if it exists
        if os.path.exists(csv_file_path):
            os.remove(csv_file_path)

        # Create a CSV file and write the header
        with open(csv_file_path, 'w', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=self._features)
            writer.writeheader()

            # Read the JSONL file and write the features to the CSV file
            with open(file_path, 'r') as file:
                for line in file:
                    json_data: dict = None
                    try:
                        json_data = json.loads(line)
                    except json.JSONDecodeError as e:
                        print(e.msg())
                        exit()

                    data = {}

                    for feature in self._features:
                        value = None

                        if feature == "sections_mean_entropy":
                            value = self._get_sections_mean_entropy(json_data)
                        elif feature == "sections_min_entropy":
                            value = self._get_sections_min_entropy(json_data)
                        elif feature == "sections_max_entropy":
                            value = self._get_sections_max_entropy(json_data)
                        elif feature == "sections_mean_rawsize":
                            value = self._get_sections_mean_raw_size(json_data)
                        elif feature == "sections_min_rawsize":
                            value = self._get_sections_min_raw_size(json_data)
                        elif feature == "sections_max_rawsize":
                            value = self._get_sections_max_raw_size(json_data)
                        elif feature == "sections_mean_virtualsize":
                            value = self._get_sections_mean_virtual_size(json_data)
                        elif feature == "sections_min_virtualsize":
                            value = self._get_sections_min_virtual_size(json_data)
                        elif feature == "sections_max_virtualsize":
                            value = self._get_sections_max_virtual_size(json_data)
                        else:
                            value = self._search_and_get(json_data, feature)

                        if value is None:
                            print(f"Feature {feature} not found in the JSON object")
                            exit()

                        if isinstance(value, dict) or isinstance(value, list):
                            print(f"Feature {feature} is a complex object")
                            exit()

                        data[feature] = value

                    writer.writerow(data)

    def check_file_path(self, file_path) -> bool:
        """
        Check if the file exists at the given path.

        Args:
        file_path (str): Path to the file.

        Returns:
        bool: True if the file exists, False otherwise.
        """
        if os.path.exists(file_path):
            return True
        else:
            return False
        
    def _search_and_get(self, json_data: dict, feature: str) -> Any:
        """
        Search recursively for the feature in the JSON object and return its value if found.

        Args:
        json_data (dict): JSON object.
        feature (str): Feature to be searched.
        default: Default value to be returned if the feature is not found.

        Returns:
        Any: Value of the feature if found, None otherwise.
        """
        for key, value in json_data.items():
            if key == feature:
                return value
            elif isinstance(value, dict):
                temp_value = self._search_and_get(value, feature)
                if temp_value is not None:
                    return temp_value
            elif isinstance(value, list):
                for item in value:
                    if isinstance(item, dict):
                        temp_value = self._search_and_get(item, feature)
                        if temp_value is not None:
                            return temp_value
        return None
    
    def _get_sections_mean_entropy(self, json_data: dict) -> float:
        """
        Calculate the mean entropy of the sections.

        Args:
        json_data (dict): JSON object.

        Returns:
        float: Mean entropy of the sections.
        """
        sections = self._search_and_get(json_data, "sections")

        if sections is None:
            print("Sections not found in the JSON object")
            exit()

        entropy_sum = 0
        feature = "entropy"

        for section in sections:
            value = self._search_and_get(section, feature)
            if value is not None:
                entropy_sum += value
            else:
                print(f"{feature} not found in the section")
                exit()

        return entropy_sum / len(sections)
    
    def _get_sections_min_entropy(self, json_data: dict) -> float:
        """
        Calculate the minimum entropy of the sections.

        Args:
        json_data (dict): JSON object.

        Returns:
        float: Minimum entropy of the sections.
        """
        sections = self._search_and_get(json_data, "sections")

        if sections is None:
            print("Sections not found in the JSON object")
            exit()

        entropy = float('inf')
        feature = "entropy"

        for section in sections:
            value = self._search_and_get(section, feature)
            if value is not None:
                entropy = min(entropy, value)
            else:
                print(f"{feature} not found in the section")
                exit()

        return entropy
    
    def _get_sections_max_entropy(self, json_data: dict) -> float:
        """
        Calculate the maximum entropy of the sections.

        Args:
        json_data (dict): JSON object.

        Returns:
        float: Maximum entropy of the sections.
        """
        sections = self._search_and_get(json_data, "sections")

        if sections is None:
            print("Sections not found in the JSON object")
            exit()

        entropy = float('-inf')
        feature = "entropy"

        for section in sections:
            value = self._search_and_get(section, feature)
            if value is not None:
                entropy = max(entropy, value)
            else:
                print(f"{feature} not found in the section")
                exit()

        return entropy
    
    def _get_sections_mean_raw_size(self, json_data: dict) -> float:
        """
        Calculate the mean raw size of the sections.

        Args:
        json_data (dict): JSON object.

        Returns:
        float: Mean raw size of the sections.
        """
        sections = self._search_and_get(json_data, "sections")

        if sections is None:
            print("Sections not found in the JSON object")
            exit()

        raw_size_sum = 0
        feature = "size"

        for section in sections:
            value = self._search_and_get(section, feature)
            if value is not None:
                raw_size_sum += value
            else:
                print(f"{feature} not found in the section")
                exit()

        return raw_size_sum / len(sections)
    
    def _get_sections_min_raw_size(self, json_data: dict) -> float:
        """
        Calculate the minimum raw size of the sections.

        Args:
        json_data (dict): JSON object.

        Returns:
        float: Minimum raw size of the sections.
        """
        sections = self._search_and_get(json_data, "sections")

        if sections is None:
            print("Sections not found in the JSON object")
            exit()

        raw_size = float('inf')
        feature = "size"

        for section in sections:
            value = self._search_and_get(section, feature)
            if value is not None:
                raw_size = min(raw_size, value)
            else:
                print(f"{feature} not found in the section")
                exit()

        return raw_size
    
    def _get_sections_max_raw_size(self, json_data: dict) -> float:
        """
        Calculate the maximum raw size of the sections.

        Args:
        json_data (dict): JSON object.

        Returns:
        float: Maximum raw size of the sections.
        """
        sections = self._search_and_get(json_data, "sections")

        if sections is None:
            print("Sections not found in the JSON object")
            exit()

        raw_size = float('-inf')
        feature = "size"

        for section in sections:
            value = self._search_and_get(section, feature)
            if value is not None:
                raw_size = max(raw_size, value)
            else:
                print(f"{feature} not found in the section")
                exit()

        return raw_size
    
    def _get_sections_mean_virtual_size(self, json_data: dict) -> float:
        """
        Calculate the mean virtual size of the sections.

        Args:
        json_data (dict): JSON object.

        Returns:
        float: Mean virtual size of the sections.
        """
        sections = self._search_and_get(json_data, "sections")

        if sections is None:
            print("Sections not found in the JSON object")
            exit()

        virtual_size_sum = 0
        feature = "vsize"

        for section in sections:
            value = self._search_and_get(section, feature)
            if value is not None:
                virtual_size_sum += value
            else:
                print(f"{feature} not found in the section")
                exit()

        return virtual_size_sum / len(sections)
    
    def _get_sections_min_virtual_size(self, json_data: dict) -> float:
        """
        Calculate the minimum virtual size of the sections.

        Args:
        json_data (dict): JSON object.

        Returns:
        float: Minimum virtual size of the sections.
        """
        sections = self._search_and_get(json_data, "sections")

        if sections is None:
            print("Sections not found in the JSON object")
            exit()

        virtual_size = float('inf')
        feature = "vsize"

        for section in sections:
            value = self._search_and_get(section, feature)
            if value is not None:
                virtual_size = min(virtual_size, value)
            else:
                print(f"{feature} not found in the section")
                exit()

        return virtual_size
    
    def _get_sections_max_virtual_size(self, json_data: dict) -> float:
        """
        Calculate the maximum virtual size of the sections.

        Args:
        json_data (dict): JSON object.

        Returns:
        float: Maximum virtual size of the sections.
        """
        sections = self._search_and_get(json_data, "sections")

        if sections is None:
            print("Sections not found in the JSON object")
            exit()

        virtual_size = float('-inf')
        feature = "vsize"

        for section in sections:
            value = self._search_and_get(section, feature)
            if value is not None:
                virtual_size = max(virtual_size, value)
            else:
                print(f"{feature} not found in the section")
                exit()

        return virtual_size

def main():
    features = [
        "md5", 
        "machine", 
        "sizeof_code", 
        "major_linker_version", 
        "minor_linker_version", 
        "sizeof_code", 
        "major_operating_system_version", 
        "minor_operating_system_version", 
        "major_image_version", 
        "minor_image_version", 
        "major_subsystem_version", 
        "minor_subsystem_version", 
        "sizeof_headers", 
        "subsystem", 
        "sizeof_heap_commit", 
        "sections_mean_entropy", 
        "sections_min_entropy", 
        "sections_max_entropy", 
        "sections_mean_rawsize", 
        "sections_min_rawsize", 
        "sections_max_rawsize", 
        "sections_mean_virtualsize", 
        "sections_min_virtualsize", 
        "sections_max_virtualsize"
    ]
    g = CSVGeneratorFromEmberJSONL(features)
    g.extract_and_generate("/path/to/data/ember2018/train_features_0.jsonl")

if __name__ == "__main__":
    main()
