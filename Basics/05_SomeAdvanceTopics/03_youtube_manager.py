import json

file_name = 'test.txt'

def load_data():
    try:
        with open(file_name, 'r') as file:
            return json.load(file)                      # returns a big string
    except FileNotFoundError:
        return []

def save_data_helper(videos):
    with open(file_name, 'w') as file:
        json.dump(videos, file)

def list_all_videos(videos):
    for index, video in enumerate(videos, start=1):
        print(f"{index} - {video}")

def add_videos(videos):
    video_name = input("Enter the name of the video: ")
    videos_time = input("Enter the time of the video: ")
    videos.append({'name': video_name, 'time': videos_time})
    save_data_helper(videos)

def update_some_data(videos):
    pass

def delete_videos(vedios):
    pass



# Optional ( Creating a entry point )

def main():

    videos = load_data()

    while True:

        print("\nYoutube Manager.... | Options: ")

        print(videos)

        print("1. List all the videos.")
        print("2. Add videos.")
        print("3. Update some data.")
        print("4. Delete a vedio.")
        print("5. Exit.")

        choice = input("Enter your choice: ")

        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_videos(videos)
            case '3':
                update_some_data(videos)
            case'4':
                delete_videos(videos)
            case '5':
                break
            case _:
                print("Invalid Choice.")


# __ -> dundar

if __name__ == "__main__":                          # File name
    main()

