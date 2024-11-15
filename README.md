# Tutee Agent System Setup Guide

This guide provides step-by-step instructions to set up and run the Tutee Agent System using MongoDB and Node.js.

## Prerequisites

- **MongoDB** installed
- **Node.js** installed

## Steps

### 1. Start MongoDB Database

1. Open your terminal.
2. Navigate to your MongoDB installation directory:
   - ```bash
     cd /Users/seki/Downloads/mongodb
     ```
3. Go to the `bin` directory:
   - ```bash
     cd bin
     ```
4. Start the MongoDB server with the following command:
   - ```bash
     ./mongod --dbpath ../data/db

5.開けない場合：mongodb―data―db(inside delete All file)


### 2. Start the Tutee Agent System
1.open your new terminal
2.Navigate to the Tutee Agent System directory:
 - ```bash
     cd /Users/seki/Desktop/tuteeagentsystem
     ```
3.Start the application in development mode:
 - ```bash
     npm run devstart
     ```
4.Optional: If needed, make the set_google_app_creds.sh script executable by running
 - ```bash
     chmod a+x ./set_google_app_creds.sh
     ```

### 3. Access the Tutee Agent System
 Open a web browser and go to:
   - [http://localhost:3000](http://localhost:3000) to access the main interface.
   - [http://localhost:3000/admin/reset_superadmin](http://localhost:3000/admin/reset_superadmin) to reset the superadmin account.

### 4. Login

- **Username**: `inolab`
- **Password**: `collablab`





