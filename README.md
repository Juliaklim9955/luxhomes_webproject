# "Luxury Homes" - Real Estate Marketplace Web App


## Project Overview
This project is a **real estate marketplace web application** designed using **Django**, **Python**, **HTML**, **CSS**, **JavaScript**, and **PostgreSQL**. The application serves as an online platform where users can browse, inquire, and interact with real estate listings. Users can also log in using traditional authentication methods, as well as through **Facebook** and **Google** authentication.

The project implements a **full-stack solution** with a rich set of features, including user authentication, contact forms, real estate listing management, advanced search and pagination, and a fully customized Django admin panel for efficient backend management. It also integrates email functionality to notify users about their inquiries.


## Distinctiveness and Complexity
This project meets the **distinctiveness and complexity** requirements in the following ways:

- **Full-Stack Django Application**: The project integrates **Django** for the backend, which interacts with a **PostgreSQL** database to store and manage data. The **frontend** utilizes **HTML**, **CSS**, and **Bootstrap** for an interactive and responsive design, ensuring an excellent user experience on both desktop and mobile.
- **User Authentication**: The app supports **Django’s built-in authentication system** along with **third-party login options** through **Facebook** and **Google**. This functionality makes the application secure and easy for users to access.
- **Advanced Backend Features**: The project includes a **customized Django admin panel**, enabling administrators to manage listings, users, and inquiries efficiently. The admin panel also includes advanced features like **RichText Editors** and **Multi-Select Fields**.
- **Real Estate Listings**: The project allows users to browse listings, inquire about properties, and search for listings based on various filters such as property type, location, price, etc. The **pagination** and **search functionality** ensure that users can easily find the properties they are looking for.
- **Email Integration**: The app integrates **Django’s email functionality** to send confirmation emails and inquiry notifications, adding a professional touch to the application.
- **Complex State Management**: The use of Django’s **models** (User, Contact, Flat, and Team) allows for complex database interactions and data fetching for dynamic content rendering on the frontend.

This project demonstrates the full lifecycle of a real estate marketplace web app, from the backend with Django to the frontend with React. The app is built to handle real-world use cases, including user authentication, email notifications, and data fetching. The future goal is to extend the app to mobile devices using React Native.


## Files and Directories
- **settings.py**: Contains the Django settings, including configurations for the PostgreSQL database, static and media files, email setup, and security settings.
- **models.py**: Defines the database models such as `User`, `Contact`, `Flat`, and `Team`, which represent the key data structures of the application.
- **views.py**: Contains the view functions for handling requests, rendering templates, and processing form submissions.
- **urls.py**: Defines the URL routes for various views in the application.
- **templates/**: Contains HTML templates for the pages, including the homepage, property listing details, user contact forms, and the admin panel.
- **static/**: Contains CSS, JavaScript, and image files, including external libraries like **Bootstrap** and custom styles.
- **media/**: Stores media files such as images uploaded by users (for properties, user profiles, etc.).
- **accounts/**: Contains user authentication-related functionality (login, signup, password reset, etc.).
- **flats/**: Manages real estate listings and search functionality.
- **contacts/**: Manages user inquiries and feedback on listings.
- **pages/**: General pages of the website (e.g., homepage, about, contact).
- **requirements.txt**: Lists all Python dependencies required for the application, including Django, PostgreSQL adapter, and other necessary packages.
- **.env**: Stores sensitive environment variables like database credentials and email API keys to avoid exposing them in the codebase.

## How to Run the Application
To run the application locally, follow these steps:

### 1. Set up the Backend (Django)
- **Clone the repository**
- **Set Up a Virtual Environment**
- **Install Dependencies**
- **Set Up Environment Variables**
- **Apply Migrations**
- **Create a Superuser (Optional)**
- **Run the Development Server**

