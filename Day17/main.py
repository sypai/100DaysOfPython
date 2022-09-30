# Instagram User Class
class User():
    # static variable
    id = 0

    def __init__(self, user_name, age=None, gender=None):
        self.user_id = User.id
        self.user_name = user_name
        self.age = age
        self.gender = gender
        self.followers = 0
        self.following = 0
        User.id += 1

    def follow(self, user):
        self.following += 1
        user.followers += 1

    def show(self):
        text = self.user_name
        if not self.age == None:
            if self.gender == 'M':
                text = text + " a " + str(self.age) + " years old boy"

            elif self.gender == 'F':
                text = text + " a " + str(self.age) + " years old girl"
            
            else:
                text = text + " who is " + str(self.age) + " years old"

        print(f"\n### \n{text} has {self.followers} followers and follows {self.following} other users.")

# Using User class
user_01 = User("Suyash", 25, 'M')
user_02 = User("Shriya", 19)
user_03 = User("Radha")

user_01.follow(user_02)
user_01.follow(user_03)
user_03.follow(user_02)

# Show Data
user_01.show()
user_02.show()
user_03.show()

