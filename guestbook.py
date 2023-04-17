import argparse

FILE_NAME = 'guestbook.txt'


def add_entry(note):
    with open(FILE_NAME, 'a') as f:
        f.write(note + '\n')
        print('New entry added successfully!')


def list_entries():
    with open(FILE_NAME, 'r') as f:
        entries = f.readlines()
        if not entries:
            print('Guestbook is empty!')
        else:
            print('Guestbook entries:')
            for i, entry in enumerate(entries, start=1):
                print(f'{i}. {entry}')


def edit_entry(index, note):
    with open(FILE_NAME, 'r') as f:
        entries = f.readlines()
        if index <= 0 or index > len(entries):
            print('Invalid index!')
        else:
            entries[-index] = note + '\n'
            with open(FILE_NAME, 'w') as f:
                f.writelines(entries)
                print('Entry edited successfully!')


def delete_entry(index):
    with open(FILE_NAME, 'r') as f:
        entries = f.readlines()
        if index <= 0 or index > len(entries):
            print('Invalid index!')
        else:
            entries.pop(-index)
            with open(FILE_NAME, 'w') as f:
                f.writelines(entries)
                print('Entry deleted successfully!')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Guestbook CLI application')
    subparsers = parser.add_subparsers(dest='command')

    # New entry sub-command
    new_parser = subparsers.add_parser('new', help='Add a new entry to the guestbook')
    new_parser.add_argument('note', type=str, help='Note to add to the guestbook')

    # List entries sub-command
    subparsers.add_parser('list', help='List all entries in the guestbook')

    # Edit entry sub-command
    edit_parser = subparsers.add_parser('edit', help='Edit an existing entry in the guestbook')
    edit_parser.add_argument('index', type=int, help='Index of the entry to edit')
    edit_parser.add_argument('note', type=str, help='New note content')

    # Delete entry sub-command
    delete_parser = subparsers.add_parser('delete', help='Delete an existing entry from the guestbook')
    delete_parser.add_argument('index', type=int, help='Index of the entry to delete')

    args = parser.parse_args()

    if args.command == 'new':
        add_entry(args.note)
    elif args.command == 'list':
        list_entries()
    elif args.command == 'edit':
        edit_entry(args.index, args.note)
    elif args.command == 'delete':
        delete_entry(args.index)
    else:
        parser.print_help()
