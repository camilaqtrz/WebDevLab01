import streamlit as st

if "owala" not in st.session_state:
    st.session_state.owala = 0
if "stanley" not in st.session_state:
    st.session_state.stanley = 0
if "nalgene" not in st.session_state:
    st.session_state.nalgene = 0
if "yeti" not in st.session_state:
    st.session_state.yeti = 0
    
#Header

def headerSection():
    st.header("Which Water Bottle Are You?")
    waterbottle_image = "../Images/waterbottles.jpg"
    st.image(waterbottle_image, width = 400)
    about_quiz = "Answer the questions to find out which water bottle you are. Have fun!"
    st.write(about_quiz)

#headerSection()

#First Question

def firstQuest():
    outdoor_image = "../Images/nature.jpg"
    st.image(outdoor_image, width = 300)
    question = "Are you outdoors often?"
    choices = ["Yes, everyday!", "Often but not everyday", "Not really", "No"]
    selectedChoices = st.radio(question, choices, key = "questOne") #NEW
    if selectedChoices == choices[0]:
        st.session_state.nalgene += 1
    elif selectedChoices == choices[1]:
        st.session_state.yeti += 1
    elif selectedChoices == choices[2]:
        st.session_state.stanley += 1
    elif selectedChoices == choices[3]:
        st.session_state.owala += 1
        
#firstQuest()

# Second Question

def secondQuest():
    water_image = "../Images/water.jpg"
    st.image(water_image, width = 300)
    st.write("About how much water do you drink in a day?")
    number = st.number_input(
        "Enter an estimate! (Remember, 20 oz is as much as a regular Coke Bottle!):",
        min_value = 0, max_value = 200, key = "questTwo"
        ) #NEW
    if number > 100:
        st.session_state.nalgene += 2
        st.session_state.yeti += 2
    elif number > 32:
        st.session_state.owala += 2
    else:
        st.session_state.stanley += 2     

#secondQuest()

# Third Question

def thirdQuest():
    color_image = "../Images/colors.jpg"
    st.image(color_image, width = 300)
    st.write("What color brightness do you like more?")
    options = ["Light", "Dark", "Neutral", "Muted"]
    selectedOption = st.selectbox("Choose your favorite! :)", options, key = "questThree")#NEW
    if selectedOption == "Light":
        st.session_state.owala += 1
    elif selectedOption == "Dark":
        st.session_state.nalgene += 1
    elif selectedOption == "Neutral":
        st.session_state.yeti += 1
    elif selectedOption == "Muted":
        st.session_state.stanley += 1
    
    
#thirdQuest()

#Fourth Question

def fourthQuest():
    scale_image = "../Images/scale.jpg"
    st.image(scale_image, width = 300)
    rate = st.slider("Rate water on a scale from 1 to 10!", 0, 10, 0, key = "questFour")#NEW
    if rate > 8:
        st.session_state.nalgene += 1
    elif rate > 5:
        st.session_state.yeti += 1
    else:
        st.session_state.stanley += 1
        st.session_state.owala += 1
#fourthQuest()
    
#Fifth Question

def fifthQuest():
    sea_image = "../Images/seacreatures.jpg"
    st.image(sea_image, width = 400)
    seaQuestion = "Lastly, choose a sea creature!"
    creature = ["Blue Whale", "Seahorse", "Sea Turtle", "Octopus"]
    selectedChoices = st.radio(seaQuestion, creature, key = "questFive")
    if selectedChoices:
        if selectedChoices == "Blue Whale":
            st.session_state.yeti += 2
        elif selectedChoices == "Seahorse":
            st.session_state.stanley += 2
        elif selectedChoices == "Sea Turtle":
            st.session_state.owala += 2
        elif selectedChoices == "Octopus":
            st.session_state.nalgene += 2
        
#fifthQuest()

#Water Bottle

def waterbottle():
    headerSection()

    firstQuest()
    secondQuest()
    thirdQuest()
    fourthQuest()
    fifthQuest()

    if st.button("Find out which water bottle you are!"):
        if st.session_state.nalgene > st.session_state.owala and st.session_state.nalgene > st.session_state.stanley and st.session_state.nalgene > st.session_state.yeti:
            st.subheader("You are a Nalgene waterbottle!")
            nalgene_image = "../Images/nalgene.jpg"
            st.image(nalgene_image, width = 400)
            st.write("Always ready for an adventure and your dreams are limitless!")
        elif st.session_state.owala > st.session_state.nalgene and st.session_state.owala > st.session_state.stanley and st.session_state.owala > st.session_state.yeti:
            st.subheader("You are an Owala waterbottle!")
            owala_image = "../Images/owala.jpg"
            st.image(owala_image, width = 400)
            st.write("Reliable and ready to be productive!")
        elif st.session_state.yeti > st.session_state.nalgene and st.session_state.yeti > st.session_state.stanley and st.session_state.yeti > st.session_state.owala:
            st.subheader("You are an Yeti waterbottle!")
            yeti_image = "../Images/yeti.webp"
            st.image(yeti_image, width = 400)
            st.write("Tough and rough on the outside and always ready for anything!")
        elif st.session_state.stanley > st.session_state.nalgene and st.session_state.stanley > st.session_state.yeti and st.session_state.stanley > st.session_state.owala:
            st.subheader("You are an Stanley waterbottle!")
            stanley_image = "../Images/stanley.jpeg"
            st.image(stanley_image, width = 400)
            st.write("Visionary and not afraid to try anything!")
        else:
            st.subheader("You are a hydroflask!")
            hydro_image = "../Images/hydroflask.jpg"
            st.image(hydro_image, width = 400)
            st.write("Nostalgia hits you with a wave of emotions, leaving you longing for the past...")
        st.balloons()
if __name__ == "__main__":
    waterbottle()
    
    
