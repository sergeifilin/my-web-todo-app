import streamlit as st
import modules.functions as functions


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.save_todos(todos)


st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app will increase your productivity.")

todos = functions.get_todos()

for i, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(i)
        functions.save_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="Enter new todo",
              label_visibility="hidden",
              placeholder="Add new todo...",
              on_change=add_todo,
              key="new_todo")

print("Hello mom")

st.session_state
