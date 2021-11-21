import json


if __name__ == '__main__':
    file_path = input("Drag and drop the Preferences file here and press Enter: ")

    # Hacky fix to remove surrounding quotes in path
    if file_path[0] == '"' and file_path[-1] == '"':
        file_path = file_path[1:-1]

    with open(file_path, 'r+') as f:
        # First, backup our file
        with open(file_path + '_backup', 'w') as f_backup:
            f_backup.writelines(f.readlines())

        f.seek(0)
        data = json.load(f)

        data['brave']['hide_brave_rewards_button'] = True
        data['brave']['wallet']['show_wallet_icon_on_toolbar'] = False
        data['brave']['ads']['enabled'] = False

        f.seek(0)
        f.truncate(0)

        json.dump(data, f, separators=(',', ':'))
