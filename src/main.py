from textnode import TextNode


def main():
    test_node = TextNode(
        text="Some sample text", text_type="link", url="https://www.boot.dev"
    )
    print(test_node)


main()
