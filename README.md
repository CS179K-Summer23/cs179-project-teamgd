[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=11509565&assignment_repo_type=AssignmentRepo)
# GoodDatabaseDB
  GoodDatabaseDB is a terminal based terminal for storing and access Json documents. Features include sorting, query, and file revision history.

## 👥 Team Members
- Joseph Hu (JosephHu113)
- Nathan Tran (NateTran)
- Cote Feldsine (cfeldsine)
- Benson Won (iarebwan)
- Jonas Tan (jones171)

## 🛠️ Technologies
- Python
- SQL
- String Manipulation
- Json Library
- Pandas Library

## 💡 Features 
- **Our features:**
  - Interface to access database: Users interact with our database using the terminal. All valid documents are automatically displayed as a table so users can better visualize the data.
  - Authentication/User Profiles: Users can login to the database using username and password. Each user has exclusive access to their own database.
  - Table representation of documents: The tables are created by taking all of the data from the documents and locally storing the information into dictionaries. This enables fast retrieval and editing of information. 
  - Ability to query documents: Users have the option to query the entire JSON like ctrl-f or query the table using keys.
  - Ability to find and/or replace strings - will show documents/line number of string location(s): Users can edit specific keys/values that are queried.
  - Uploading/importing documents: Users can upload documents to the database from their computer and download documents from the database to their computer. 
  - Conversion of non-json documents to json format and vice versa: CSV files that are uploaded by the user are automatically read as a JSON and adhere to the JSON schema. 
  - Editing the document(s) in the database: Users have the option of directly editing the JSON or editing rows of the table.
  - Ability to pin certain documents to make them more accessible based on user’s priorities: Users have the option of pinning a document to the top of the document list. This document stays pinned until the user decides to unpin it.
  - Get statistics about document (number characters, words): Users can view the metadata of their documents.
    
## User Stories
  - As a developer, I want users to have an interface to access the database
  - As a developer, I want to enable users to edit, upload, and delete their documents
  - As a developer, I want users to query documents in the database
  - As a developer, I want to enable users to convert imports and export files to and from Json
  - As a developer, I want older versions of stored documents to be available for users to access
  - As a developer, I want to enforce customers logging in with a username and password to view their documents
