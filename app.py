import streamlit as st
import random
choices={
    "rock":"rock.jpg",
    "paper":"paper.jpg",
    "scissor":"scissor.jpg"
}
users_choice=st.selectbox("choice your option",choices.keys())
com_choice=random.choice(list(choices.keys()))
if st.button("PLAY"):

    col1,col2,col3=st.columns([1,1,1])

    with col1:
        st.image(choices[users_choice])
    with col2:
        st.write("v/s")
    with col3:
       
        st.image(choices[com_choice])
if users_choice==com_choice:
    st.markdown("### its a tie!")
elif(users_choice=="Rock" and com_choice=="scissor")or\
    (users_choice=="paper" and com_choice=="Rock")or\
    (users_choice=="scissor" and com_choice=="paper"):
    st.markdown("you win")
else:
    st.markdown("you lose!")


