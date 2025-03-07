from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
import secrets

# Instead of using the database to store the tokens, we are using a dictionary to store the tokens
tokens = {}

class LoginView(APIView):

    def post(self, request):
        username = request.data.get("username")  # Get the username from the request
        password = request.data.get("password")  # Get the password from the request

        if not username: # Check if the username is not provided
            return Response({"error": "Username is required"}, status=400)
        if not password: # Check if the password is not provided
            return Response({"error": "Password is required"}, status=400)

        # Check if the username and password are correct
        if username == "admin" and password == "password123":
            
            if username not in tokens:
                tokens[username] = secrets.token_hex(32)

            return Response({"token": tokens[username]}, status=200)

        return Response({"error": "Invalid credentials"}, status=401)



class TodoListView(APIView):

    def get(self, request):

        auth_token = request.headers.get("Authorization") # Get the Authorization token from the request headers
        
        if auth_token not in tokens.values():
            return Response({"error": "Unauthorized"}, status=401)
        # List of todos stactic data
        todos = [
            {"id": 1, "task": "TODO", "status": "pending"},
            {"id": 2, "task": "Shortlisted", "status": "in progress"},
            {"id": 3, "task": "Hired", "status": "completed"},
            {"id": 4, "task": "Waiting List", "status": "pending"},
            {"id": 5, "task": "Rejected", "status": "in progress"},
            {"id": 6, "task": "In Review", "status": "completed"},
        ]

        return Response(todos, status=200)


