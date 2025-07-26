
# from fastapi import Body, FastAPI, Query
# import json
 
# app = FastAPI()
 
# def load_json_db():
#     #open file and return data
#     with open("database.json", 'r') as f:
#         return json.load(f)
   
 
# def save_json_db(user_details):
#     with open('database.json', 'w') as f:
#         json.dump(user_details, f)
 
# @app.post('/save')
# def users(details: dict = Body(...)):
#     all_users = load_json_db()
#     all_users.update({ details.get('username') : details.get('password')})
#     save_json_db(all_users)
#     # print(all_users)
#     all_users = load_json_db()
#     return all_users

# @app.post('/user/add')
# def add_user(details: dict = Body(...)):
#     username = details.get("username")
#     password = details.get("password")

#     if not username or not password:
#         raise HTTPException(status_code=400, detail="Username and password required.")

#     users = load_json_db()
#     if username in users:
#         raise HTTPException(status_code=400, detail="Username already exists.")

#     users[username] = password
#     save_json_db(users)
#     return {"message": f"User '{username}' added successfully."}

# @app.put("/password/update")
# def update_password(username: str = Query(...), new_password: str = Body(...)):
#     users = load_json_db()

#     if username not in users:
#         raise HTTPException(status_code=404, detail="User not found.")

#     users[username] = new_password
#     save_json_db(users) 
#     return {"message": f"Password updated for user '{username}'."}

# @app.delete("/user/delete")
# def delete_user(username: str = Query(...)):
#     users = load_json_db()

#     if username not in users:
#         raise HTTPException(status_code=404, detail="User not found.")

#     del users[username]
#     save_json_db(users)
#     return {"message": f"User '{username}' deleted successfully."}

# @app.get("/user/all")
# def get_all_users():
#     return load_json_db()

# @app.get("/user")
# def get_user(username: str = Query(...)):
#     users = load_json_db()

#     if username not in users:
#         raise HTTPException(status_code=404, detail="User not found.")

#     return {username: users[username]}
