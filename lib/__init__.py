import csv
import dataclasses
from typing import List, Type


bills_filepath = 'assets/bills.csv'
legislators_filepath = 'assets/legislators.csv'
vote_results_filepath = 'assets/vote_results.csv'
votes_filepath = 'assets/votes.csv'

def __read_and_convert__(filepath:str, cls:Type[dataclasses.dataclass]) ->List[dataclasses.dataclass]:
    """
    Reads and converts CSV records to a dataclass

    Parameters:
    - filepath: The CSV file path
    - cls: The dataclass Type to be used to create and insert the objects in the list

    Returns:
        A list with the records of the CSV file path converted to objects of the cls Type
    """
    is_data_class = dataclasses.is_dataclass(cls)
    if not is_data_class:
        raise TypeError('obj_type is not a dataclass')
    with open(filepath) as csv_file:
        items = []
        fields = list(cls.__dataclass_fields__.keys())
        reader = csv.DictReader(csv_file)
        for row in reader:
            data = {}
            for field in fields:
                if field in row.keys():
                    content = row[field]
                    if content is not None:
                        data[field] =  content
            obj = cls.__new__(cls)
            obj.__init__(**data)
            items.append(obj)
    return items
    