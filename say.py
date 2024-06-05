from gtts import gTTS
import pygame
import tempfile

def say(text):

    language = 'en'
    
    myobj = gTTS(text=text, lang=language, slow=False)
       
    # Create a temporary file
    with tempfile.NamedTemporaryFile(suffix='.mp3', delete_on_close=False, delete=True) as temp_file:
        
        temp_file_name = temp_file.name
        print(temp_file_name)
        
        myobj.save(temp_file_name)
        temp_file.close()

        pygame.mixer.init()
        pygame.mixer.music.load(temp_file_name)
        pygame.mixer.music.play()
                
        # wait for player to finish
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)  # Adjust the value to control the loop speed
        
        # unload the temp file so it can be deleted
        pygame.mixer.music.unload()


    

    # if os.path.exists(temp_file_name):
    #     os.remove(temp_file_name)

