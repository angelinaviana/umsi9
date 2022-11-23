import requests
import json
import pprint


# HELPER FUNCTION. DO NOT ALTER
def read_json(filepath, encoding='utf-8'):
    """Reads a JSON document, decodes the file content, and returns a list or
    dictionary if provided with a valid filepath.

    Parameters:
        filepath (str): path to file
        encoding (str): name of encoding used to decode the file

    Returns:
        dict/list: dict or list representations of the decoded JSON document
    """

    with open(filepath, 'r', encoding=encoding) as file_obj:
        return json.load(file_obj)


# HELPER FUNCTION. DO NOT ALTER
def write_json(filepath, data, encoding='utf-8', ensure_ascii=False, indent=2):
    """Serializes object as JSON. Writes content to the provided filepath.

    Parameters:
        filepath (str): the path to the file
        data (dict)/(list): the data to be encoded as JSON and written to the file
        encoding (str): name of encoding used to encode the file
        ensure_ascii (str): if False non-ASCII characters are printed as is;
                            otherwise non-ASCII characters are escaped.
        indent (int): number of "pretty printed" indention spaces applied to
                      encoded JSON

    Returns:
        None
    """

    with open(filepath, 'w', encoding=encoding) as file_obj:
        json.dump(data, file_obj, ensure_ascii=ensure_ascii, indent=indent)

# HELPER FUNCTION. DO NOT ALTER
def get_character_info(person, characteristics):
    """
    Creates a dictionary representing a person by extracting
    the key-value pairs from the SWAPI representation of the person
    (i.e., the JSON object retrieved from the SWAPI API)

    Since there are multiple key-value pairs in the < person > dictionary
    retrieved from the SWAPI API, the function simplifies the < person >
    dictionary by only keeping the key-value pairs that have the key in
    < characteristics >.

    Parameters:
        person (dict): a dictionary containing information about a person
        characteristics (list): a list of strings representing a person's
        characteristics

    Returns:
        dict: a dictionary containing information about a person
    """

    return {key: person[key] for key in person.keys() if key in characteristics}


def get_swapi_resource(url, params=None):
    """Returns a response object decoded into a dictionary. If query string < params > are
    provided the response object body is returned in the form on an "envelope" with the data
    payload of one or more SWAPI entities to be found in ['results'] list; otherwise, response
    object body is returned as a single dictionary representation of the SWAPI entity.

    Parameters:
        url (str): a url that specifies the resource.
        params (dict): optional dictionary of querystring arguments.

    Returns:
        dict: dictionary representation of the decoded JSON.
    """
    pass


def request_resource_details(base_url, category=None, params=None):
    """
    If provided, appends the resource < category > to the < base_url > to restrict
    the type of resource to be returned from SWAPI. If < params > are provided
    further qualifies the request by passing a dictionary of one or more querystring
    name-value pairs together with the (modified) < base_url > to the function
    < get_swapi_resource > which requests the resource. The possible categories
    include 'planets', 'people', 'starships', 'species', 'films', and 'vehicles.'

    Parameters:
        base_url (str): The base URL to SWAPI
        category (str): The type of resource to fetch
        params (dict): Dictionary of querystring arguments. The default value is None

    Returns:
        dict: dictionary representation of the resource retrieved from SWAPI.
    """
    pass


def resolve_dict_url(resource, key_name):
    """
    Replaces the URL inside a dictionary with a dictionary representation of the data returned by
    the URL.

    Parameters:
        resource (dict): A dictionary that contains the URLs that have to be replaced with a
                         dictionary.
        key_name (str): The key that contains the URL that has to be resolved

    Returns:
        None
    """
    pass


def get_darth_vader_info(base_url):
    """
    Retrieves all information about the Sith Lord, Darth Vader. Returns a dictionary comprising
    three key-value pairs:

    1. 'leader' (dict): representation of Darth Vader
    2. 'ships' (dict): representation of Darth Vader's ships
    3. 'planet' (dict): representation of the planet Bespin

    Parameters:
        base_url (str): Resource URL used to retrieve the resource.

    Returns:
        dict: leader, ships, and planet key-value pairs
    """
    pass


def fetch_boarding_order(passenger):
    """
    Returns the value of the 'boarding_order' key in the 'passenger' dict passed to it as an argument.

    Parameters:
        passenger (dict): A dictionary representation of a passenger.

    Returns:
        int: An integer value corresponding to the 'boarding_order' key
        in the 'passenger' dictionary.
    """
    pass


def sort_boarding_order(boarding_order):
    """
    Accepts a list of dictionaries containing the name of each passenger and their boarding order.
    Sorts the passengers in ascending order according to their boarding order and returns the
    sorted list.

    Parameters:
        boarding_order (list): List of dictionaries containing the name and boarding order of each
                               passenger.

    Returns:
        list: List of dictionaries sorted according to the value of their
              'boarding_order' keys.
    """
    pass


def main():
    """Program entry point.

    Parameters:
        None

    Returns:
        None
    """
    pp = pprint.PrettyPrinter(indent=2, sort_dicts=False, width=100)
    # Use pp.pprint() to print dictionaries in a cleaner way.

    # Problem 1.2
    base_url = None
    films_url = None


    # Problem 02
    planets_name = None


    # Problem 03
    characteristics = ['name', 'height', 'mass', 'birth_year', 'homeworld', 'species']
    people_names = None


    # Problem 04
    # people_names.???

    # Problem 05
    starship_info = None
    starship_names = None

    # Problem 06
    residents_count = None

    # Problem 07
    all_vader_info = None

    # Problem 08
    boarding_order = None


if __name__ == "__main__":
    main()