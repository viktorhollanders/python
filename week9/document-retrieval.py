from string import punctuation

# Constants
VALID_OPTIONS = ["search", "print", "quit"]
SEARCH = "search"
PRINT = "print"
QUIT = "quit"
NO_MATCH = "No match"


def main():
    file_input = input()

    document_list = list_of_documents(open_file(file_input))

    search_dict = create_search_dict(document_list)

    while (user_input := input().lower()) in VALID_OPTIONS:
        if user_input == SEARCH:
            # call the search function
            search_input = input().lower()
            search_document(search_input, search_dict)
        if user_input == PRINT:
            # call the print function
            print_input = input()
            print_document(print_input, document_list)
        if user_input == QUIT:
            return


def open_file(file_name):
    """
    Open a document if a valid file name is entered
    """
    try:
        with open(file_name) as file:
            content = file.readlines()

        return [item.replace("\n", " ") for item in content]
    except FileNotFoundError:
        return []


def list_of_documents(a_list: list[str]):
    """
    This function takes a list of documents and splits them in to a list of the n number of document. Each document in the list is one long string.
    """
    DELIMITER = "<END OF DOCUMENT>"

    documents = []
    current_document = ""

    for item in a_list:
        if DELIMITER in item:
            documents.append(current_document.strip(" "))
            current_document = ""
        else:
            current_document += item
    if current_document:
        documents.append(current_document)

    return documents


def process_text(text):
    words = [word.lower().strip(punctuation) for word in text.split()]
    return " ".join(words)


def create_search_dict(a_list: list[str]) -> dict:
    """
    This function function takes the list of documents and returns a dictonaary with how many documents the words apear in.
    """

    search_dict = {}

    for index, item in enumerate(a_list):
        processed_words = process_text(item)

        for word in processed_words.split():
            if word not in search_dict:
                search_dict[word] = {index + 1}
            elif word not in search_dict[word]:
                search_dict[word].add(index + 1)
    return search_dict


def search_document(search_quaery: str, search_dict: dict) -> None:
    """
    Takes in a searc quary string of 1 - 3 words. If the search quary is in the search_dict it prints the documents containing the givven words.
    """
    search_query_words = [word.strip() for word in search_quaery.split()]

    if all(word in search_dict for word in search_query_words):
        list_of_sets = [search_dict[item] for item in search_query_words]

        # Initialize set_value with the first set
        set_value = list_of_sets[0].copy()

        # Find the intersection of sets
        for item in list_of_sets[1:]:
            set_value.intersection_update(item)

        if set_value:
            print("Documents matching search:", end=" ")
            for item in set_value:
                print(item, end=" ")
            print()
        else:
            print(NO_MATCH)
    else:
        print(NO_MATCH)


def print_document(search_query: str, document_list):
    # if search - 1 is in document list
    # print the document number
    # print the document content

    try:
        query = int(search_query)
        index = query - 1
        if document_list[index]:
            print(f"Document #{index + 1}:")
            print(f"{document_list[index]}")
        else:
            print(NO_MATCH)
    except IndexError:
        print(NO_MATCH)
    except ValueError:
        print(NO_MATCH)


if __name__ == "__main__":
    main()
