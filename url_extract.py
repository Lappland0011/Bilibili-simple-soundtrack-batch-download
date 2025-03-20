def extract_and_format_urls_from_file(file_path):
    # Read the file content
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Split the content by space and filter out elements starting with 'href'
    href_elements = [element for element in content.split() if element.startswith('href')]
    
    # Extract URLs from the first pair of quotes within href elements
    urls = []
    for element in href_elements:
        start_quote_index = element.find('"') + 1  # Find the index of the first quote and move past it
        end_quote_index = element.find('"', start_quote_index)  # Find the next quote starting after the first
        url = element[start_quote_index:end_quote_index]
        urls.append(url)
    
    # Remove duplicates by converting to a set and back to a list
    urls = list(set(urls))
    
    # Sort the list to ensure duplicates are adjacent (if any remain)
    urls.sort()
    
    # Remove exact consecutive duplicates
    unique_urls = [urls[i] for i in range(len(urls)) if i == 0 or urls[i] != urls[i-1]]
    
    # Format and print the URLs
    for url in unique_urls:
        print(f'"{url}",')

if __name__ == "__main__":
    file_path_doc_list =['C:\Users\maxzh\AppData\Local\Programs\animenz\animenzzz_full_url_pg1.txt']
                        '''['C:\\Users\\maxzh\\AppData\\Local\\Programs\\animenz\animenzzz_full_url_pg1.txt',
                          'C:\\Users\\maxzh\\AppData\\Local\\Programs\\animenz\animenzzz_full_url_pg2.txt',
                          'C:\\Users\\maxzh\\AppData\\Local\\Programs\\animenz\animenzzz_full_url_pg3.txt',
                          'C:\\Users\\maxzh\\AppData\\Local\\Programs\\animenz\animenzzz_full_url_pg4.txt',
                          'C:\\Users\\maxzh\\AppData\\Local\\Programs\\animenz\animenzzz_full_url_pg5.txt',
                          'C:\\Users\\maxzh\\AppData\\Local\\Programs\\animenz\animenzzz_full_url_pg6.txt',
                          'C:\\Users\\maxzh\\AppData\\Local\\Programs\\animenz\animenzzz_full_url_pg7.txt']'''
    for i in file_path_doc_list:
        extract_and_format_urls_from_file(i)
