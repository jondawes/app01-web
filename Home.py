import streamlit as st
from modules import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"]
    print(todo)
    todos.append(todo + "\n")
    functions.write_todos(todos)
    st.session_state["new_todo"]=""

st.title("My Todo App")
st.subheader("This is my todo app")
st.text("This app is to increase your productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=index)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[index]
        #st.experimental_rerun()
        st.rerun()

st.text_input(label="Enter a todo", label_visibility="hidden", 
              placeholder="Enter a todo",
              on_change=add_todo,
              key="new_todo")

# Super cool Dev tool!! Remove before publishing
#st.session_state