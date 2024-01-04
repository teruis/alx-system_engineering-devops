# Docker Debugging Project

## Description
This repository contains the solution for the Docker debugging project. The goal is to get Apache running on a Docker container and have it return a page containing "Hello Holberton" when querying the root.

## Instructions

1. **Start the Docker Container:**
   ```bash
   docker run -p 8080:80 -d -it holbertonschool/265-0
   ```

2. **Check the Container Status:**
   ```bash
   docker ps
   ```

3. **Curl the Port and Check for Errors:**
   ```bash
   curl 0:8080
   ```

   If you encounter an error, follow the steps below to fix the issue.

4. **Access the Container:**
   ```bash
   docker exec -it CONTAINER_ID /bin/bash
   ```

5. **Navigate to Apache Configuration:**
   ```bash
   cd /etc/apache2/
   ```

6. **Edit Apache Configuration:**
   ```bash
   nano apache2.conf
   ```

   Update the `<Directory /var/www/>` section to allow the execution of PHP files and set `AllowOverride` to `All`.

7. **Create a Simple HTML Page:**
   ```bash
   echo "Hello Holberton" > /var/www/html/index.html
   ```

8. **Restart Apache:**
   ```bash
   service apache2 restart
   ```

9. **Exit the Container:**
   ```bash
   exit
   ```

10. **Test with Curl:**
    ```bash
    curl 0:8080
    ```

    Ensure that the "Hello Holberton" message is displayed.

## Files
- `Dockerfile`: Docker configuration file for building the container.
- `README.md`: Documentation on how to set up and debug the Docker container.
- `index.html`: Simple HTML page with the "Hello Holberton" message.

## Credits
This project is part of the Holberton School curriculum.

