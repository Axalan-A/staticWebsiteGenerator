from re import findall

def extract_markdown_images(text: str) -> list:
    image_properties = findall(r"!\[(.*?)\]\((.*?)\)", text)
    return(image_properties)

def extract_markdown_links(text: str) -> list:
    link_properties = findall(r"(?<!!)\[(.*?)\]\((.*?)\)", text)
    return(link_properties)
