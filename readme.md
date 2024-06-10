# My Blog Project

Welcome to the My Blog Project! This is a simple blog platform built using Python, allowing users to create blog posts, comment on them, and share posts via email.

## Features

- **Create Blog Posts**: Users can write and publish blog posts.
- **Comment on Posts**: Readers can leave comments on blog posts.
- **Share Posts via Email**: Readers can share interesting blog posts with others via email.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Installation

To get a local copy up and running, follow these steps:

### Prerequisites

Make sure you have Python 3.x installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### Installation Steps

1. **Clone the Repository**

    ```sh
    git clone https://github.com/Mayejacob/blog.git
    cd your-blog-project
    ```

2. **Create a Virtual Environment**

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install Dependencies**

    ```sh
    pip install -r requirements.txt
    ```

4. **Set Up the Database**

    ```sh
    python manage.py migrate
    ```

5. **Create a Superuser**

    ```sh
    python manage.py createsuperuser
    ```

6. **Run the Development Server**

    ```sh
    python manage.py runserver
    ```

7. **Access the Application**

    Open your web browser and go to `http://127.0.0.1:8000/`.

## Usage

### Creating a Blog Post

1. Log in to the admin panel at `http://127.0.0.1:8000/admin/`.
2. Navigate to the Blog section and add a new post.
3. Fill in the title, content, and any other fields, then save the post.

### Commenting on a Post

1. Visit a blog post detail page.
2. Fill in the comment form at the bottom of the post.
3. Submit the comment.

### Sharing a Post via Email

1. Open a blog post.
2. Click the "Share via Email" button.
3. Enter the recipient's email address and send the email.



