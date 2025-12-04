class SocialMediaProfile:
    def __init__(self, username):
        self.username = username
        self.posts = []

    def add_post(self, content):
        self.posts.append(content)
        print(f"{self.username} added a new post: {content}")

    def display_timeline(self):
        print(f"{self.username}:")
        for a in self.posts:
            print(a)

if __name__ == "__main__":
    derek = SocialMediaProfile("Derek")

    derek.add_post("Hello, world!")
    derek.add_post("Had a great day at the park!")
    derek.add_post("What's up, Natalie? How are you?")

    derek.display_timeline()
