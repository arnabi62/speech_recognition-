
# coding: utf-8

# In[4]:


import speech_recognition as sr
r=sr.Recognizer()
with sr.Microphone() as source:
    print("say")
    audio=r.listen(source)
try:
    print(r.recognize_google(audio))
except:
    print("can't listen")

