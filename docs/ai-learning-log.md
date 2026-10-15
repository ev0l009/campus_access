# UI Menu workflow

My proposed workflow

```
Campus Access Menu Workflow

Auth_selection menu:
    - Login
    - Register
    - Exit

    User selection menu:
        - Admin
        - Staff
        - Student
        - Visitor
        - Go back or exit

        Auth menu:
            - Register and on sucess move to login menu
            - Login

            User specific menu:
                - *** User specific actions
                -Exit
```

I asked how to implement and it suggested;
- While Loops with Conditional Statements (if/elif/else)
- Functions / State Machine Pattern

I opted for the second. It was uncharted territory and it's cleaner.

# Bug Log: Multi-User Registration & Login Failure

    Issue:
    Registering a new user succeeded initially, but logging in with subsequent registered users failed or lost user attributes (such as names and correct ID keys).

    Root Causes:

        Persistence Gap: Newly created users were added to the in-memory data dictionary during create_user(), but changes were not saved back to data.json via save_session().

        Data Omission: The name input collected during registration was not passed into generate_user_data(), leaving "name": "" empty in the stored JSON.

        Data Key Mismatch: generate_user_data() assigned "stf_id" to student objects instead of "std_id".

        Unsafe DB Initialization: load_data() lacked a fallback default schema ({"users": {...}}) if data.json was empty or missing.

    Fixes Applied:

        Added save_session(data) call directly inside create_user() immediately following user assignment.

        Updated generate_user_data() signature and dict mappings to include name and corrected "std_id" for students.

        Enhanced load_data() to auto-generate and save the standard nested dictionary schema if data.json is missing or empty.