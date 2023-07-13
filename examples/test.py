from AnimazePy import AnimazeWrapper

animaze.connect()

# Get Avatars
response = animaze.get_avatars()
print(response)


#Load an Avatar
response = animaze.load_avatar("avatar03")
print(response)

# Get Scenes
response = animaze.get_scenes()
print(response)

# Load a Scene
response = animaze.load_scene("@Kentax_Red")
print(response)




if __name__ == "__main__":
  animaze = AnimazeWrapper()

