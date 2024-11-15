# Tutee Agent System Setup Guide

This guide provides step-by-step instructions to set up and run the Tutee Agent System using MongoDB and Node.js.

## Prerequisites

- MongoDB installed
- Node.js installed

## Steps

### 1. Start MongoDB Database

1. Open your terminal.
2. Navigate to your MongoDB installation directory:
   ```bash
   cd /Users/seki/Downloads/mongodb
Go to the bin directory:
bash
コードをコピーする
cd bin
Start the MongoDB server with the following command:
bash
コードをコピーする
./mongod --dbpath ../data/db
Note: If you encounter any issues with the database path, try deleting all files inside the data/db directory and restarting.
2. Start the Tutee Agent System
Open a new terminal window.
Navigate to the Tutee Agent System directory:
bash
コードをコピーする
cd /Users/seki/Desktop/tuteeagentsystem
Start the application in development mode:
bash
コードをコピーする
npm run devstart
If needed, you may also need to make the set_google_app_creds.sh script executable by running:
bash
コードをコピーする
chmod a+x ./set_google_app_creds.sh
3. Access the System
Open a web browser and go to:
http://localhost:3000 to access the main interface.
http://localhost:3000/admin/reset_superadmin to reset the superadmin account.
4. Login
Username: inolab
Password: collablab
コードをコピーする
