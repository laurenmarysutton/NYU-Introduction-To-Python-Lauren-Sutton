def make_tags():
    tag_response = input('Please enter the word you would like to italicize in HTML.\n')
    return '<i>{}</i>'.format(tag_response)

def main():
    print(make_tags())

if __name__ == "__main__":
    main()
