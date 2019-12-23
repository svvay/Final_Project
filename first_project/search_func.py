import file_operation


def search_func(word):
    all_contacts = file_operation.WriteRead.finding_contact(None)
    similar_search = []
    for num_of_row, list_rows in enumerate(all_contacts):
        for id in dict(list_rows).values():
            if id == word:
                similar_search.append(num_of_row)
                print()
                for m_keys, m_value in dict(all_contacts[num_of_row]).items():
                    print(f"{m_keys} - {m_value}")
    print(similar_search)
