# What is Docker & Docker Container?
<br>

`ডকার হল একধরনের লিনাক্স **কন্টেইনার** টেকনোলজি । এর কাজ হল ডেভেলপমেন্ট এর জন্য আপনার অ্যাপ্লিকেশান লেয়ার কে সিস্টেম লেয়ার থেকে আলাদা করা । এটা একটা Cross Platform টুল যেটা উইন্ডোজ , লিনাক্স , ম্যাক , পাওয়ার পিসি সহ অনেক অনেক অপারেটিং সিস্টেম এ চলে ।`

<br>

- Container কিভাবে কাজ করে?
কার্গো জাহাজে যেভাবে কন্টেইনার সাজানো হয়, যেখানে একটির সাথে আরেকটির কোনো সম্পর্ক থাকে না। ঠিক একই ভাবে কন্টেইনার ইঞ্জিনের (Like Docker) উপরে বিভিন্ন কন্টেইনার ভিত্তিক অ্যাপ্লিকেশন রান করানো হয়। একটি কন্টেইনার প্ল্যাটফর্মের (Like Docker) উপরে অনেকগুলা কন্টেইনার তৈরি করা যায় এবং এক একটি কন্টেইনার আলাদা সার্ভিস/অ্যাপ্লিকেশন হিসেবে ব্যবহার করা যায়। কন্টেইনার টেকনোলজি প্রসেস লেভ'isolation' করে ফলে, এক কন্টেইনারের প্রেসেসের সাথে আরেক কন্টেইনারের প্রেসেস অথবা কন্টেইনার প্রসেসের সাথে হোস্ট (Host) সিস্টেমের প্রসেসের মধ্যে কোনো সম্পর্ক থাকে না।  প্রতিটি কন্টেইনার সরাসরি অপারেটিং সিস্টেম (OS) হতে প্রয়োজনীয় রিসোর্স (Kernel, Memory, Storage, Network, etc.) ব্যবহার করে।এক একটি কন্টেইনার ইমেজ মূলত নির্দিষ্ট অ্যাপ্লিকেশন/সার্ভিসের (Like Apache, mySQL, nginx) জন্য ব্যবহার করা হয় এবং এক একটি কন্টেইনার একটি পূর্ণাঙ্গ (Complete) প্যাকেজ, যার মধ্যে শুধুমাত্র নির্দিষ্ট অ্যাপ্লিকেশনের জন্য প্রয়োজনীয় কোড, বাইনারী (Binaries), সিস্টেম লাইব্রেরী (Libraries) থাকে। ফলে, এটার সাইজ খুবই ছোট (MBs) হয় এবং ভার্চুয়াল মেশিন (VM) থেকে অনেক দ্রুত রান করে এবং কাজ করে। 
<br>

# devops এর সাথে docker: 
- DevOps হল একটি software development methodology যা software development থেকে “Dev” শব্দ এবং IT operations থেকে “Ops” শব্দ দুটির মিশ্রিত একটি নাম। যার অর্থ দাঁড়ায় DevOps হচ্ছে কিছু practice, tools, process গুলো এবং এমনকি কোম্পানির লোকেদের একটি সেট যা একটি দলের মধ্যে আরও বেশি সহযোগিতা এবং দ্রুত, আরও নির্ভরযোগ্য product release এর উদ্দেশ্য রাখে।<br>
![Alt text](/helper/images/image.png)


for more about [devops](https://github.com/yasin-arafat-05/rest_api_fastapi/blob/main/helper/devops.md)


<br> <br> <br>

# Create Docker for fastapi: 

- first, create requirement.txt file with a single command: ```pip freeze > requirement.txt```
- then, create a file name `Dockerfile` and follow the steps below:
    - **Choose a Base Image:** Start by choosing a base image that includes the necessary Python runtime and libraries. For FastAPI, using an image with a Python runtime is common. Here's an example using the `python:3.9` image as a base:
    <br>

    ```Dockerfile
    FROM python:3.9
    ```
    <br>

    - **Set the Working Directory:**
    Set the working directory inside the container where your application code will be placed.
    <br>

    ```Dockerfile
    WORKDIR /app
    ```
    <br>
    - **Copy the Application Files:** Copy your FastAPI application files (Python scripts, requirements.txt, etc.) into the container.
    <br>

   ```Dockerfile
   COPY . /app
   ```
    <br>

    -  **Install Dependencies:** Install the required dependencies using `pip`. This step involves copying the `requirements.txt` file into the container and running `pip install`.

    <br>

   ```Dockerfile
   COPY requirements.txt .
   RUN pip install --no-cache-dir -r requirements.txt
   ```

    <br>

    - **Expose the Port:**
   Expose the port that your FastAPI application will run on.
    <br>

   ```Dockerfile
   EXPOSE 8000
   ```
    <br>

    - **Command to Run the Application:**
   Specify the command to run your FastAPI application. Typically, you'll use `uvicorn` to run the FastAPI app.
    <br>

   ```Dockerfile
   CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
   ```
    <br>

   Make sure to adjust the `"main:app"` part based on your project structure.
    <br>

    - **Build and Run the Docker Image:**
   Build the Docker image using the following command:
    <br>

   ```bash
   docker build -t my-fastapi-app .
   ```
    <br>

   Replace "my-fastapi-app" with the desired image name.
    <br>
    - **Run the Docker Container:**
   Run the Docker container based on the image you just built.
    <br>

   ```bash
   docker run -p 8000:8000 my-fastapi-app
   ```
    <br>
   This assumes your FastAPI application is set to run on port 8000.
<br>

Here's the complete Dockerfile:
<br>

```Dockerfile
FROM python:3.9

WORKDIR /app

COPY . /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```
<br><br><br>

